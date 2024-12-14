import random
level = int(input("Choose dificalt: 1. easy, 2. normal, 3. hard: "))
round = 0
point = 0
if level == 1:
    while round < 10:
        n1 = random.randint(1, 100)
        n2 = random.randint(1, 100)
        answer = int(input(f"{n1}+{n2}= "))
        if answer == n1+n2:
            print("Next")
            round += 1
            point += 1
        else:
            print("Next")
            round += 1

if level == 2:
    while round <10:
        n1 = random.randint(-200, 200)
        n2 = random.randint(-200, 200)
        sine = "+"
        if n2 < 0:
            sine = ""
        answer = int(input(f"{n1}{sine}{n2}= "))
        if answer == n1 + n2:
            print("Next")
            round += 1
            point += 1
        else:
            print("Next")
            round += 1
if level == 3:
    while round < 10:
        n1 = random.randint(1, 50)
        n2 = random.randint(1, 50)
        answer = int(input(f"{n1}*{n2}= "))
        if answer == n1 * n2:
            print("Next")
            round += 1
            point += 1
        else:
            print("Next")
            round += 1
print(f"Your points: {point * 10}")