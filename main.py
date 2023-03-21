import random
import string


class PasswordGenerator:
    def __init__(self, password_len, uppercase_include):
        self.password_len = password_len
        self.uppercase_include = uppercase_include

    def __str__(self):
        return ''.join(
            [random.choice(self.uppercase_include + string.ascii_lowercase + string.digits + string.punctuation) for
             n in
             range(self.password_len)])


try:
    get_password_len = int(input("Enter length of password(default - 16): "))
except ValueError:
    get_password_len = 16

get_uppercase_include = input("Do you want to include uppercase letters?(default: yes, type '0' to not include)")
if get_uppercase_include != "0":
    get_uppercase_include = string.ascii_uppercase

options = PasswordGenerator(get_password_len, get_uppercase_include)

print(options)
