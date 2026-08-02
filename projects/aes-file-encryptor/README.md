# AES File Encryptor

A Python command-line tool that securely encrypts and decrypts files using **AES-256-GCM**.

This project demonstrates practical cryptography concepts including authenticated encryption, password-based key derivation, and secure file handling.

---

## Features

- AES-256-GCM encryption
- AES-256-GCM decryption
- Password-protected encryption
- PBKDF2 key derivation
- Random salt generation
- Random nonce generation
- SHA-256 checksum
- Command-line interface using argparse
- Error handling

---

## Technologies Used

- Python 3
- PyCryptodome
- hashlib
- argparse

---

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## Usage

Encrypt a file:

```bash
python encryptor.py encrypt samples/secret.txt
```

Decrypt a file:

```bash
python encryptor.py decrypt samples/secret.txt.enc
```

---

## Example Output

```text
=======================================================
Encryption Complete
=======================================================
Output : samples/secret.txt.enc
SHA256 : 7d1a4b...
```

---

## Project Structure

```text
aes-file-encryptor/
├── encryptor.py
├── README.md
├── requirements.txt
├── .gitignore
├── samples/
└── screenshots/
```

---

## Skills Demonstrated

- AES-256-GCM
- Authenticated encryption
- PBKDF2 key derivation
- SHA-256 hashing
- Python file handling
- Secure password input
- CLI application development

---

## Future Improvements

- Progress bar for large files
- Drag-and-drop support
- GUI version
- Multiple encryption algorithms
- Directory encryption
- Secure key file support
- Digital signature verification

---

## License

MIT License
