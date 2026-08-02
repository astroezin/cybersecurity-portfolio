# WHOIS Lookup Tool

A Python-based command-line WHOIS lookup tool that retrieves domain registration information using the `python-whois` library.

---

## Features

- Lookup WHOIS information for any domain
- Display registrar details
- Show creation, expiration, and updated dates
- Display name servers
- Display domain status
- Display contact emails (if available)
- Display DNSSEC status
- Clean command-line interface using `argparse`

---

## Technologies Used

- Python 3
- python-whois
- argparse

---

## Installation

### Clone the repository

```bash
git clone https://github.com/astroezin/cybersecurity-portfolio.git
```

### Navigate to the project

```bash
cd cybersecurity-portfolio/projects/whois-lookup
```

### Create a virtual environment

```bash
python3 -m venv .venv
```

### Activate the virtual environment

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows:

```powershell
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

Basic lookup:

```bash
python whois_lookup.py google.com
```

Another example:

```bash
python whois_lookup.py github.com
```

---

## Example Output

```text
============================================================
WHOIS INFORMATION : google.com
============================================================

Domain Name      : GOOGLE.COM
Registrar        : MarkMonitor, Inc.
Creation Date    : 1997-09-15
Expiration Date  : 2028-09-14
Updated Date     : 2024-08-02
Name Servers     : NS1.GOOGLE.COM ...
Status           : clientTransferProhibited
Emails           : whoisrequest@markmonitor.com
DNSSEC           : unsigned
```

---

## Project Structure

```text
whois-lookup/
│
├── whois_lookup.py
├── README.md
├── requirements.txt
├── .gitignore
└── .venv/
```

---

## Skills Demonstrated

- Python Programming
- Domain Reconnaissance
- WHOIS Queries
- Virtual Environments
- Third-Party Python Packages
- argparse
- Error Handling

---

## Interview Questions

### What is WHOIS?

WHOIS is a protocol and database used to retrieve registration information about domain names.

### What is a domain registrar?

A registrar is a company authorized to register domain names (for example, MarkMonitor or Namecheap).

### Why do some WHOIS records hide information?

Many registrars offer privacy protection or are subject to regulations such as GDPR, which limit publicly available contact details.

### What is DNSSEC?

DNSSEC (Domain Name System Security Extensions) helps protect DNS responses from tampering by using digital signatures.

### What is the difference between DNS and WHOIS?

- DNS resolves domain names to IP addresses.
- WHOIS provides domain registration and ownership information.

---

## Future Improvements

- Export results to JSON
- Export results to CSV
- Lookup multiple domains from a file
- Colorized terminal output
- Better formatting for date fields
- Registrar statistics
- Detect domain expiration
- GUI version using Tkinter or PySide6

---

## Disclaimer

This project is intended for educational purposes and authorized security research only.
