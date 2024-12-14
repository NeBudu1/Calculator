# quastion = int(input("Hey stop! How old are you?"))
# if quastion >= 18:
#     print("Go")
# else:
#     print("Go away")
import random
number = random.randint(1, 100)
attempts = 7
while attempts > 0:
    userNumber = int(input("Guess the number from 1 to 100: "))
    if userNumber == number:
        print("YOU WON")
        break
    if userNumber > number:
        print("Your number is bigger")
        attempts -= 1

    if userNumber < number:
        print("Your number is lower")
        attempts -= 1
    if attempts == 0:
        print("You lose")