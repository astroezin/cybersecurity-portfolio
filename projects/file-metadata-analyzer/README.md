# File Metadata Analyzer

A professional digital forensics tool that extracts file metadata, calculates cryptographic hashes, performs basic malware analysis, detects suspicious indicators, and generates forensic investigation reports.

This project simulates a real-world forensic workflow used by security analysts during evidence collection and file investigation.

---

# Features

## Version 1 - File Analysis

### File Information Extraction
- Filename identification
- Absolute file path
- File size analysis
- MIME type detection
- Creation timestamp
- Modification timestamp

### Cryptographic Hashing

Generates:

- MD5 hash
- SHA1 hash
- SHA256 hash

Used for:
- File identification
- Malware sample tracking
- Threat intelligence lookup


### Reporting

Generates:

- JSON forensic report
- Markdown investigation report


---

# Version 2 - Extended Metadata Analysis

## Document Metadata Extraction

Supports:

- EXIF metadata extraction
- PDF metadata extraction
- Office document metadata extraction


## Suspicious Metadata Detection

Detects:

- Suspicious file extensions
- Suspicious keywords
- Potential malware-related indicators


Examples:

```

.ps1
.exe
.dll
password
dump
credential

```

---

# Version 3 - Malware Analysis Integration

## Entropy Analysis

Calculates file entropy to identify:

- Packed files
- Encrypted content
- Potential malware obfuscation


## YARA Integration

Supports YARA scanning for:

- Malware signatures
- Suspicious patterns
- Threat detection rules


## VirusTotal Integration

Provides hash-based threat intelligence lookup.

Capabilities:

- Malware detection results
- Reputation analysis
- Threat intelligence enrichment


---

# Version 4 - Professional Forensic Workflow

## Case Management

Generates unique:

- Case ID
- Evidence ID


## Evidence Tracking

Tracks:

- Evidence collection time
- File information
- Investigation history


## Chain of Custody

Maintains forensic evidence records:

Example:

```

Evidence collected
Timestamp recorded
Analysis performed

```


## Timeline Generation

Creates investigation timeline:

Example:

```

File Created
File Modified
Evidence Collected

```


---

# Technologies Used

- Python 3
- hashlib
- pathlib
- mimetypes
- python-magic
- Pillow
- PyMuPDF
- olefile
- yara-python
- VirusTotal API
- JSON
- Markdown


---

# Installation

Clone repository:

```bash
git clone https://github.com/astroezin/cybersecurity-portfolio.git
````

Navigate:

```bash
cd cybersecurity-portfolio/projects/file-metadata-analyzer
```

Create virtual environment:

```bash
python3 -m venv venv
```

Activate:

Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Usage

## Analyze a file

```bash
python metadata_analyzer.py samples/test.txt
```

Example:

```
============================================================

FILE METADATA ANALYZER

============================================================

File:
samples/test.txt

SHA256:
335aaf2752deb85043fb515241e94311f455c5cf5a522f7dd57faf69765f409c

Entropy:
3.604

Suspicious Findings:
None


Reports Generated:

JSON:
reports/metadata_report_xxxxx.json

Markdown:
reports/metadata_report_xxxxx.md
```

---

# Suspicious File Example

Command:

```bash
python metadata_analyzer.py samples/password_dump.ps1
```

Output:

```
Suspicious Findings:

- Suspicious extension: .ps1
- Suspicious keyword: password
- Suspicious keyword: dump
```

---

# Project Structure

```
file-metadata-analyzer/

├── core/
│   ├── config.py
│   ├── forensic.py
│   ├── hashing.py
│   ├── metadata.py
│   ├── malware.py
│   ├── reporter.py
│   └── __init__.py
│
├── logs/
│   └── .gitkeep
│
├── reports/
│   └── .gitkeep
│
├── samples/
│   ├── test.txt
│   └── password_dump.ps1
│
├── screenshots/
│
├── metadata_analyzer.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

# Example Report Contents

Generated reports include:

## Case Information

* Case ID
* Creation timestamp

## Evidence Information

* Evidence ID
* File path
* Collection timestamp

## File Metadata

* Filename
* Size
* MIME type
* Created date
* Modified date

## Hash Information

* MD5
* SHA1
* SHA256

## Security Analysis

* Entropy score
* YARA results
* VirusTotal results
* Suspicious findings

## Investigation Timeline

* File creation
* File modification
* Evidence collection

## Chain of Custody

* Evidence handling history

---

# Skills Demonstrated

This project demonstrates:

* Digital forensics fundamentals
* File analysis
* Malware triage
* Threat intelligence integration
* Cryptographic hashing
* Evidence handling
* Security automation
* Python security tooling development
* Report generation

---

# Future Improvements

Possible improvements:

* Full sandbox malware execution analysis
* Memory dump analysis
* Automated malware family classification
* MITRE ATT&CK technique mapping
* Web dashboard interface
* Database evidence storage
* PDF professional reporting
* Cloud malware scanning

---

# Security Notice

This tool is designed for:

* Defensive security research
* Digital forensics learning
* Malware analysis practice
* Authorized investigations

Only analyze files that you have permission to investigate.

---

# License

MIT License

Copyright (c) 2026 Rejin Lama
