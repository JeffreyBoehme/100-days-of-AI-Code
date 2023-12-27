import random
from art import GRAPHIC, TOO_HIGH, TOO_LOW, WINNER, LOSER

print(GRAPHIC)

number = random.randint(1, 100)


def select_difficulty():
    difficulty = input("Choose a Difficulty. \nType 'hard' or 'easy'. ")
    if difficulty == "hard":
        attempts = 5
    else:
        attempts = 10
    return attempts


def guess():
    global attempts
    while True:
        guess = input(
            "Choose a number between 1 and 100. \nPress enter when you are ready: "
        )
        if guess == "":
            print("You need to enter a number")
            continue
        else:
            break
    guess = int(guess)
    if guess == number:
        print(WINNER)
        print("You guessed Correctly!")
        print(f"you still had {(attempts - 1)} attempts left")
        return True
    elif guess > number:
        print(TOO_HIGH)
        return False
    elif guess < number:
        print(TOO_LOW)

        return False


attempts = select_difficulty()


while attempts > 0:
    correct = guess()
    if correct == True:
        break
    attempts -= 1
    print(f"You have {attempts} attempts left")

if attempts == 0:
    print(LOSER)
    print(f"The number was {number}")
