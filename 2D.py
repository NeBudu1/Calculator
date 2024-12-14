# def abc(name):
#     print(f"Hi {name}")
#     print("Привет")
#     print("Привіт козаче")
# abc(input("Введи имя: "))
import tkinter
window = tkinter.Tk()
window.geometry("800x500")
text1 = tkinter.Label(text="Калькулятор", font = ("Impact", 35))
text1.place(x = 280, y = 0)
def clear():
    input1.delete(0, 20)
    input2.delete(0, 20)
    text4["text"] = "?"
def plus():
    print()
    number1 = int(input1.get())
    number2 = int(input2.get())
    text4["text"] = f"{number1 + number2}"
def minus():
    number1 = int(input1.get())
    number2 = int(input2.get())
    text4["text"] = f"{number1 - number2}"
def umnoshitb():
    number1 = int(input1.get())
    number2 = int(input2.get())
    text4["text"] = f"{number1 * number2}"
def delit():
    number1 = int(input1.get())
    number2 = int(input2.get())
    text4["text"] = f"{number1 / number2}"
button1 = tkinter.Button(text = "+", font = ("Impact", 35), width = 2, border = 5, command = plus)
button1.place(x = 20, y = 300)
button2 = tkinter.Button(text = "-", font = ("Impact", 35), width = 2, border = 5, command = minus)
button2.place(x = 100, y = 300)
input1 = tkinter.Entry(font = ("Impact", 20), width = 7)
input1.place(x = 100, y = 150)
text2 = tkinter.Label(text = "Введи первую цифру", font = ("Impact", 20))
text2.place(x = 30, y = 180)
input2 = tkinter.Entry(font = ("Impact", 20), width = 7)
input2.place(x = 550, y = 150)
text3 = tkinter.Label(text = "Введи вторую цифру", font = ("Impact", 20))
text3.place(x = 470, y = 180)
text4 = tkinter.Label(text = "?", font = ("Impact", 30))
text4.place(x = 350, y = 150)
button3 = tkinter.Button(text = "*", font = ("Impact", 35), width = 2, border = 5, command = umnoshitb)
button3.place(x = 180, y = 300)
button4 = tkinter.Button(text = ":", font = ("Impact", 35), width = 2, border = 5, command = delit)
button4.place(x = 260, y = 300)
button5 = tkinter.Button(text = "C", font = ("Impact", 35), width = 2, border = 5, command = clear)
button5.place(x = 340, y = 300)


window.mainloop()
