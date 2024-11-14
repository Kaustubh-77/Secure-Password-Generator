import tkinter as tk
from tkinter import messagebox
import random

# Characters for password generation
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    try:
        
        nr_letters = int(entry_letters.get())
        nr_symbols = int(entry_symbols.get())
        nr_numbers = int(entry_numbers.get())
        
        order_choice = order_var.get()
        
        if order_choice == "Ordered":
            password = ''.join(random.choice(letters) for _ in range(nr_letters))
            password += ''.join(random.choice(symbols) for _ in range(nr_symbols))
            password += ''.join(random.choice(numbers) for _ in range(nr_numbers))
        else:
            password_list = (
                [random.choice(letters) for _ in range(nr_letters)] +[random.choice(symbols) for _ in range(nr_symbols)] +[random.choice(numbers) for _ in range(nr_numbers)]
            )
            random.shuffle(password_list)
            password = ''.join(password_list)
        
        
        result.config(text=f"Here's a safe and secure password for you: {password}")
        
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for each field.")


root = tk.Tk()
root.title("Secure Password Generator")
root.geometry("400x350")


title_label = tk.Label(root, text="Secure Password Generator", font=("Times NEw Roman", 16, "bold"))
title_label.pack(pady=10)


tk.Label(root, text="Number of Letters:").pack()
entry_letters = tk.Entry(root, width=10)
entry_letters.pack()

tk.Label(root, text="Number of Symbols:").pack()
entry_symbols = tk.Entry(root, width=10)
entry_symbols.pack()

tk.Label(root, text="Number of Numbers:").pack()
entry_numbers = tk.Entry(root, width=10)
entry_numbers.pack()


order_var = tk.StringVar(value="Random")
tk.Label(root, text="Preferred Password Format:").pack()
ordered_radio = tk.Radiobutton(root, text="Ordered", variable=order_var, value="Ordered")
random_radio = tk.Radiobutton(root, text="Random", variable=order_var, value="Random")
ordered_radio.pack()
random_radio.pack()


generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=20)


result = tk.Label(root, text="", font=("Times New Roman", 12), fg="Green")
result.pack()


root.mainloop()
