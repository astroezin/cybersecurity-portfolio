#!/usr/bin/env python3

import argparse
import secrets
import string


def generate_password(length, use_upper, use_digits, use_symbols):
    characters = string.ascii_lowercase

    if use_upper:
        characters += string.ascii_uppercase

    if use_digits:
        characters += string.digits

    if use_symbols:
        characters += "!@#$%^&*()-_=+[]{}<>?/"

    password = "".join(
        secrets.choice(characters)
        for _ in range(length)
    )

    return password


def main():
    parser = argparse.ArgumentParser(
        description="Secure Password Generator"
    )

    parser.add_argument(
        "-l",
        "--length",
        type=int,
        default=16,
        help="Password length (default: 16)"
    )

    parser.add_argument(
        "--no-uppercase",
        action="store_true",
        help="Disable uppercase letters"
    )

    parser.add_argument(
        "--no-digits",
        action="store_true",
        help="Disable digits"
    )

    parser.add_argument(
        "--no-symbols",
        action="store_true",
        help="Disable symbols"
    )

    args = parser.parse_args()

    password = generate_password(
        args.length,
        not args.no_uppercase,
        not args.no_digits,
        not args.no_symbols,
    )

    print("\nGenerated Password\n")
    print(password)


if __name__ == "__main__":
    main()
