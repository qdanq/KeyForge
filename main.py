import random
import string
import tkinter as tk


# TODO: add requirements.txt


def generate_password(password_len, uppercase_include=True, lowercase_include=True, numbers_include=True,
                      symbols_include=True):
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


window = tk.Tk()
window.title("Password Generator")

options_frame = tk.Frame(window)
options_frame.pack(pady=10)

length_label = tk.Label(options_frame, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=5)
length_entry = tk.Entry(options_frame, width=5)
length_entry.grid(row=0, column=1)
length_entry.insert(tk.END, "16")

uppercase_var = tk.BooleanVar(value=True)
uppercase_checkbtn = tk.Checkbutton(options_frame, text="Include Uppercase", variable=uppercase_var)
uppercase_checkbtn.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

lowercase_var = tk.BooleanVar(value=True)
lowercase_checkbtn = tk.Checkbutton(options_frame, text="Include Lowercase", variable=lowercase_var)
lowercase_checkbtn.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

numbers_var = tk.BooleanVar(value=True)
numbers_checkbtn = tk.Checkbutton(options_frame, text="Include Numbers", variable=numbers_var)
numbers_checkbtn.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

symbols_var = tk.BooleanVar(value=True)
symbols_checkbtn = tk.Checkbutton(options_frame, text="Include Symbols", variable=symbols_var)
symbols_checkbtn.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

window.mainloop()
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

password = generate_password(get_password_len, get_uppercase_include, get_lowercase_include, get_numbers_include,
                             get_symbols_include)
print(password)
