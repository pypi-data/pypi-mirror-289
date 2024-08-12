import unittest
from secure_password.validator import PasswordStrengthChecker


class TestPasswordValidator(unittest.TestCase):
    def test_password_strength_deafult_options(self):
        checker = PasswordStrengthChecker()
        
        strong_password = "A!1b2C3d$zqP"
        weak_password = "12345"
        
        strong_result = checker.check_strength(strong_password)
        weak_result = checker.check_strength(weak_password)

        self.assertEqual(strong_result["strength"], "Strong")
        self.assertEqual(weak_result["strength"], "Weak")

    def test_password_strength_common_pass(self):
        checker = PasswordStrengthChecker(common_passwords=["test123456789"])
        
        password = "Test123456789"
        result = checker.check_strength(password)

        self.assertEqual(result["strength"], "Weak")

    def test_password_strength_min_length(self):
        length = 12
        checker = PasswordStrengthChecker(min_length=length)
        
        strong_password = "A!1b2C3d$zqPJqk"
        weak_password = "A!1b2C3d$z"

        strong_result = checker.check_strength(strong_password)
        weak_result = checker.check_strength(weak_password)

        self.assertEqual(strong_result["strength"], "Strong")
        self.assertEqual(weak_result["suggestions"][0], f"Password should be at least {length} characters long.")

    def test_password_strength_dictionary_word(self):
        dictionary_words = ["abyssobenthonic", "otherword", "anotherword"]
        checker = PasswordStrengthChecker(dictionary_words=dictionary_words)
        
        password = "Abyssobenthonic!1"
        result = checker.check_strength(password)
        
        self.assertIn("Avoid using common dictionary words or names.", result["suggestions"])
