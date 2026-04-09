import tkinter as tk
from tkinter import messagebox
import random
import string

# -------------------------------
# Password Strength Checker
# -------------------------------
def check_strength(password):
    strength = 0

    if any(c.islower() for c in password):
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c in string.punctuation for c in password):
        strength += 1
    if len(password) >= 12:
        strength += 1

    if strength <= 2:
        return "Weak", "red"
    elif strength == 3 or strength == 4:
        return "Medium", "orange"
    else:
        return "Strong", "green"

# -------------------------------
# Generate Password
# -------------------------------
def generate_password():
    length = length_slider.get()
    characters = ""

    if var_letters.get():
        characters += string.ascii_letters
    if var_numbers.get():
        characters += string.digits
    if var_symbols.get():
        characters += string.punctuation

    if characters == "":
        messagebox.showwarning("Warning", "Select at least one option!")
        return

    password = "".join(random.choice(characters) for _ in range(length))

    # Display password
    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)

    # Show strength
    strength_text, color = check_strength(password)
    strength_label.config(text=f"Strength: {strength_text}", fg=color)

# -------------------------------
# Copy Function
# -------------------------------
def copy_password():
    password = result_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        status_label.config(text="Copied to clipboard ✅", fg="#00c896")

# -------------------------------
# Main Window
# -------------------------------
root = tk.Tk()
root.title("Password Generator Pro")
root.geometry("450x500")
root.config(bg="#1e1e2f")

# -------------------------------
# Title
# -------------------------------
title = tk.Label(root, text="🔐 Password Generator",
                 font=("Helvetica", 20, "bold"),
                 bg="#1e1e2f", fg="white")
title.pack(pady=15)

# -------------------------------
# Card Frame
# -------------------------------
frame = tk.Frame(root, bg="#2c2c3e", padx=20, pady=20)
frame.pack(pady=10, padx=20, fill="both")

# -------------------------------
# Length Slider
# -------------------------------
tk.Label(frame, text="Password Length",
         bg="#2c2c3e", fg="white").pack(anchor="w")

length_slider = tk.Scale(frame, from_=4, to=32,
                         orient="horizontal",
                         bg="#2c2c3e", fg="white",
                         highlightthickness=0)
length_slider.set(10)
length_slider.pack(fill="x", pady=5)

# -------------------------------
# Options
# -------------------------------
var_letters = tk.IntVar(value=1)
var_numbers = tk.IntVar(value=1)
var_symbols = tk.IntVar()

tk.Checkbutton(frame, text="Include Letters",
               variable=var_letters,
               bg="#2c2c3e", fg="white",
               selectcolor="#444").pack(anchor="w")

tk.Checkbutton(frame, text="Include Numbers",
               variable=var_numbers,
               bg="#2c2c3e", fg="white",
               selectcolor="#444").pack(anchor="w")

tk.Checkbutton(frame, text="Include Symbols",
               variable=var_symbols,
               bg="#2c2c3e", fg="white",
               selectcolor="#444").pack(anchor="w")

# -------------------------------
# Generate Button
# -------------------------------
generate_btn = tk.Button(root, text="Generate Password",
                         command=generate_password,
                         bg="#6c63ff", fg="white",
                         font=("Arial", 12, "bold"),
                         padx=10, pady=8)
generate_btn.pack(pady=15)

# -------------------------------
# Result Entry
# -------------------------------
result_entry = tk.Entry(root,
                        font=("Arial", 14),
                        justify="center",
                        bd=0,
                        bg="#3b3b5c",
                        fg="white")
result_entry.pack(pady=10, ipadx=10, ipady=8)

# -------------------------------
# Strength Label
# -------------------------------
strength_label = tk.Label(root,
                          text="Strength: -",
                          bg="#1e1e2f",
                          fg="white",
                          font=("Arial", 11))
strength_label.pack()

# -------------------------------
# Copy Button
# -------------------------------
copy_btn = tk.Button(root, text="Copy Password",
                     command=copy_password,
                     bg="#00c896", fg="white",
                     font=("Arial", 11, "bold"))
copy_btn.pack(pady=10)

# -------------------------------
# Status Label
# -------------------------------
status_label = tk.Label(root,
                         text="",
                         bg="#1e1e2f",
                         fg="gray",
                         font=("Arial", 10))
status_label.pack()

# -------------------------------
# Run App
# -------------------------------
root.mainloop()