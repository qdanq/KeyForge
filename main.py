import random
import string
import tkinter as tk
from tkinter import messagebox


def generate_password():
    password_len = int(length_entry.get())
    uppercase_include = uppercase_var.get()
    lowercase_include = lowercase_var.get()
    numbers_include = numbers_var.get()
    symbols_include = symbols_var.get()

    characters = ''
    if uppercase_include:
        characters += string.ascii_uppercase
    if lowercase_include:
        characters += string.ascii_lowercase
    if numbers_include:
        characters += string.digits
    if symbols_include:
        characters += string.punctuation

    if not characters:
        messagebox.showinfo("Error", "Select at least one option.")
        return

    password = ''.join(random.choice(characters) for _ in range(password_len))
    password_var.set(password)


def copy_to_clipboard():
    window.clipboard_clear()
    window.clipboard_append(password_var.get())


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

password_var = tk.StringVar()
password_label = tk.Label(window, textvariable=password_var, font=("Arial", 12), pady=10)
password_label.pack()


copy_button = tk.Button(window, text="Copy Password", command=copy_to_clipboard)
copy_button.pack(pady=5)

window.mainloop()
