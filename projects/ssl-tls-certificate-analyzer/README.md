# SSL/TLS Certificate Analyzer

A Python-based SSL/TLS Certificate Analyzer that retrieves and inspects X.509 certificates from remote HTTPS servers.

This project demonstrates how security analysts validate certificates, inspect certificate metadata, verify expiration dates, and review Subject Alternative Names (SANs).

---

## Features

- Retrieve SSL/TLS certificates from remote servers
- Display certificate subject information
- Display certificate issuer
- Display certificate serial number
- Display certificate version
- Show certificate validity period
- Calculate remaining validity in days
- Enumerate Subject Alternative Names (SANs)
- Export results to JSON
- Uses only the Python Standard Library

---

## Technologies Used

- Python 3
- ssl
- socket
- argparse
- json
- datetime
- pathlib

---

## Installation

Clone the repository.

```bash
git clone https://github.com/astroezin/cybersecurity-portfolio.git
```

Navigate to the project.

```bash
cd cybersecurity-portfolio/projects/ssl-tls-certificate-analyzer
```

No external packages are required.

---

## Usage

Analyze Google.

```bash
python3 certificate_analyzer.py -H google.com
```

Analyze GitHub.

```bash
python3 certificate_analyzer.py -H github.com
```

Analyze a custom host.

```bash
python3 certificate_analyzer.py -H example.com
```

Specify a custom port.

```bash
python3 certificate_analyzer.py -H example.com -p 8443
```

Save report.

```bash
python3 certificate_analyzer.py -H google.com -o reports/certificate_report.json
```

---

## Example Output

```
Host               : google.com
Port               : 443

Subject            : commonName=*.google.com
Issuer             : Google Trust Services
Version            : 3

Days Remaining     : 67

JSON Report Saved  : reports/certificate_report.json
```

---

## Folder Structure

```
ssl-tls-certificate-analyzer/
│
├── certificate_analyzer.py
├── README.md
├── requirements.txt
├── .gitignore
├── reports/
├── samples/
└── screenshots/
```

---

## Skills Demonstrated

- SSL/TLS Fundamentals
- X.509 Certificate Analysis
- HTTPS Security
- Python Networking
- JSON Report Generation
- Security Automation
- Certificate Expiration Monitoring

---

## Future Improvements

- Support certificate chain analysis
- Verify hostname mismatches
- Detect weak signature algorithms
- Detect weak public key sizes
- Grade certificate security
- Export HTML reports

---

## License

This project is licensed under the MIT License.
