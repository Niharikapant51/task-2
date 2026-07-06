import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ""

    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return None

    password = ""

    # Make sure at least one character from each selected category is included
    if use_upper:
        password += random.choice(string.ascii_uppercase)
    if use_lower:
        password += random.choice(string.ascii_lowercase)
    if use_digits:
        password += random.choice(string.digits)
    if use_symbols:
        password += random.choice(string.punctuation)

    while len(password) < length:
        password += random.choice(characters)

    password = list(password)
    random.shuffle(password)

    return "".join(password)


def password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Medium"
    else:
        return "Strong"


print("=" * 40)
print("      PYTHON PASSWORD GENERATOR")
print("=" * 40)

try:
    length = int(input("Enter password length: "))

    if length < 4:
        print("Password length should be at least 4.")
        exit()

    upper = input("Include Uppercase Letters? (y/n): ").lower() == "y"
    lower = input("Include Lowercase Letters? (y/n): ").lower() == "y"
    digits = input("Include Numbers? (y/n): ").lower() == "y"
    symbols = input("Include Symbols? (y/n): ").lower() == "y"

    password = generate_password(length, upper, lower, digits, symbols)

    if password:
        print("\nGenerated Password:")
        print(password)

        print("\nPassword Strength:", password_strength(password))

        save = input("\nDo you want to save the password to a file? (y/n): ").lower()

        if save == "y":
            with open("passwords.txt", "a") as file:
                file.write(password + "\n")
            print("Password saved to passwords.txt")

    else:
        print("Please select at least one character type.")

except ValueError:
    print("Please enter a valid number.")