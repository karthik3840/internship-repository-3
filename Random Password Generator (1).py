import random
import string

while True:
    try:
        length = int(input("Enter password length: "))

        if length <= 0:
            print("Please enter a positive number.")
            continue

        break

    except ValueError:
        print("Please enter a valid integer.")

characters = (
    string.ascii_letters +
    string.digits +
    string.punctuation
)

password = ""

for i in range(length):
    password += random.choice(characters)

print("Generated Password:", password)