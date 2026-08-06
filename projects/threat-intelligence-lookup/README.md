# Threat Intelligence Lookup

A professional Python-based threat intelligence lookup tool that queries multiple reputation services to investigate IPv4 addresses. The tool integrates with VirusTotal and AbuseIPDB to provide security analysts with actionable intelligence about potentially malicious IP addresses.

This project demonstrates secure API integration, IOC validation, threat intelligence enrichment, and clean command-line application design.

---

## Features

* Query VirusTotal for IPv4 reputation
* Query AbuseIPDB for abuse reports
* Automatic IOC type detection
* Human-readable security reports
* Secure API key management using `.env`
* Modular project architecture
* Command-line interface using `argparse`
* Robust error handling
* Clean and maintainable Python code

---

## Technologies Used

* Python 3
* Requests
* python-dotenv
* VirusTotal API v3
* AbuseIPDB API
* Kali Linux
* Git & GitHub

---

## Project Structure

```text
threat-intelligence-lookup/
├── api/
│   ├── abuseipdb.py
│   ├── __init__.py
│   └── virustotal.py
├── utils/
│   ├── config.py
│   ├── formatter.py
│   └── validators.py
├── screenshots/
├── samples/
├── threat_lookup.py
├── requirements.txt
├── .gitignore
├── .env.example
├── README.md
└── LICENSE
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/astroezin/cybersecurity-portfolio.git
```

Navigate to the project:

```bash
cd cybersecurity-portfolio/projects/threat-intelligence-lookup
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it:

Linux/macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file in the project directory.

Example:

```text
VIRUSTOTAL_API_KEY=your_api_key
ABUSEIPDB_API_KEY=your_api_key
```

Never commit your `.env` file to GitHub.

---

## Usage

Lookup an IPv4 address:

```bash
python threat_lookup.py 8.8.8.8
```

Example:

```text
==================================================
Threat Intelligence Lookup
==================================================
Target : 8.8.8.8

=========================================
VirusTotal IP Intelligence
=========================================

Country    : US
ASN        : 15169
Owner      : Google LLC

Malicious  : 0
Suspicious : 0
Harmless   : 53
Undetected : 38

=========================================
AbuseIPDB Intelligence
=========================================

Country    : US
ISP        : Google LLC

Abuse Score : 0%
Reports     : 175
Distinct Users : 88
```

---

## Skills Demonstrated

* Threat Intelligence
* IOC Analysis
* API Integration
* Secure Configuration Management
* Python CLI Development
* JSON Parsing
* Error Handling
* Input Validation
* Modular Software Design
* Defensive Security Fundamentals

---

## Future Improvements

### Version 2

* Support domain lookups
* Support URL lookups
* Support file hash lookups
* JSON output
* Report export
* Risk scoring
* Colored terminal output

### Version 3

* AlienVault OTX integration
* GreyNoise integration
* URLScan.io integration
* Shodan integration
* API rate-limit handling
* Local caching

### Version 4

* Multi-source threat correlation
* Interactive terminal dashboard
* HTML/PDF reporting
* Unit and integration tests
* Docker support
* CI/CD workflow

---

## License

This project is licensed under the MIT License.
