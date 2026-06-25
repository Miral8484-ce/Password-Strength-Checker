# Password-Strength-Checker
# 🔐 Password Strength Checker

A simple and user-friendly Password Strength Checker built with **Python** and **Tkinter**. This application evaluates the strength of a password and provides suggestions to help users create stronger and more secure passwords.

---

## 📌 Features

- ✅ Check password strength instantly
- 🔢 Password score (0–100)
- 🔒 Detect:
  - Minimum password length
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters
- 💡 Suggestions to improve weak passwords
- 👁️ Show/Hide password
- 📋 Copy password to clipboard
- 🖥️ Easy-to-use Tkinter GUI

---

## 🛠️ Technologies Used

- Python 3
- Tkinter
- Pyperclip
- Regular Expressions (re)

---

## 📂 Project Structure

```
PasswordStrengthChecker/
│
├── app.py
├── password_checker.py
├── requirements.txt
├── README.md
└── screenshots/
```

---

## 📥 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Miral8484-ce/Password-Strength-Checker.git
```

### 2. Open the Project Folder

```bash
cd Password-Strength-Checker
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run the Application

Run the following command in the terminal:

```bash
python app.py
```

The Password Strength Checker window will open.

---

## 🚀 How to Use

1. Launch the application.
2. Enter a password in the input field.
3. Click **Check Password Strength**.
4. View:
   - Password Score
   - Password Strength
   - Suggestions for improvement
5. Use the **Show** button to view the password.
6. Use the **Copy** button to copy the password to the clipboard.

---

## 📊 Password Strength Levels

| Score | Strength |
|--------|----------|
| 0–29 | 🚨 Very Weak |
| 30–49 | ❌ Weak |
| 50–69 | ⚠️ Medium |
| 70–89 | ✅ Strong |
| 90–100 | 💪 Very Strong |

---

## 📸 Screenshots

Create a folder named **screenshots** and add application screenshots.

Example:

```
screenshots/
├── home.png
├── password_check.png
└── result.png
```

---

## 📦 Requirements

```
pyperclip
```

Install manually if needed:

```bash
pip install pyperclip
```

---

## 👨‍💻 Author

**Miral Patel**

GitHub: https://github.com/Miral8484-ce

---

## 📄 License

This project is developed for educational purposes and learning Python GUI development.
