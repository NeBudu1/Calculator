# Файл: inventory_management_system.py
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import sqlite3
from datetime import datetime


class InventoryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Система управления инвентарем")
        self.root.geometry("800x600")

        # Инициализация базы данных
        self.conn = sqlite3.connect('inventory.db')
        self.create_tables()

        # Создание вкладок
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill='both')

        self.sales_frame = tk.Frame(self.notebook)
        self.add_product_frame = tk.Frame(self.notebook)
        self.view_products_frame = tk.Frame(self.notebook)

        self.notebook.add(self.sales_frame, text="Продажа")
        self.notebook.add(self.add_product_frame, text="Добавление")
        self.notebook.add(self.view_products_frame, text="Товары")

        # Настройка страниц
        self.setup_sales_page()
        self.setup_add_product_page()
        self.setup_view_products_page()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                barcode TEXT PRIMARY KEY,
                name TEXT,
                price REAL,
                category TEXT,
                quantity INTEGER
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                barcode TEXT,
                quantity INTEGER,
                sale_date DATETIME
            )
        ''')
        self.conn.commit()

    def setup_sales_page(self):
        # Фрейм для чека продаж
        sales_label = tk.Label(self.sales_frame, text="Чек продаж", font=('Arial', 16))
        sales_label.pack(pady=10)

        self.sales_tree = ttk.Treeview(self.sales_frame, columns=('Штрих-код', 'Название', 'Количество', 'Цена'),
                                       show='headings')
        self.sales_tree.heading('Штрих-код', text='Штрих-код')
        self.sales_tree.heading('Название', text='Название')
        self.sales_tree.heading('Количество', text='Количество')
        self.sales_tree.heading('Цена', text='Цена')
        self.sales_tree.pack(padx=10, pady=10, fill='both', expand=True)

        # Поле для ввода штрих-кода
        barcode_label = tk.Label(self.sales_frame, text="Введите штрих-код:")
        barcode_label.pack()

        self.barcode_entry = tk.Entry(self.sales_frame, width=30)
        self.barcode_entry.pack()
        self.barcode_entry.bind('<Return>', self.add_product_to_sales)

        # Кнопка оплаты
        pay_button = tk.Button(self.sales_frame, text="Оплатить", command=self.process_sale)
        pay_button.pack(pady=10)

    def add_product_to_sales(self, event=None):
        barcode = self.barcode_entry.get()
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM products WHERE barcode = ?", (barcode,))
        product = cursor.fetchone()

        if product:
            self.sales_tree.insert('', 'end', values=(product[0], product[1], 1, product[2]))
            self.barcode_entry.delete(0, 'end')
        else:
            messagebox.showerror("Ошибка", "Товар не найден")

    def process_sale(self):
        sales = self.sales_tree.get_children()
        if not sales:
            messagebox.showwarning("Внимание", "Чек пуст")
            return

        total = 0
        sale_date = datetime.now()
        cursor = self.conn.cursor()

        for sale in sales:
            values = self.sales_tree.item(sale)['values']
            barcode, name, quantity, price = values
            total = price * float(quantity)

            # Обновление базы данных продаж
            cursor.execute("INSERT INTO sales (barcode, quantity, sale_date) VALUES (?, ?, ?)",
                           (barcode, quantity, sale_date))

            # Уменьшение количества товара
            cursor.execute("UPDATE products SET quantity = quantity - ? WHERE barcode = ?",
                           (quantity, barcode))

        self.conn.commit()

        # Формирование чека
        receipt = f"Чек от {sale_date.strftime('%Y-%m-%d %H:%M:%S')}\n"
        for sale in sales:
            values = self.sales_tree.item(sale)['values']
            receipt += f"{values[1]} - {values[2]} x {values[3]} = {values[2] * values[3]}\n"
        receipt += f"Итого: {total}"

        messagebox.showinfo("Чек", receipt)

        # Очистка чека
        for sale in sales:
            self.sales_tree.delete(sale)

    def setup_add_product_page(self):
        # Поля для добавления товара
        labels = ['Штрих-код', 'Название', 'Цена', 'Категория', 'Количество']
        self.add_entries = {}

        for label_text in labels:
            frame = tk.Frame(self.add_product_frame)
            frame.pack(pady=5, padx=10, fill='x')

            label = tk.Label(frame, text=label_text, width=15)
            label.pack(side='left')

            entry = tk.Entry(frame, width=40)
            entry.pack(side='left', expand=True, fill='x')

            self.add_entries[label_text] = entry

        # Кнопка добавления товара
        add_button = tk.Button(self.add_product_frame, text="Добавить товар", command=self.add_product)
        add_button.pack(pady=10)

    def add_product(self):
        values = [entry.get() for entry in self.add_entries.values()]

        if not all(values):
            messagebox.showerror("Ошибка", "Заполните все поля")
            return

        cursor = self.conn.cursor()
        try:
            cursor.execute('''
                INSERT OR REPLACE INTO products 
                (barcode, name, price, category, quantity) 
                VALUES (?, ?, ?, ?, ?)
            ''', values)
            self.conn.commit()
            messagebox.showinfo("Успех", "Товар добавлен")

            # Очистка полей после добавления
            for entry in self.add_entries.values():
                entry.delete(0, 'end')
        except sqlite3.Error as e:
            messagebox.showerror("Ошибка базы данных", str(e))

    def setup_view_products_page(self):
        # Таблица товаров
        self.products_tree = ttk.Treeview(self.view_products_frame,
                                          columns=('Штрих-код', 'Название', 'Цена', 'Категория', 'Количество'),
                                          show='headings')

        for col in ['Штрих-код', 'Название', 'Цена', 'Категория', 'Количество']:
            self.products_tree.heading(col, text=col)

        self.products_tree.pack(padx=10, pady=10, fill='both', expand=True)

        # Кнопка обновления списка товаров
        refresh_button = tk.Button(self.view_products_frame, text="Обновить список", command=self.refresh_products)
        refresh_button.pack(pady=10)

        # Первоначальная загрузка товаров
        self.refresh_products()

    def refresh_products(self):
        # Очистка текущего дерева
        for item in self.products_tree.get_children():
            self.products_tree.delete(item)

        # Загрузка товаров из базы данных
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM products")
        for product in cursor.fetchall():
            self.products_tree.insert('', 'end', values=product)


def main():
    root = tk.Tk()
    app = InventoryManagementSystem(root)
    root.mainloop()


if __name__ == "__main__":
    main()