import tkinter
import tkinter.messagebox
window = tkinter.Tk()
window.geometry("530x540")
step = 1
buttons = []
def click(bt):
    print(bt)
    global step
    if step == 1 and bt["text"] == " " or step == 3 and bt["text"] == " " or step == 5 and bt["text"] == " " or step == 7 and bt["text"] == " " or step == 9 and bt["text"] == " ":
        bt["text"] = "X"
        step += 1
    else:
        if bt["text"] == " ":
            bt["text"] = "0"
            step += 1

    if check() == "X":
        tkinter.messagebox.showinfo("Победитель", "Победил крестик")
        restart()
    if check() == "0":
        tkinter.messagebox.showinfo("Победитель", "Победил нолик")
        restart()

def check():
    if buttons[0]["text"] == buttons[1]["text"] == buttons[2]["text"]:
        return buttons[0]["text"]
    if buttons[3]["text"] == buttons[4]["text"] == buttons[5]["text"]:
        return buttons[5]["text"]
    if buttons[6]["text"] == buttons[7]["text"] == buttons[8]["text"]:
        return buttons[6]["text"]

    if buttons[0]["text"] == buttons[3]["text"] == buttons[6]["text"]:
        return buttons[0]["text"]
    if buttons[1]["text"] == buttons[4]["text"] == buttons[7]["text"]:
        return buttons[1]["text"]
    if buttons[2]["text"] == buttons[5]["text"] == buttons[8]["text"]:
        return buttons[2]["text"]

    if buttons[0]["text"] == buttons[4]["text"] == buttons[8]["text"]:
        return buttons[0]["text"]
    if buttons[2]["text"] == buttons[4]["text"] == buttons[6]["text"]:
        return buttons[2]["text"]
    if step == 10:
        tkinter.messagebox.showinfo("Ничья", "У вас ничья")
        restart()
def restart():
    global step
    for e in buttons:
        e["text"] = " "
    step = 1
    window.update()
for i in range(3):
    for a in range(3):
        button1 = tkinter.Button(text=" ", font=("Impact", 60), width=4, border=3, )
        button1["command"] = lambda btn = button1:click(btn)
        button1.place(x = a*170+10, y = i*180)
        buttons.append(button1)


window.mainloop()
