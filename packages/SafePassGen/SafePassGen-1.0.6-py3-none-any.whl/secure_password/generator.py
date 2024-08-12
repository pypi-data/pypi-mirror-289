import random
import string
from typing import Union, List


class PasswordGenerator:
    def __init__(
        self,
        length=12,
        include_numbers=True,
        include_lowercase=True,
        include_uppercase=True,
        include_symbols=True,
        no_duplicates=True,
        begin_with_letter=True,
        only_numbers=False,
        quantity=1,
    ):
        if length < 6:
            raise ValueError("Password length must be at least 6.")

        self.length = length
        self.include_numbers = include_numbers
        self.include_lowercase = include_lowercase
        self.include_uppercase = include_uppercase
        self.include_symbols = include_symbols
        self.no_duplicates = no_duplicates
        self.begin_with_letter = begin_with_letter
        self.only_numbers = only_numbers
        self.quantity = quantity
        self.characters_pool = self._generate_characters_pool()

        if self.no_duplicates and len(self.characters_pool) < self.length:
            raise ValueError(
                "Character pool too small to generate a unique password of the specified length."
            )

    def _generate_characters_pool(self):
        characters = ""
        if self.only_numbers:
            characters = string.digits
        else:
            if self.include_numbers:
                characters += string.digits
            if self.include_lowercase:
                characters += string.ascii_lowercase
            if self.include_uppercase:
                characters += string.ascii_uppercase
            if self.include_symbols:
                characters += "!#$%()*+,-./:;<=>?@[]^_{|}~"

        if not characters:
            raise ValueError("Character pool is empty. Adjust the settings.")

        return characters

    def _generate_password(self):
        password = []

        # Ensure the password starts with a letter if required
        if self.begin_with_letter and not self.only_numbers:
            first_char = random.choice(string.ascii_letters)
            password.append(first_char)

        while len(password) < self.length:
            char = random.choice(self.characters_pool)
            if self.no_duplicates and char in password:
                continue
            password.append(char)

        # Ensure password contains at least one digit if include_numbers is True
        if self.include_numbers and not any(char.isdigit() for char in password):
            digit_char = random.choice(string.digits)
            replace_index = random.randint(
                1 if self.begin_with_letter else 0, self.length - 1
            )
            password[replace_index] = digit_char

        # Ensure the password has the correct length
        if len(password) != self.length:
            password = password[: self.length]

        return "".join(password)

    def generate_passwords(self) -> Union[str, List[str]]:
        passwords = set()
        while len(passwords) < self.quantity:
            new_password = self._generate_password()
            passwords.add(new_password)

        if self.quantity == 1:
            return list(passwords)[0]
        return list(passwords)
