import unittest
from secure_password.generator import PasswordGenerator


class TestPasswordGenerator(unittest.TestCase):

    def test_password_length(self):
        generator = PasswordGenerator(length=16, quantity=10)
        passwords = generator.generate_passwords()
        for pwd in passwords:
            self.assertEqual(len(pwd), 16)

    def test_include_numbers(self):
        generator = PasswordGenerator(
            length=10,
            include_numbers=True,
            include_lowercase=True,
            include_uppercase=False,
            include_symbols=False,
        )
        pwd = generator.generate_passwords()

        has_digit = any(char.isdigit() for char in pwd)
        has_lowercase = any(char.islower() for char in pwd)
        self.assertTrue(has_digit, f"Password does not contain a digit: {pwd}")
        self.assertTrue(
            has_lowercase, f"Password does not contain a lowercase letter: {pwd}"
        )

    def test_no_duplicates(self):
        generator = PasswordGenerator(length=20, no_duplicates=True)
        passwords = generator.generate_passwords()
        for pwd in passwords:
            self.assertEqual(len(pwd), len(set(pwd)))

    def test_begin_with_letter(self):
        generator = PasswordGenerator(length=10, begin_with_letter=True)
        password = generator.generate_passwords()
        self.assertTrue(password[0].isalpha())

    def test_generate_multiple_passwords(self):
        generator = PasswordGenerator(length=8, quantity=5)
        passwords = generator.generate_passwords()
        self.assertEqual(len(passwords), 5)
        for pwd in passwords:
            self.assertEqual(len(pwd), 8)

    def test_does_not_start_with_letter(self):
        generator = PasswordGenerator(
            length=10,
            include_numbers=True,
            include_lowercase=True,
            include_uppercase=True,
            include_symbols=True,
            begin_with_letter=False,
        )
        passwords = generator.generate_passwords()

        for pwd in passwords:
            # The first character should be in the allowed pool, no restriction to letters
            self.assertIn(
                pwd[0],
                generator._generate_characters_pool(),
                f"First character '{pwd[0]}' is not in the pool",
            )

    def test_only_numbers(self):
        generator = PasswordGenerator(length=10, only_numbers=True)
        passwords = generator.generate_passwords()

        for pwd in passwords:
            self.assertTrue(
                all(char.isdigit() for char in pwd),
                f"Password contains non-digit characters: {pwd}",
            )


if __name__ == "__main__":
    unittest.main()
