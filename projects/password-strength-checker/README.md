# Password Strength Checker

A Python command-line tool that evaluates password strength based on common cybersecurity best practices.

---

## Features

- Analyze password strength
- Score passwords from 0 to 5
- Classify passwords from Very Weak to Very Strong
- Check for:
  - Minimum length
  - Lowercase letters
  - Uppercase letters
  - Numbers
  - Special characters
- Provide recommendations for stronger passwords

---

## Technologies Used

- Python 3
- argparse
- re (Regular Expressions)

---

## Installation

### Clone the repository

```bash
git clone https://github.com/astroezin/cybersecurity-portfolio.git
```

### Navigate to the project

```bash
cd cybersecurity-portfolio/projects/password-strength-checker
```

No external dependencies are required.

---

## Usage

Weak password

```bash
python3 password_strength.py password
```

Medium password

```bash
python3 password_strength.py MyPassword123
```

Strong password

```bash
python3 password_strength.py P@ssw0rd123456!
```

---

## Example Output

```text
==================================================
Password Strength Analysis
==================================================

Score : 5/5

Strength : Very Strong

Excellent! Your password meets all basic strength criteria.
```

---

## Project Structure

```text
password-strength-checker/
│
├── password_strength.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Skills Demonstrated

- Python Programming
- Regular Expressions
- Password Security
- CLI Development
- Input Validation
- Security Best Practices

---

## Interview Questions

### What makes a password strong?

A strong password is long, unique, and contains a combination of uppercase letters, lowercase letters, numbers, and special characters.

### Why are regular expressions useful?

Regular expressions allow efficient pattern matching, making them ideal for validating password complexity.

### Is password complexity more important than length?

Both matter, but increasing password length generally provides a larger improvement in resistance to brute-force attacks than complexity alone.

### Should users reuse passwords?

No. Each account should have a unique password to reduce the impact of credential leaks.

---

## Future Improvements

- Estimate password entropy
- Detect common dictionary words
- Check against known breached password databases
- Export analysis reports
- Add colorized terminal output
- Create a GUI version

---

## Disclaimer

This project is intended for educational purposes and promoting good password security practices.
