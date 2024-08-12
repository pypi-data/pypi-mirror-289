import argparse
from .generator import PasswordGenerator
from .validator import PasswordStrengthChecker


def check_password_strength(passwords):
    """Check the strength of each generated password."""
    checker = PasswordStrengthChecker()
    if isinstance(passwords, str):
        result = checker.check_strength(passwords)
        print(f"\nStrength: {result['strength']}")
        if result["suggestions"]:
            print("Suggestions:")
            for suggestion in result["suggestions"]:
                print(f"- {suggestion}")

    else:
        for i, pwd in enumerate(passwords, start=1):
            result = checker.check_strength(pwd)
            print(f"\nPassword {i} Strength: {result['strength']}")
            if result["suggestions"]:
                print("Suggestions:")
                for suggestion in result["suggestions"]:
                    print(f"- {suggestion}")


def generate_passwords(args):
    """Generate passwords based on the provided arguments."""
    # Ensure at least one character type is included
    if not (args.numbers or args.lowercase or args.uppercase or args.symbols):
        raise ValueError(
            "You must specify at least one character type (numbers, lowercase, uppercase, symbols)."
        )

    generator = PasswordGenerator(
        length=args.length,
        include_numbers=args.numbers,
        include_lowercase=args.lowercase,
        include_uppercase=args.uppercase,
        include_symbols=args.symbols,
        no_duplicates=args.no_duplicates,
        begin_with_letter=args.begin_with_letter,
        only_numbers=args.only_numbers,
        quantity=args.quantity,
    )

    return generator.generate_passwords()


def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(
        description="Password Generator and Strength Checker"
    )

    # Add arguments for password generation
    parser.add_argument(
        "--length",
        type=int,
        default=12,
        help="Length of the password(s) to be generated",
    )
    parser.add_argument(
        "--numbers", action="store_true", help="Include numbers in the password"
    )
    parser.add_argument(
        "--lowercase",
        action="store_true",
        help="Include lowercase characters in the password",
    )
    parser.add_argument(
        "--uppercase",
        action="store_true",
        help="Include uppercase characters in the password",
    )
    parser.add_argument(
        "--symbols", action="store_true", help="Include symbols in the password"
    )
    parser.add_argument(
        "--no-duplicates",
        action="store_true",
        help="Ensure no duplicate characters within the password",
    )
    parser.add_argument(
        "--begin-with-letter",
        action="store_true",
        help="Ensure the password starts with a letter",
    )
    parser.add_argument(
        "--only-numbers",
        action="store_true",
        help="Generate passwords containing only numbers",
    )
    parser.add_argument(
        "--quantity", type=int, default=1, help="Number of passwords to generate"
    )

    # Add argument for password strength checking
    parser.add_argument(
        "--check-strength",
        action="store_true",
        help="Check the strength of the generated passwords",
    )

    # Parse arguments
    args = parser.parse_args()

    # Generate passwords
    try:
        passwords = generate_passwords(args)
    except ValueError as e:
        print(e)
        return

    # Print generated passwords
    if isinstance(passwords, str):  # If a single password is returned
        print(passwords)
    else:  # If multiple passwords are returned
        for i, pwd in enumerate(passwords, start=1):
            print(f"Password {i}: {pwd}")

    # Optionally check password strength
    if args.check_strength:
        check_password_strength(passwords)


if __name__ == "__main__":
    main()
