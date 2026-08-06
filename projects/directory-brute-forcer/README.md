# Directory Brute Forcer

A Python-based directory brute forcing tool that discovers hidden files and directories on web servers by testing paths from a wordlist. The project is built using only Python's standard library and demonstrates core web enumeration techniques used during authorized penetration testing and security assessments.

> **Disclaimer:** This tool is intended for educational purposes and authorized security testing only. Never scan systems without explicit permission.

---

# Features

* Multi-threaded directory scanning
* Custom target URL
* Custom wordlist support
* Configurable timeout
* Configurable number of threads
* Custom User-Agent
* HTTP status code detection
* JSON report generation
* Clean command-line interface
* Uses only Python Standard Library

---

# Technologies Used

* Python 3
* argparse
* urllib
* concurrent.futures
* pathlib
* json
* datetime

---

# Installation

Clone the repository:

```bash
git clone https://github.com/astroezin/cybersecurity-portfolio.git

cd cybersecurity-portfolio/projects/directory-brute-forcer
```

No external dependencies are required.

---

# Usage

Display help:

```bash
python3 brute_forcer.py --help
```

Scan a website:

```bash
python3 brute_forcer.py \
-u https://example.com \
-w wordlists/common.txt
```

Specify thread count:

```bash
python3 brute_forcer.py \
-u https://example.com \
-w wordlists/common.txt \
-T 20
```

Save report:

```bash
python3 brute_forcer.py \
-u https://example.com \
-w wordlists/common.txt \
-o reports/scan_results.json
```

---

# Example Output

```text
============================================================
Directory Brute Forcer
============================================================
Target   : https://example.com
Wordlist : wordlists/common.txt
Entries  : 20
Threads  : 20
============================================================
[200] https://example.com/login
[403] https://example.com/uploads
[200] https://example.com/robots.txt

============================================================
Scan Summary
============================================================
Total Requests      : 20
Interesting Results : 3
JSON Report         : reports/scan_results.json
```

---

# Folder Structure

```text
directory-brute-forcer/
│
├── brute_forcer.py
├── README.md
├── requirements.txt
├── .gitignore
├── reports/
│   └── scan_results.json
├── screenshots/
├── samples/
└── wordlists/
    └── common.txt
```

---

# Skills Demonstrated

* Web Enumeration
* HTTP Protocol
* Multi-threading
* Security Automation
* Python Networking
* JSON Reporting
* Command-Line Tool Development
* Error Handling

---

# Future Improvements

* Recursive directory discovery
* Extension fuzzing
* Custom status-code filtering
* Response size filtering
* HTML and CSV reports
* Progress bar
* Request rate limiting
* Resume interrupted scans

---

# Screenshots

Add the following screenshots:

* Help menu
* Successful scan
* Generated JSON report

---

# License

This project is licensed under the MIT License.
