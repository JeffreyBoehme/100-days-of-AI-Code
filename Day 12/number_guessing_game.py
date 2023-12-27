import random
from art import GRAPHIC, TOO_HIGH, TOO_LOW, WINNER, LOSER

print(GRAPHIC)

difficulty = input("Choose a Difficulty. \nType 'hard' or 'easy'. ")

number = random.randint(1, 100)

attempts = 0
if difficulty == "hard":
    attempts = 5
else:
    attempts = 10


while attempts > 0:
    guess = input(
        "Choose a number between 1 and 100. \nPress enter when you are ready. "
    )
    if guess == "":
        print("You need to enter a number")
        continue
    guess = int(guess)
    if guess == number:
        print(WINNER)
        print("You guessed Correctly!")
        print(f"you still had {attempts} attempts left")
        break
    elif guess > number:
        print(TOO_HIGH)
        attempts -= 1
        print(f"You have {attempts} attempts left")
    elif guess < number:
        print(TOO_LOW)
        attempts -= 1
        print(f"You have {attempts} attempts left")

if attempts == 0:
    print(LOSER)
    print(f"The number was {number}")
