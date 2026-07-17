import random
import string

print("=" * 50)
print("        PASSWORD GENERATOR")
print("=" * 50)

while True:

    print("\n1. Generate Password")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        length = int(input("Enter Password Length: "))

        if length < 4:
            print("Password length should be at least 4.")
            continue

        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation

        all_characters = lowercase + uppercase + digits + symbols

        password = (
            random.choice(lowercase)
            + random.choice(uppercase)
            + random.choice(digits)
            + random.choice(symbols)
        )

        for i in range(length - 4):
            password += random.choice(all_characters)

        password = ''.join(random.sample(password, len(password)))

        print("\nGenerated Password:", password)

    elif choice == "2":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")