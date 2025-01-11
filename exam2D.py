import tkinter
import random
import tkinter.messagebox
window = tkinter.Tk()
window.geometry("500x500+0+200")
points = 0
rounds = 0
def easy():
    def check():
        global rounds
        while rounds < 10:
            if int(inputNumber.get()) == number1+number2:
                global points
                points += 10
                print(f"{points}")
                rounds += 1
                window2.destroy()
                easy()
            else:
                rounds += 1
                window2.destroy()
                easy()
        tkinter.messagebox.showinfo("kolobok", f"Ты набрал {points} баллов")
        window2.destroy()
    window2 = tkinter.Tk()
    window2.geometry("500x500+500+200")
    number1 = random.randint(1,100)
    number2 = random.randint(1, 100)
    numbers1 = tkinter.Label(window2, text = f"{number1}+{number2}=", font = ("Impact", 25))
    numbers1.place(x = 200, y = 100)
    inputNumber = tkinter.Entry(window2, font = ("Impact", 25), width = 5)
    inputNumber.place(x = 300, y = 100)
    checkButton = tkinter.Button(window2, text = "Check", font = ("Impact", 25), width = 5, command = check)
    checkButton.place(x = 250, y = 150)
def normal():
    def check():
        global rounds
        while rounds < 10:
            if int(inputNumber.get()) == number1 + number2:
                global points
                points += 10
                print(f"{points}")
                rounds += 1
                window2.destroy()
                normal()
            else:
                rounds += 1
                window2.destroy()
                normal()
        tkinter.messagebox.showinfo("kolobok", f"Ты набрал {points} баллов")
        window2.destroy()
    window2 = tkinter.Tk()
    window2.geometry("500x500+500+200")
    number1 = random.randint(-200,200)
    number2 = random.randint(-200, 200)
    sine = "+"
    if number2 < 0:
        sine = ""
    numbers1 = tkinter.Label(window2, text = f"{number1}{sine}{number2}=", font = ("Impact", 25))
    numbers1.place(x = 200, y = 100)
    inputNumber = tkinter.Entry(window2, font = ("Impact", 25), width = 5)
    inputNumber.place(x = 300, y = 100)
    checkButton = tkinter.Button(window2, text = "Check", font = ("Impact", 25), width = 5, command = check)
    checkButton.place(x = 250, y = 150)
def hard():
    def check():
        global rounds
        while rounds < 10:
            if int(inputNumber.get()) == number1 * number2:
                global points
                points += 10
                print(f"{points}")
                rounds += 1
                window2.destroy()
                hard()
            else:
                rounds += 1
                window2.destroy()
                hard()
        tkinter.messagebox.showinfo("kolobok", f"Ты набрал {points} баллов")
        window2.destroy()

    window2 = tkinter.Tk()
    window2.geometry("500x500+500+200")
    number1 = random.randint(1, 50)
    number2 = random.randint(1, 50)
    numbers1 = tkinter.Label(window2, text=f"{number1}*{number2}=", font=("Impact", 25))
    numbers1.place(x=200, y=100)
    inputNumber = tkinter.Entry(window2, font=("Impact", 25), width=5)
    inputNumber.place(x=300, y=100)
    checkButton = tkinter.Button(window2, text="Check", font=("Impact", 25), width=5, command=check)
    checkButton.place(x=250, y=150)
button1 = tkinter.Button(text = "Легко", font = ("Impact", 20), width = 10, border = 5, command = easy)
button1.place(x = 50, y = 200)
button2 = tkinter.Button(text = "Нормально", font = ("Impact", 20), width = 10, border = 5, command = normal)
button2.place(x = 210, y = 200)
button3 = tkinter.Button(text = "Сложно", font = ("Impact", 20), width = 10, border = 5, command = hard)
button3.place(x = 370, y = 200)


window.mainloop()