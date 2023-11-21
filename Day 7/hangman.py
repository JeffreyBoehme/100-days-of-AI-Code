from random_word import RandomWords

words = RandomWords()

current_word = ""
chars = []
solved_chars = []
guesses = []

incorrect_guesses = 0

HANGMANPICS = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
]


def generateWord():
    word = words.get_random_word()
    return word


def splitWord(word):
    global chars
    global solved_chars
    global current_word
    current_word = word
    for char in str(word):
        chars.append(char)
        solved_chars.append("_")


def checkChar(char):
    global incorrect_guesses
    global guesses
    correctGuess = False
    guesses.append(char)

    for index, guess in enumerate(guesses):
        if guess == char:
            print("You already chose this character")
            break

    for index, letter in enumerate(chars):
        if letter == char:
            solved_chars[index] = char
            chars[index] = "_"
            correctGuess = True

    if correctGuess == False:
        incorrect_guesses += 1
    return correctGuess


def updateDisplay():
    solved = ""
    for char in solved_chars:
        solved = solved + str(char)
    print(solved)
    print(HANGMANPICS[incorrect_guesses])


def playGame(choice):
    correct = checkChar(choice)
    winner = True
    if correct == None:
        print("Choose again \n")

    if correct == True:
        print("You chose correctly")
        updateDisplay()
    if correct == False:
        if incorrect_guesses == 6:
            print("You Lose!")
            print(f"The word was {current_word}")
            exit()
        print("You chose incorrectly")
        updateDisplay()
    for char in solved_chars:
        if char == "_":
            winner = False
    print(f"Your Guesses: {guesses}")

    return winner


playing = True

currentWord = generateWord()
splitWord(currentWord)


while playing:
    playerChar = input("Enter a letter \n")
    if (len(playerChar) > 1) or (len(playerChar) < 1):
        print("Invalid choice, please pick again.")
        win = False
    else:
        win = playGame(playerChar)

    if win == True:
        print("You Win!")
        playing = False
