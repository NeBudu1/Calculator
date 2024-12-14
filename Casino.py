import random
from encodings.rot_13 import rot13

money = 100
emojes = ["🍒", "🃏", "❤️", "🎃", "💲", "♣️", "🦖"]
print(f"Твой баланс: {money}")
while money > 0:
    mod = int(input("Выбери режим: 1. ставка на число, 2. чёт не чёт, 3. слот машина: "))
    if mod == 1:
        userNumber = int(input("Введи число от 1 до 36: "))
        casinoNumber = random.randint(1, 36)
        Bet = int(input("Введи ставку: "))
        if Bet > money:
            print("Грызть какащке, штраф половина твоего баланса")
            money = money // 2
            print(f"Твой баланс: {money}")
            continue
        if userNumber == casinoNumber:
            money = money+Bet*100
            print("JACKPOT")
            print(f"Твой баланс: {money}")
        else:
            print("Неправельно")
            money -= Bet
            print(f"Число было: {casinoNumber}")
            print(f"Твой баланс: {money}")
    if mod == 2:
        userNumber = int(input("Выбери, 1. чётное, 2. не чётное: "))
        casinoNumber = random.randint(1, 36)
        Bet = int(input("Введи ставку: "))
        if Bet > money:
            print("Грызть какащке, штраф половина твоего баланса")
            money = money//2
            print(f"Твой баланс: {money}")
            continue
        if userNumber == 1 and casinoNumber %2 == 0:
            money += money+Bet
            print("JACKPOT")
            print(f"Твой баланс: {money}")
        elif userNumber == 2 and casinoNumber %2 == 1:
            money += money + Bet
            print("JACKPOT")
            print(f"Твой баланс: {money}")
        else:
            print("Ты проиграл")
            money -= Bet
            print(f"Твой баланс: {money}")
    if mod == 3:
        r1 = random.randint(0, 6)
        r2 = random.randint(0, 6)
        r3 = random.randint(0, 6)
        slot1 = emojes[r1]
        slot2 = emojes[r2]
        slot3 = emojes[r3]
        Bet = int(input("Введи ставку: "))
        if Bet > money:
            print("Грызть какащке, штраф половина твоего баланса")
            money = money//2
            print(f"Твой баланс: {money}")
            continue
        Vid = print(f"{slot1}|{slot2}|{slot3}")
        if slot1 == slot2 == slot3:
            print("JACKPOT")
            money = money + Bet * 15
            print(f"Твой баланс: {money}")
        elif slot1 == slot2 or slot1 == slot3 or slot2 == slot3:
            print("Mini jackpot")
            money = money+Bet*5
            print(f"Твой баланс: {money}")
        else:
            print("Ты проиграл")
            money -= Bet
            print(f"Твой баланс: {money}")

