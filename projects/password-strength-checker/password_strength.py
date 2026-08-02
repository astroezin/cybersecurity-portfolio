#!/usr/bin/env python3

import argparse
import re


def evaluate_password(password):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 1
    else:
        feedback.append("Use at least 12 characters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if re.search(r"[!@#$%^&*()_\-+=\[\]{};:'\",.<>?/\\|`~]", password):
        score += 1
    else:
        feedback.append("Add special characters.")

    ratings = {
        5: "Very Strong",
        4: "Strong",
        3: "Moderate",
        2: "Weak",
        1: "Very Weak",
        0: "Very Weak",
    }

    print("=" * 50)
    print("Password Strength Analysis")
    print("=" * 50)
    print(f"Score    : {score}/5")
    print(f"Strength : {ratings[score]}")

    if feedback:
        print("\nRecommendations:")
        for item in feedback:
            print(f"- {item}")
    else:
        print("\nExcellent! Your password meets all basic strength criteria.")


def main():
    parser = argparse.ArgumentParser(
        description="Password Strength Checker"
    )

    parser.add_argument(
        "password",
        help="Password to evaluate"
    )

    args = parser.parse_args()

    evaluate_password(args.password)


if __name__ == "__main__":
    main()
