# URL Reputation Checker

A Python-based cybersecurity tool that performs basic URL reputation analysis using heuristic checks. It analyzes a URL for potentially suspicious characteristics, resolves its IP address, calculates a simple risk score, and generates a JSON report.

---

## Features

- URL parsing and validation
- Hostname extraction
- DNS resolution
- Detects IP-based URLs
- Detects suspicious top-level domains (TLDs)
- Detects common URL shortening services
- Detects excessively long URLs
- Checks HTTPS usage
- Calculates a heuristic risk score
- Assigns a risk level (Low, Medium, High)
- Generates JSON reports
- Command-line interface using argparse

---

## Technologies Used

- Python 3
- argparse
- socket
- urllib.parse
- ipaddress
- json
- pathlib

---

## Project Structure

```
url-reputation-checker/
│
├── url_checker.py
├── README.md
├── requirements.txt
├── .gitignore
├── reports/
│   └── url_report.json
├── screenshots/
└── samples/
```

---

## Installation

Clone the repository.

```bash
git clone https://github.com/astroezin/cybersecurity-portfolio.git

cd cybersecurity-portfolio/projects/url-reputation-checker
```

No external packages are required.

---

## Usage

Display help:

```bash
python3 url_checker.py --help
```

Analyze a URL:

```bash
python3 url_checker.py -u https://google.com
```

Specify a custom output file:

```bash
python3 url_checker.py \
-u https://github.com \
-o reports/github_report.json
```

---

## Example Output

```
============================================================
URL Reputation Checker
============================================================
URL              : https://google.com
Hostname         : google.com
Scheme           : https
HTTPS            : True
IP Address       : 142.251.xx.xx

Security Checks
------------------------------------------------------------
Suspicious TLD   : False
IP URL           : False
URL Shortener    : False
Long URL         : False

Risk Score       : 0/100
Risk Level       : Low
```

---

## Skills Demonstrated

- URL parsing
- DNS lookups
- Cybersecurity heuristics
- Risk scoring
- JSON reporting
- CLI development
- Error handling
- Python standard library usage

---

## Future Improvements

- VirusTotal API integration
- Google Safe Browsing API
- WHOIS lookup
- Domain age analysis
- SSL certificate inspection
- Redirect chain analysis
- HTML phishing detection
- Bulk URL scanning
- CSV report export

---

## License

This project is provided for educational and defensive cybersecurity purposes only.
