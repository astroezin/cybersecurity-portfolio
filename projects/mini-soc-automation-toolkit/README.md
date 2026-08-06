# Mini SOC Automation Toolkit

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Platform](https://img.shields.io/badge/Platform-Kali%20Linux-green)
![Security](https://img.shields.io/badge/Category-SOC%20Automation-red)

## Project Description

Mini SOC Automation Toolkit is a cybersecurity automation project designed to simulate a Security Operations Center (SOC) analyst workflow.

The tool collects threat intelligence from multiple security sources, analyzes indicators of compromise (IOCs), calculates risk levels, and generates professional security reports.

The project demonstrates how SOC analysts automate repetitive investigation tasks using Python.

Supported IOC types:

- IPv4 addresses
- Domains
- File hashes (MD5, SHA1, SHA256)

---

# Features

## IOC Validation

Automatically identifies and validates:

- IPv4 addresses
- Domains
- URLs
- File hashes

---

## Threat Intelligence Integration

### VirusTotal

Collects:

- Malicious detection count
- Suspicious detection count
- Harmless engines
- Undetected engines

---

### AbuseIPDB

Collects:

- Abuse confidence score
- ISP information
- Country
- Domain
- Historical reports

---

## Risk Correlation Engine

Combines multiple intelligence sources and calculates a security risk rating.

Risk levels:

| Score | Risk |
|---|---|
| 80+ | Critical |
| 50-79 | High |
| 25-49 | Medium |
| 1-24 | Low |
| 0 | Informational |

---

## SOC Reporting

Generates:

### Terminal Report

Real-time analyst-friendly output.

### JSON Report

Useful for:

- Automation
- SIEM ingestion
- Further processing

### Markdown Report

Useful for:

- Investigation notes
- Documentation
- Incident reports

---

## Logging System

Maintains an audit trail of:

- Tool execution
- IOC analysis
- Processing events
- Errors

---

# Technologies Used

- Python 3
- Kali Linux
- REST APIs
- VirusTotal API
- AbuseIPDB API
- argparse
- requests
- python-dotenv
- JSON
- Markdown reporting

---

# Installation

Clone repository:

```bash
git clone https://github.com/astroezin/cybersecurity-portfolio.git
```

Navigate to project:

```bash
cd cybersecurity-portfolio/projects/mini-soc-automation-toolkit
```

Create virtual environment:

```bash
python3 -m venv venv
```

Activate:

Linux/Kali:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# API Configuration

Create environment file:

```bash
cp .env.example .env
```

Edit:

```bash
nano .env
```

Add your API keys:

```env
VIRUSTOTAL_API_KEY=your_key_here
ABUSEIPDB_API_KEY=your_key_here
```

Never upload `.env` to GitHub.

---

# Usage

## Analyze an IP address

```bash
python soc_toolkit.py 8.8.8.8
```

Example:

```
==================================================
SOC Analysis Report
==================================================

IOC      : 8.8.8.8
Type     : IPv4

Risk     : INFORMATIONAL
Score    : 0

Threat Intelligence
------------------------------
VirusTotal Malicious : 0
VirusTotal Suspicious: 0
Abuse Score          : 0%

Risk Factors
------------------------------
- No threat indicators detected

==================================================
```

---

## Generate JSON and Markdown Reports

```bash
python soc_toolkit.py 8.8.8.8 --json --markdown
```

Output:

```
JSON:
reports/soc_report_20260806_XXXXXX.json

Markdown:
reports/soc_report_20260806_XXXXXX.md
```

---

# Project Structure

```
mini-soc-automation-toolkit/

├── api/
│   ├── abuseipdb.py
│   ├── virustotal.py
│   └── __init__.py
│
├── core/
│   ├── config.py
│   ├── correlator.py
│   ├── formatter.py
│   ├── logger.py
│   ├── report.py
│   └── validator.py
│
├── logs/
│   └── .gitkeep
│
├── reports/
│   └── .gitkeep
│
├── samples/
│   └── sample_iocs.txt
│
├── screenshots/
│
├── requirements.txt
├── soc_toolkit.py
├── README.md
└── LICENSE
```

---

# Skills Demonstrated

## Blue Team / SOC Skills

- Threat intelligence analysis
- IOC investigation
- Security automation
- Risk assessment
- Incident response workflow

## Python Skills

- API integration
- CLI development
- Modular architecture
- Error handling
- JSON processing
- File management
- Logging

## Security Engineering Concepts

- IOC enrichment
- Threat scoring
- Security reporting
- Evidence preservation
- Automation workflow design

---

# Future Improvements

## Version 2

Planned improvements:

- Add VirusTotal URL scanning
- Add IP geolocation enrichment
- Add Censys/Shodan integration
- Improve risk scoring algorithm
- Add bulk IOC scanning

---

## Version 3

Advanced features:

- CSV IOC import
- Scheduled scanning
- Email alert notifications
- Database storage
- SQLite investigation history

---

## Version 4

Enterprise-style features:

- Web dashboard
- User authentication
- SIEM integration
- Threat intelligence feeds
- Automated incident tickets
- Machine learning based risk prediction

---

# License

This project is licensed under the MIT License.

---

# Disclaimer

This project is created for educational purposes and authorized security testing only.

Do not scan or investigate systems without proper permission.
