import random
import string


class PasswordOptions:
    def __init__(self, password_len, uppercase_include):
        self.password_len = password_len
        self.uppercase_include = uppercase_include


try:
    get_password_len = int(input("Enter length of password(default - 16): "))
except ValueError:
    get_password_len = 16

get_uppercase_include = input("Do you want to include uppercase letters?(default: yes, type '0' to not include)")
if get_uppercase_include != "0":
    get_uppercase_include = string.ascii_uppercase

options = PasswordOptions(get_password_len, get_uppercase_include)

rand = ''.join(
    [random.choice(options.uppercase_include + string.ascii_lowercase + string.digits + string.punctuation) for n in
     range(options.password_len)])
print(rand)
