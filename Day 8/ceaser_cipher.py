action = input("Type Encode to Encrypt, or Decode to decrypt\n")
word = input("Enter the word: \n")
shift = input("What shift level would you like to use? - Enter a number\n")


alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def encode(word, shift):
    encoded_output = ""
    for letter in word:
        for index, char in enumerate(alphabet):
            if char == letter:
                charnum = index + int(shift)
                if charnum >= 26:
                    charnum = charnum - 26
                encoded_output = encoded_output + alphabet[charnum]
    print(encoded_output)


def decode(word, shift):
    decoded_output = ""
    for letter in word:
        for index, char in enumerate(alphabet):
            if char == letter:
                charnum = index - int(shift)
                if charnum < 0:
                    charnum = charnum + 26
                decoded_output = decoded_output + alphabet[charnum]
    print(decoded_output)


if action == "Encode":
    encode(word, shift)

elif action == "Decode":
    decode(word, shift)
else:
    print("Invalid choice")
