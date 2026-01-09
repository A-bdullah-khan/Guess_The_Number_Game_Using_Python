from random import randint

guess = 0
number = randint(1 , 100)
estimation = 0
name = input("Tell me your name: ")

print(f"Hello {name} I have though of a number for you between 1 and 100\nYou have 8 attempts to guess it")

while guess < 8:
    estimation = int(input("Enter your number: "))
    guess = guess +1

    if estimation > number:
        print("Your guessed number is high")
    elif estimation < number:
        print("Your guessed number is low")
    elif estimation > 100:
        print("Your guessed number is not in game")
    else:
        print(f"Congrats! {name}, You have guessed the number correct in {guess} attempts")
        break

if estimation != number:
    print(f"Sorry you are out of attempts, The secret number was {number}")