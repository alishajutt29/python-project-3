import random
import string


def get_length():
    while True:
        value = input("Enter desired password length: ")

        try:
            length = int(value)
        except ValueError:
            print("Please enter a whole number.")
            continue

        if length < 4:
            print("Password length should be at least 4.")
            continue

        return length


def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("Random Password Generator")
    print("--------------------------")

    length = get_length()
    password = generate_password(length)

    print(f"\nYour generated password is: {password}")


main()
