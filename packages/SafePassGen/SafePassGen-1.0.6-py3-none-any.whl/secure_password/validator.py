import re


class PasswordStrengthChecker:
    def __init__(self, common_passwords=None, min_length=10, dictionary_words=None):
        # Load common passwords and dictionary words if provided
        self.common_passwords = common_passwords or self.load_common_passwords()
        self.dictionary_words = dictionary_words or self.load_dictionary_words()
        self.min_length = min_length

    @staticmethod
    def load_common_passwords():
        try:
            with open("common_passwords.txt", "r") as file:
                return [line.strip().lower() for line in file]
        except FileNotFoundError:
            return []

    @staticmethod
    def load_dictionary_words():
        try:
            with open("dictionary_words.txt", "r") as file:
                return [line.strip().lower() for line in file]
        except FileNotFoundError:
            return []

    def check_strength(self, password):
        score = 0
        suggestions = []

        # Length check
        if len(password) >= self.min_length:
            score += 2
        else:
            suggestions.append(
                f"Password should be at least {self.min_length} characters long."
            )

        # Character variety checks
        if re.search(r"[a-z]", password):
            score += 1
        else:
            suggestions.append("Add lowercase letters to improve strength.")

        if re.search(r"[A-Z]", password):
            score += 1
        else:
            suggestions.append("Add uppercase letters to improve strength.")

        if re.search(r"[0-9]", password):
            score += 1
        else:
            suggestions.append("Add digits to improve strength.")

        if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            score += 1
        else:
            suggestions.append("Add special characters to improve strength.")

        # Check against common passwords (case insensitive)
        if password.lower() in self.common_passwords:
            score = 0  # Immediate fail
            suggestions.append("This password is too common and easily guessable.")

        # Check for dictionary words
        for word in self.dictionary_words:
            if word in password.lower():
                suggestions.append("Avoid using common dictionary words or names.")
                break

        # Final evaluation
        if score < 3:
            strength = "Weak"
        elif score < 5:
            strength = "Moderate"
        else:
            strength = "Strong"

        return {"strength": strength, "score": score, "suggestions": suggestions}
