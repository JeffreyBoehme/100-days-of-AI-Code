import random

computer_score = 0
player_score = 0

choices = [
    "    _______\n---'   ____)\n      (_____)\n      (_____)\n      (____)\n---.__(___)\n",
    "    _______\n---'   ____)____\n          ______)\n          _______)\n         _______)\n---.__________)\n",
    "    _______\n---'   ____)____\n          ______)\n          _______)\n      (____)\n---.__(___)\n",
]


def print_choice(name, result):
    match int(result):
        case 0:
            print(f"{name} chose Rock\n")
            print(choices[0])
        case 1:
            print(f"{name} chose Paper\n")
            print(choices[1])
        case 2:
            print(f"{name} chose Scissors\n")
            print(choices[0])
        case _:
            print("Invalid choice\n")


def who_wins(choice: int, computer_choice: int):
    global computer_score
    global player_score
    match (choice, computer_choice):
        case (0, 0) | (1, 1) | (2, 2):
            print("It's a draw")
        case (0, 1) | (1, 2) | (2, 0):
            print("The computer wins!")
            computer_score += 1
        case (0, 2) | (1, 0) | (2, 1):
            print("You win!")
            player_score += 1


play_again = "yes"

while play_again == "yes":
    choice = input("Make your choice? 0 for Rock, 1 for Paper, 2 for Scissors. \n")
    print_choice("You", choice)

    computer_choice = random.randint(0, 2)
    print_choice("Computer", computer_choice)

    who_wins(choice, computer_choice)
    print(f"The curren score is Player: {player_score} Computer: {computer_score}")
    if player_score > computer_score:
        print("You are winning!")
    elif computer_score > player_score:
        print("The computer is winning!")
    else:
        print("It's a draw!")
    play_again = input("Do you want to play again? yes or no\n").lower()
