import random
import string

letters = int(input("How many letters would you like in your password?\n"))
symbols = int(input("How many symbols would you like?\n"))
numbers = int(input("How many numbers would you like?\n"))


password_length = letters + symbols + numbers
unique_symbols = "!@#$%^&*()_+-=[]{}|;:',.<>/?`~"

password = ""

individual_chars = []

for i in range(letters):
    individual_chars += random.choice(string.ascii_letters)
for i in range(symbols):
    individual_chars += str(random.choice(unique_symbols))
for i in range(numbers):
    individual_chars += str(random.randint(0, 9))

for i in range(len(individual_chars)):
    number = random.randint(0, (len(individual_chars) - 1))
    print(number)
    password += str(individual_chars[number])
    del individual_chars[number]

print(f"Your password is {password}")
