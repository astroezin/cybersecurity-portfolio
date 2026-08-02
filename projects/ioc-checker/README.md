# IOC Checker

A Python command-line tool that checks Indicators of Compromise (IOCs) against a local threat intelligence database.

The tool supports IP addresses, domains, URLs, and SHA256 file hashes. It is designed as an offline threat intelligence utility to demonstrate blue-team and SOC automation skills.

---

## Features

- Detect malicious IP addresses
- Detect malicious domains
- Detect malicious URLs
- Detect malicious SHA256 hashes
- Automatic IOC type detection
- Offline JSON threat database
- Clean command-line interface

---

## Technologies Used

- Python 3
- argparse
- json
- ipaddress
- pathlib

---

## Installation

No external dependencies are required.

```bash
python3 ioc_checker.py evil.com
```

---

## Usage

Check an IP address:

```bash
python3 ioc_checker.py 192.168.1.100
```

Check a domain:

```bash
python3 ioc_checker.py evil.com
```

Check a URL:

```bash
python3 ioc_checker.py http://bad-domain.com/login
```

Check a SHA256 hash:

```bash
python3 ioc_checker.py e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

---

## Example Output

```text
IOC       : evil.com
Category  : DOMAIN

Status    : MALICIOUS
Threat    : Phishing Domain
Severity  : HIGH
```

---

## Project Structure

```text
ioc-checker/
├── ioc_checker.py
├── iocs.json
├── README.md
├── requirements.txt
├── screenshots/
└── samples/
```

---

## Skills Demonstrated

- Threat Intelligence
- IOC Analysis
- Blue Team Automation
- JSON Data Processing
- Python CLI Development
- Security Scripting

---

## Future Improvements

- VirusTotal API integration
- AbuseIPDB integration
- AlienVault OTX support
- CSV and JSON report export
- Bulk IOC scanning
- IOC confidence scoring
- IOC expiration dates
- Colored terminal output

---

## License

MIT License
