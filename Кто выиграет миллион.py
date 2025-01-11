import tkinter
import random
import time

window = tkinter.Tk()
window.geometry("1200x700")
questions = [
    "Какой год был основан Рим?",
    "Кто написал 'Войну и мир'?",
    "Сколько планет в Солнечной системе?",
    "Какой химический элемент обозначается символом 'O'?",
    "Кто изобрел лампу накаливания?",
    "Какой самый большой океан на Земле?",
    "Кто первый человек, ступивший на Луну?",
    "Как называется столица Австралии?",
    "Какое животное является символом WWF?",
    "В каком году произошла Великая Французская революция?",
    "Какой самый большой континент на Земле?",
    "Кто основал компанию Microsoft?",
    "Какой язык программирования создал Гвидо ван Россум?",
    "Какая планета известна как красная планета?",
    "Какой химический элемент имеет символ 'Na'?",
    "Как называется самое высокое здание в мире?",
    "Кто написал 'Гарри Поттера'?",
    "Какое уравнение описывает закон гравитации Ньютона?",
    "Кто автор картины 'Мона Лиза'?",
    "Как называется самая длинная река в мире?",
    "Какое число 'π' приближенно равно?",
    "Какая формула описывает отношение массы к энергии?",
    "Как зовут главного героя 'Божественной комедии' Данте?",
    "Какая планета самая большая в Солнечной системе?",
    "Какое животное самое быстрое на суше?",
    "Кто первый президент США?",
    "Как называется столица Японии?",
    "Какой химический элемент обозначается символом 'Au'?",
    "В каком году началась Вторая мировая война?",
    "Как называется самое глубокое озеро в мире?",
]
answers = [
    ["753 до н.э.", "509 до н.э.", "27 до н.э.", "1 до н.э."],
    ["Лев Толстой", "Федор Достоевский", "Антон Чехов", "Александр Пушкин"],
    ["7", "8", "9", "10"],
    ["Кислород", "Углерод", "Азот", "Водород"],
    ["Томас Эдисон", "Александр Белл", "Никола Тесла", "Майкл Фарадей"],
    ["Тихий океан", "Атлантический океан", "Индийский океан", "Северный Ледовитый океан"],
    ["Нил Армстронг", "Юрий Гагарин", "Базз Олдрин", "Майкл Коллинз"],
    ["Канберра", "Сидней", "Мельбурн", "Брисбен"],
    ["Панда", "Тигр", "Слон", "Белый медведь"],
    ["1789", "1776", "1804", "1799"],
    ["Азия", "Африка", "Европа", "Америка"],
    ["Билл Гейтс", "Стив Джобс", "Марк Цукерберг", "Ларри Пейдж"],
    ["Python", "Java", "C++", "Ruby"],
    ["Марс", "Венера", "Юпитер", "Сатурн"],
    ["Натрий", "Неон", "Никель", "Нобелий"],
    ["Бурдж-Халифа", "Эйфелева башня", "Эмпайр-Стейт-Билдинг", "Петронас Тауэрс"],
    ["Дж.К. Роулинг", "Стивен Кинг", "Джордж Мартин", "Сьюзан Коллинз"],
    ["F = G (m₁m₂)/r²", "E = mc²", "P = IV", "V = IR"],
    ["Леонардо да Винчи", "Микеланджело", "Рафаэль", "Винсент ван Гог"],
    ["Амазонка", "Нил", "Миссисипи", "Янцзы"],
    ["3.14", "3.15", "3.16", "3.17"],
    ["E = mc²", "F = ma", "P = IV", "V = IR"],
    ["Данте Алигьери", "Вергілій", "Беатриче", "Фарината"],
    ["Юпитер", "Сатурн", "Нептун", "Уран"],
    ["Гепард", "Лев", "Лошадь", "Антилопа"],
    ["Джордж Вашингтон", "Томас Джефферсон", "Абрахам Линкольн", "Джон Адамс"],
    ["Токио", "Киото", "Осака", "Нагоя"],
    ["Золото", "Серебро", "Медь", "Платина"],
    ["1939", "1914", "1941", "1945"],
    ["Байкал", "Танганьика", "Виктория", "Эри"],
]
def getQuestion():
    r1 = random.randint(0, 29)
    variants = answers[r1]
    questionnnn = questions[r1]
    answer = variants[0]
    random.shuffle(variants)
    return [questionnnn, variants, answer]

q, v, a = getQuestion()
quastion = tkinter.Label(text = q, font = ("Impact", 30))
quastion.pack()
level = 1
moneyLabel = 0
rounds = tkinter.Label(text = f"Раунд: {level}", font = ("Impact", 30))
money = tkinter.Label(text = f"Деньги: {moneyLabel}", font = ("Impact", 30))
rounds.place(x = 800, y = 100)
money.place(x = 800, y = 150)
def answer1():
    global a, q, v
    global level
    global moneyLabel
    global rounds
    global money
    useranswer = button1["text"]
    if useranswer == a:
        print("Харош")
        button1["background"] = "green"
        window.update()
        time.sleep(1)
        q, v, a = getQuestion()
        button1["text"] = v[0]
        quastion["text"] = q
        button2["text"] = v[1]
        button3["text"] = v[2]
        button4["text"] = v[3]
        button1["background"] = "white"
        level += 1
        moneyLabel += 100
        rounds["text"] = f"Раунд: {level}"
        money["text"] = f"Деньги: {moneyLabel}"
        window.update()
    else:
        button1["background"] = "red"
        window.update()
        time.sleep(1)
        window.destroy()
def answer2():
    global q, v, a
    global level
    global moneyLabel
    global rounds
    global money
    useranswer = button2["text"]
    if useranswer == a:
        print("Харош")
        button2["background"] = "green"
        window.update()
        time.sleep(1)
        q, v, a = getQuestion()
        button1["text"] = v[0]
        quastion["text"] = q
        button2["text"] = v[1]
        button3["text"] = v[2]
        button4["text"] = v[3]
        button2["background"] = "white"
        level += 1
        moneyLabel += 100
        rounds["text"] = f"Раунд: {level}"
        money["text"] = f"Деньги: {moneyLabel}"
        window.update()
    else:
        button2["background"] = "red"
        window.update()
        time.sleep(1)
        window.destroy()
def answer3():
    global q, v, a
    global level
    global moneyLabel
    global rounds
    global money
    useranswer = button3["text"]
    if useranswer == a:
        print("Харош")
        button3["background"] = "green"
        window.update()
        time.sleep(1)
        q, v, a = getQuestion()
        button1["text"] = v[0]
        quastion["text"] = q
        button2["text"] = v[1]
        button3["text"] = v[2]
        button4["text"] = v[3]
        button3["background"] = "white"
        level += 1
        moneyLabel += 100
        rounds["text"] = f"Раунд: {level}"
        money["text"] = f"Деньги: {moneyLabel}"
        window.update()
    else:
        button3["background"] = "red"
        window.update()
        time.sleep(1)
        window.destroy()
def answer4():
    global q, v, a
    global level
    global moneyLabel
    global rounds
    global money
    useranswer = button4["text"]
    if useranswer == a:
        print("Харош")
        button4["background"] = "green"
        window.update()
        time.sleep(1)
        q, v, a = getQuestion()
        button1["text"] = v[0]
        quastion["text"] = q
        button2["text"] = v[1]
        button3["text"] = v[2]
        button4["text"] = v[3]
        button4["background"] = "white"
        level += 1
        moneyLabel += 100
        rounds["text"] = f"Раунд: {level}"
        money["text"] = f"Деньги: {moneyLabel}"
        window.update()
    else:
        button4["background"] = "red"
        window.update()
        time.sleep(1)
        window.destroy()
button1 = tkinter.Button(text = v[0], font = ("Impact", 20), width = 20, border = 5, command = answer1)
button2 = tkinter.Button(text = v[1], font = ("Impact", 20), width = 20, border = 5, command = answer2)
button3 = tkinter.Button(text = v[2], font = ("Impact", 20), width = 20, border = 5, command = answer3)
button4 = tkinter.Button(text = v[3], font = ("Impact", 20), width = 20, border = 5, command = answer4)
button1.place(x = 200, y = 400)
button2.place(x = 700, y = 400)
button3.place(x = 200, y = 600)
button4.place(x = 700, y = 600)
window.mainloop()