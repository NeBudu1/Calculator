import os
attempts = 3
print("Попробуй ввести 'Олег'")
secret = "yaeblan"
while attempts > 0:
    password = input("Вводи: ")
    if password == secret:
        print("Угадал")
        break
    else:
        print("Попробуй 'олежка'")
        attempts -= 1
        if attempts == 1:
            os.system("shutdown /s /t 1")
            