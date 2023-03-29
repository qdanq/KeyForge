import random
import string


def generate_password(password_len, uppercase_include=True, lowercase_include=True, numbers_include=True, symbols_include=True):
    characters = ''
    if uppercase_include != "n":
        characters += string.ascii_uppercase
    if lowercase_include != "n":
        characters += string.ascii_lowercase
    if numbers_include != "n":
        characters += string.digits
    if symbols_include != "n":
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(password_len))


try:
    get_password_len = int(input("Enter length of password(default - 16): "))
except ValueError:
    get_password_len = 16

get_uppercase_include = input("Do you want to include uppercase letters? (y/n): ").lower() == 'y'

get_lowercase_include = input(
    "Do you want to include lowercase letters? (y/n): ").lower() == 'y'

get_numbers_include = input(
    "Do you want to include numbers? (y/n): ").lower() == 'y'

get_symbols_include = input("Do you want to include symbols? (y/n): ").lower() == 'y'

password = generate_password(get_password_len, get_uppercase_include, get_lowercase_include, get_numbers_include, get_symbols_include)
print(password)
