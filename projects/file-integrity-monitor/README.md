# File Integrity Monitor (FIM)

A Python-based File Integrity Monitoring (FIM) tool that detects file modifications, newly created files, and deleted files by comparing SHA-256 hashes against a trusted baseline.

---

## Features

- Create a trusted baseline of file hashes
- Detect modified files
- Detect newly created files
- Detect deleted files
- Recursive directory scanning
- SHA-256 hashing
- JSON baseline storage
- Simple command-line interface

---

## Technologies Used

- Python 3
- hashlib
- json
- os
- argparse

---

## Installation

### Clone the repository

```bash
git clone https://github.com/astroezin/cybersecurity-portfolio.git
```

### Navigate to the project

```bash
cd cybersecurity-portfolio/projects/file-integrity-monitor
```

No external dependencies are required.

---

## Usage

Create a baseline

```bash
python3 fim.py baseline test_folder
```

Check file integrity

```bash
python3 fim.py check test_folder
```

---

## Example Output

```text
Checking integrity...

[MODIFIED] test_folder/file1.txt
[NEW] test_folder/file3.txt
[DELETED] test_folder/file2.txt

Done.
```

---

## Project Structure

```text
file-integrity-monitor/
│
├── fim.py
├── README.md
├── requirements.txt
├── .gitignore
├── baseline.json
└── test_folder/
```

---

## Skills Demonstrated

- File Integrity Monitoring (FIM)
- SHA-256 Hashing
- Blue Team Security
- Python File Handling
- JSON Data Storage
- Recursive Directory Traversal
- Change Detection

---

## Interview Questions

### What is File Integrity Monitoring?

File Integrity Monitoring (FIM) is the process of detecting unauthorized changes to files by comparing their current state with a trusted baseline.

### Why use SHA-256?

SHA-256 produces a unique cryptographic hash for file contents. Even a one-byte change results in a completely different hash.

### Why is File Integrity Monitoring important?

It helps detect unauthorized modifications, malware infections, accidental changes, and insider threats.

### What is a baseline?

A baseline is a trusted snapshot of files and their hashes that future scans compare against.

---

## Future Improvements

- SHA-512 support
- MD5 support (for compatibility only)
- CSV report export
- JSON report export
- Colorized output
- Ignore specific file types
- Ignore directories
- Logging
- Email alerts
- Real-time monitoring
- Automatic scheduled scans

---

## Disclaimer

This project is intended for educational purposes and authorized security monitoring only.
