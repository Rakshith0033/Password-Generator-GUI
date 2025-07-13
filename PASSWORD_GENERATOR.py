import tkinter as tk
from tkinter import messagebox
import random
import string

# 🔐 Password generator logic
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text=f"Password:\n{password}")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid positive number.")

# 🖼 GUI setup
app = tk.Tk()
app.title("Password Generator")
app.geometry("350x300")
app.configure(bg="black")

# Title
tk.Label(app, text="🔐 Password Generator", font=("Arial", 16, "bold"), bg="black", fg="white").pack(pady=10)

# Length input
tk.Label(app, text="Enter password length:", font=("Arial", 12), bg="black", fg="white").pack()
length_entry = tk.Entry(app, font=("Arial", 12), bg="black", fg="white", insertbackground="white")
length_entry.pack(pady=10)

# Generate button
tk.Button(app, text="Generate Password", font=("Arial", 12), bg="white", fg="black", command=generate_password).pack(pady=10)

# Result display
result_label = tk.Label(app, text="Password:\n", font=("Courier", 12), bg="black", fg="white", wraplength=320, justify="center")
result_label.pack(pady=20)

# Run the app
app.mainloop()
