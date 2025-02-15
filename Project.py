import tkinter as tk
from tkinter import messagebox

def check_password_strength():
    password = password_entry.get()
    length = len(password)

    if length < 6:
        strength_label.config(text="Weak", fg="red")

    elif 6 <= length <= 10:
        strength_label.config(text="Moderate", fg="orange")

    else:
        strength_label.config(text="Strong", fg="green")

# Create main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("300x200")

# Create label and entry field
tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=5)
password_entry = tk.Entry(root, show="*", font=("Arial", 12))
password_entry.pack(pady=5)

# Create button to check password strength
check_button = tk.Button(root, text="Check Strength", command=check_password_strength, font=("Arial", 12))
check_button.pack(pady=10)

# Label to display password strength
strength_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
strength_label.pack()

# Run the application
root.mainloop()

# ACTIVITY DOES NOT WORK ON VSC. GO TO REPLIT > TKINTER TO RUN.