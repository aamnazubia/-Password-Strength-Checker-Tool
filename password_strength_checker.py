import tkinter as tk
import re

def check_strength():
    password = entry.get()
    strength_points = 0

    if len(password) >= 8:
        strength_points += 1
    if re.search(r"[A-Z]", password):
        strength_points += 1
    if re.search(r"[a-z]", password):
        strength_points += 1
    if re.search(r"\d", password):
        strength_points += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength_points += 1

    if strength_points <= 2:
        strength_label.config(text="Weak", fg="red")
    elif strength_points == 3 or strength_points == 4:
        strength_label.config(text="Moderate", fg="orange")
    else:
        strength_label.config(text="Strong", fg="green")

# Create main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("350x200")

# 🔹 Force window to stay on top
root.lift()
root.attributes('-topmost', True)
root.after_idle(root.attributes, '-topmost', False)

# Title
title_label = tk.Label(root, text="🔒 Password Strength Checker", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

# Password Entry
entry_label = tk.Label(root, text="Enter Password:", font=("Arial", 11))
entry_label.pack()
entry = tk.Entry(root, show="*", width=30, font=("Arial", 12))
entry.pack(pady=5)

# Button to check strength
check_button = tk.Button(root, text="Check Strength", command=check_strength, font=("Arial", 11, "bold"), bg="#4a90e2", fg="white", relief="raised", bd=3)
check_button.pack(pady=10)

# Label to show result
strength_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
strength_label.pack(pady=5)

# Run the GUI loop
root.mainloop()
