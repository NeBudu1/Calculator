import tkinter as tk
from random import randrange
from typing import List, Tuple


class SnakeGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Змейка")
        self.root.config(bg='#2C3E50')

        # Константы игры
        self.WIDTH = 600
        self.HEIGHT = 400
        self.CELL_SIZE = 20
        self.SPEED = 100

        # Создаем холст
        self.canvas = tk.Canvas(
            self.root,
            width=self.WIDTH,
            height=self.HEIGHT,
            bg='#34495E',
            highlightthickness=0
        )
        self.canvas.pack(padx=10, pady=10)

        # Инициализация змейки
        self.snake: List[Tuple[int, int]] = [(100, 100), (80, 100), (60, 100)]
        self.direction = "Right"
        self.new_direction = "Right"

        # Создаем первую еду
        self.food = self.create_food()

        # Счет
        self.score = 0
        self.score_label = tk.Label(
            self.root,
            text=f"Счет: {self.score}",
            fg='white',
            bg='#2C3E50',
            font=('Helvetica', 16)
        )
        self.score_label.pack(pady=5)

        # Привязка клавиш
        self.root.bind('<Left>', lambda e: self.change_direction('Left'))
        self.root.bind('<Right>', lambda e: self.change_direction('Right'))
        self.root.bind('<Up>', lambda e: self.change_direction('Up'))
        self.root.bind('<Down>', lambda e: self.change_direction('Down'))

        # Запуск игры
        self.game_loop()
        self.root.mainloop()

    def create_food(self) -> Tuple[int, int]:
        while True:
            x = randrange(1, (self.WIDTH - 20) // self.CELL_SIZE) * self.CELL_SIZE
            y = randrange(1, (self.HEIGHT - 20) // self.CELL_SIZE) * self.CELL_SIZE
            if (x, y) not in self.snake:
                return (x, y)

    def change_direction(self, new_dir: str):
        opposites = {'Left': 'Right', 'Right': 'Left', 'Up': 'Down', 'Down': 'Up'}
        if opposites[new_dir] != self.direction:
            self.new_direction = new_dir

    def game_loop(self):
        self.direction = self.new_direction

        # Определяем новую позицию головы
        head = self.snake[0]
        if self.direction == 'Left':
            new_head = (head[0] - self.CELL_SIZE, head[1])
        elif self.direction == 'Right':
            new_head = (head[0] + self.CELL_SIZE, head[1])
        elif self.direction == 'Up':
            new_head = (head[0], head[1] - self.CELL_SIZE)
        else:  # Down
            new_head = (head[0], head[1] + self.CELL_SIZE)

        # Проверка столкновений
        if (new_head in self.snake or
                new_head[0] < 0 or
                new_head[0] >= self.WIDTH or
                new_head[1] < 0 or
                new_head[1] >= self.HEIGHT):
            self.game_over()
            return

        self.snake.insert(0, new_head)

        # Проверка, съела ли змея еду
        if new_head == self.food:
            self.score += 10
            self.score_label.config(text=f"Счет: {self.score}")
            self.food = self.create_food()
        else:
            self.snake.pop()

        # Отрисовка
        self.canvas.delete('all')

        # Отрисовка еды
        self.canvas.create_oval(
            self.food[0], self.food[1],
            self.food[0] + self.CELL_SIZE, self.food[1] + self.CELL_SIZE,
            fill='#E74C3C',
            outline='#C0392B'
        )

        # Отрисовка змеи
        for i, segment in enumerate(self.snake):
            color = '#2ECC71' if i == 0 else '#27AE60'  # Голова зеленее
            self.canvas.create_rectangle(
                segment[0], segment[1],
                segment[0] + self.CELL_SIZE, segment[1] + self.CELL_SIZE,
                fill=color,
                outline='#219A52'
            )

        self.root.after(self.SPEED, self.game_loop)

    def game_over(self):
        self.canvas.create_text(
            self.WIDTH / 2, self.HEIGHT / 2,
            text="Игра окончена!",
            fill='white',
            font=('Helvetica', 24)
        )
        self.canvas.create_text(
            self.WIDTH / 2, self.HEIGHT / 2 + 40,
            text=f"Финальный счет: {self.score}",
            fill='white',
            font=('Helvetica', 18)
        )


if __name__ == "__main__":
    SnakeGame()