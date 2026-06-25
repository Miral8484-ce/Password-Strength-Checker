import re


def check_password_strength(password):

    score = 0
    feedback = []

    # Length
    if len(password) >= 12:
        score += 25
    elif len(password) >= 8:
        score += 15
    else:
        feedback.append("Password should be at least 8 characters.")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 15
    else:
        feedback.append("Add uppercase letters.")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 15
    else:
        feedback.append("Add lowercase letters.")

    # Numbers
    if re.search(r"\d", password):
        score += 20
    else:
        feedback.append("Add numbers.")

    # Special Characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 25
    else:
        feedback.append("Add special characters.")

    if score >= 90:
        strength = "Very Strong 💪"

    elif score >= 70:
        strength = "Strong ✅"

    elif score >= 50:
        strength = "Medium ⚠️"

    elif score >= 30:
        strength = "Weak ❌"

    else:
        strength = "Very Weak 🚨"

    return score, strength, feedback