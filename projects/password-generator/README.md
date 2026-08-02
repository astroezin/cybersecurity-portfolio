# Secure Password Generator

A Python command-line tool that generates strong, cryptographically secure passwords using Python's built-in `secrets` module.

---

## Features

- Generate cryptographically secure passwords
- Custom password length
- Optional uppercase letters
- Optional digits
- Optional special characters
- Simple command-line interface using `argparse`

---

## Technologies Used

- Python 3
- secrets
- string
- argparse

---

## Installation

### Clone the repository

```bash
git clone https://github.com/astroezin/cybersecurity-portfolio.git
```

### Navigate to the project

```bash
cd cybersecurity-portfolio/projects/password-generator
```

No external dependencies are required.

---

## Usage

Generate a default password

```bash
python3 password_generator.py
```

Generate a 24-character password

```bash
python3 password_generator.py --length 24
```

Generate a password without symbols

```bash
python3 password_generator.py --no-symbols
```

Generate a password without uppercase letters or digits

```bash
python3 password_generator.py --no-uppercase --no-digits
```

---

## Example Output

```text
Generated Password

Pi8QJS#=!]3cPq42
```

---

## Project Structure

```text
password-generator/
│
├── password_generator.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Skills Demonstrated

- Python Programming
- Cryptographically Secure Randomness
- Password Security
- Command-Line Interface Development
- argparse
- Python Standard Library

---

## Interview Questions

### Why use the `secrets` module instead of `random`?

The `secrets` module is designed for cryptographic use cases such as passwords, tokens, and API keys. The `random` module is intended for simulations and is not considered secure for generating sensitive values.

### What makes a strong password?

A strong password is long, unique, and includes a mix of uppercase letters, lowercase letters, numbers, and special characters.

### Why is password length important?

Longer passwords increase the number of possible combinations, making brute-force attacks significantly more difficult.

### What is entropy?

Entropy is a measure of unpredictability. Higher-entropy passwords are harder to guess or crack.

---

## Future Improvements

- Copy password to clipboard
- Generate multiple passwords at once
- Exclude ambiguous characters
- Save generated passwords to an encrypted file
- Estimate password entropy
- Generate passphrases (Diceware style)
- Add a graphical user interface (GUI)

---

## Disclaimer

This project is intended for educational purposes and authorized security research only.
