import random
import string


class PasswordOptions:
    def __init__(self, password_len):
        self.password_len = password_len


try:
    get_password_len = int(input("Enter length of password(default - 16): "))
except ValueError:
    get_password_len = 16

options = PasswordOptions(get_password_len)

rand = ''.join(
    [random.choice(string.ascii_letters + string.digits + string.punctuation) for n in range(options.password_range)])
print(rand)
