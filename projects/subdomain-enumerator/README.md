# Advanced Subdomain Enumerator

A Python-based subdomain enumeration tool that discovers subdomains by performing DNS lookups against a target domain.

This project was built to improve my understanding of DNS, socket programming, multithreading, and Python automation for cybersecurity.

---

## Features

- DNS-based subdomain discovery
- Custom wordlist support
- Command-line interface using `argparse`
- IPv4 address resolution
- Scan summary with execution time
- Clean and modular Python code
- Easy to extend with multithreading and export features

---

## Technologies Used

- Python 3
- socket
- argparse

---

## Installation

Clone the repository:

```bash
git clone https://github.com/astroezin/cybersecurity-portfolio.git
```

Navigate to the project:

```bash
cd cybersecurity-portfolio/projects/subdomain-enumerator
```

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Basic scan:

```bash
python3 subenum.py google.com
```

Use a custom wordlist:

```bash
python3 subenum.py example.com --wordlist wordlist.txt
```

---

## Example Output

```text
=======================================================
Simple Subdomain Enumerator
=======================================================
Target : google.com

[FOUND] www.google.com        142.251.xxx.xxx
[FOUND] mail.google.com       142.250.xxx.xxx
[FOUND] docs.google.com       142.251.xxx.xxx

=======================================================
Scan Summary
=======================================================
Subdomains Tested : 38
Found             : 3
Time              : 0.42 seconds
```

---

## Project Structure

```text
subdomain-enumerator/
├── subenum.py
├── README.md
├── requirements.txt
├── wordlist.txt
├── .gitignore
├── output/
└── screenshots/
```

---

## Skills Demonstrated

- Python programming
- DNS resolution
- Socket programming
- Command-line application development
- File handling
- Error handling
- Cybersecurity automation

---

## Future Improvements

- Multithreaded scanning
- Colored terminal output
- TXT and CSV export
- Wildcard DNS detection
- Progress indicator
- IPv6 support
- Passive subdomain enumeration
- JSON export
- Logging support

---

## License

This project is licensed under the MIT License.
