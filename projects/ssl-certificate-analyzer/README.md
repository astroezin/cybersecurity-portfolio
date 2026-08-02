# SSL Certificate Analyzer

A Python command-line tool that retrieves and analyzes the SSL/TLS certificate of a remote HTTPS server.

---

## Features

- Retrieve SSL/TLS certificate information
- Display TLS protocol version
- Display negotiated cipher suite
- Show certificate issuer
- Show certificate subject
- Display certificate validity period
- Calculate remaining days until expiration
- Display Subject Alternative Names (SAN)

---

## Technologies Used

- Python 3
- ssl
- socket
- argparse
- datetime

---

## Installation

### Clone the repository

```bash
git clone https://github.com/astroezin/cybersecurity-portfolio.git
```

### Navigate to the project

```bash
cd cybersecurity-portfolio/projects/ssl-certificate-analyzer
```

No external dependencies are required.

---

## Usage

Analyze Google's certificate

```bash
python3 ssl_analyzer.py google.com
```

Analyze GitHub

```bash
python3 ssl_analyzer.py github.com
```

Analyze OpenAI

```bash
python3 ssl_analyzer.py openai.com
```

---

## Example Output

```text
======================================================================
SSL Certificate Analysis: github.com
======================================================================

TLS Version : TLSv1.3

Cipher Suite: TLS_AES_128_GCM_SHA256

Issuer
------------------------------
organizationName : DigiCert Inc

Subject
------------------------------
commonName : github.com

Validity
------------------------------
Valid From : ...
Valid Until: ...
Days Remaining: ...

Subject Alternative Names
------------------------------
github.com
www.github.com
```

---

## Project Structure

```text
ssl-certificate-analyzer/
│
├── ssl_analyzer.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Skills Demonstrated

- SSL/TLS Fundamentals
- Certificate Inspection
- Python Networking
- Secure Socket Programming
- Certificate Parsing
- Error Handling
- Command-Line Interfaces

---

## Interview Questions

### What is SSL/TLS?

SSL/TLS encrypts communication between clients and servers to provide confidentiality and integrity.

### What is a Certificate Authority (CA)?

A trusted organization that issues and signs digital certificates.

### What happens when a certificate expires?

Browsers warn users that the site's identity can no longer be trusted until the certificate is renewed.

### What is a Subject Alternative Name (SAN)?

A certificate extension that lists additional domain names covered by the certificate.

### Why is HTTPS important?

HTTPS helps protect data in transit from eavesdropping and tampering.

---

## Future Improvements

- Certificate chain analysis
- OCSP status checking
- Export reports to JSON
- Export reports to CSV
- Check multiple hosts from a file
- Expiration alerts
- Colorized output

---

## Disclaimer

This project is intended for educational purposes and authorized security research only.
