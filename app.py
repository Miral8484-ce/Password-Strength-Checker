import tkinter as tk
from tkinter import messagebox
import pyperclip

from password_checker import check_password_strength


def check_password():

    password = password_entry.get()

    if password == "":
        messagebox.showerror(
            "Error",
            "Please Enter Password"
        )
        return

    score, strength, feedback = check_password_strength(password)

    score_label.config(
        text=f"Score : {score}/100"
    )

    strength_label.config(
        text=f"Strength : {strength}"
    )

    suggestion_text.config(state="normal")
    suggestion_text.delete("1.0", tk.END)

    if len(feedback) == 0:
        suggestion_text.insert(
            tk.END,
            "Excellent Password!"
        )
    else:
        for item in feedback:
            suggestion_text.insert(
                tk.END,
                "• " + item + "\n"
            )

    suggestion_text.config(state="disabled")


def toggle_password():

    if password_entry.cget("show") == "*":
        password_entry.config(show="")
        show_button.config(text="Hide")
    else:
        password_entry.config(show="*")
        show_button.config(text="Show")


def copy_password():

    password = password_entry.get()

    if password == "":
        return

    pyperclip.copy(password)

    messagebox.showinfo(
        "Copied",
        "Password Copied Successfully!"
    )


root = tk.Tk()

root.title("Password Strength Checker")
root.geometry("600x500")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Password Strength Checker",
    font=("Arial", 20, "bold")
)

title.pack(pady=20)

password_entry = tk.Entry(
    root,
    width=35,
    show="*",
    font=("Arial", 12)
)

password_entry.pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

show_button = tk.Button(
    button_frame,
    text="Show",
    command=toggle_password
)

show_button.grid(row=0, column=0, padx=5)

copy_button = tk.Button(
    button_frame,
    text="Copy",
    command=copy_password
)

copy_button.grid(row=0, column=1, padx=5)

check_button = tk.Button(
    root,
    text="Check Password Strength",
    command=check_password,
    width=25,
    bg="#4CAF50",
    fg="white"
)

check_button.pack(pady=10)

score_label = tk.Label(
    root,
    text="Score : ",
    font=("Arial", 14)
)

score_label.pack()

strength_label = tk.Label(
    root,
    text="Strength : ",
    font=("Arial", 14, "bold")
)

strength_label.pack(pady=5)

tk.Label(
    root,
    text="Suggestions",
    font=("Arial", 12, "bold")
).pack()

suggestion_text = tk.Text(
    root,
    width=60,
    height=10,
    state="disabled"
)

suggestion_text.pack(pady=10)

root.mainloop()