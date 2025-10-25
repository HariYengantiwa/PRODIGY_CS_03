import re

def assess_password_strength(password):
    length_error = len(password) < 8
    uppercase_error = not re.search(r"[A-Z]", password)
    lowercase_error = not re.search(r"[a-z]", password)
    digit_error = not re.search(r"[0-9]", password)
    special_char_error = not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    score = 5 - sum([length_error, uppercase_error, lowercase_error, digit_error, special_char_error])

    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    feedback = []
    if length_error:
        feedback.append("• Password should be at least 8 characters long.")
    if uppercase_error:
        feedback.append("• Include at least one uppercase letter (A-Z).")
    if lowercase_error:
        feedback.append("• Include at least one lowercase letter (a-z).")
    if digit_error:
        feedback.append("• Include at least one number (0-9).")
    if special_char_error:
        feedback.append("• Include at least one special character (e.g. !, @, #, $).")

    return strength, feedback, score


def main():
    print("[*] Password Strength Checker [*]\n")

    while True:
        password = input("Enter your password: ")
        strength, feedback, score = assess_password_strength(password)

        print(f"\nPassword Strength: {strength}\n")

        if score >= 4:
            print("✅ Great! Your password is secure.")
            break
        else:
            print("Suggestions to improve your password:")
            for item in feedback:
                print(item)
            print("\nPlease try again.\n")


if __name__ == "__main__":
    main()


#  python "d:\vscode\task3\Password Complexity Checke.py"