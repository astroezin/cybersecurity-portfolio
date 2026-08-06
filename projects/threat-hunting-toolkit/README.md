# Threat Hunting Toolkit

A Python-based defensive security tool designed to assist security analysts in performing basic threat hunting activities.

The toolkit automates the analysis of files, logs, and Indicators of Compromise (IOCs) to identify suspicious activity and generate structured investigation reports.

This project simulates workflows commonly used by SOC analysts during security monitoring and incident response.

---

# Features

## File Hunting

- Analyze files for suspicious characteristics
- Calculate SHA-256 file hashes
- Detect potential suspicious files
- Support malware investigation workflows


## IOC Hunting

Extract and identify:

- IPv4 addresses
- Domains
- File hashes

Useful for:

- Threat intelligence investigations
- Malware analysis
- Incident response


## Log Hunting

Analyze security logs for suspicious behaviors:

- Failed login attempts
- Privilege escalation activity
- Suspicious commands
- Potential attacker behavior


## Automated Reporting

Generates:

- JSON reports
- Markdown reports

Reports contain:

- Findings
- Detection type
- Severity
- Investigation details


## Logging

Maintains analyst activity logs:

- Hunting start time
- Analysis actions
- Findings detected
- Report generation status

---

# Technologies Used

- Python 3
- Linux / Kali Linux
- Regular Expressions
- JSON
- SHA-256 Hashing
- File Analysis
- Log Analysis
- Threat Intelligence Concepts
- MITRE ATT&CK Framework Concepts

---

# Installation

Clone the repository:

```bash
git clone https://github.com/astroezin/cybersecurity-portfolio.git
```


Navigate to project:

```bash
cd cybersecurity-portfolio/projects/threat-hunting-toolkit
```

Create virtual environment:
```
python3 -m venv venv
```
Activate:

Linux:
```
source venv/bin/activate
```
Install requirements:
```
pip install -r requirements.txt
```
# Usage

## Log Hunting

Analyze authentication logs:

python threat_hunter.py --log samples/security.log

Example:

==================================================
THREAT HUNTING REPORT
==================================================

Findings: 3

Reports Generated:

JSON Report:
reports/hunt_report_xxxxx.json

Markdown Report:
reports/hunt_report_xxxxx.md
File Analysis

Analyze suspicious files:

python threat_hunter.py --file samples/test_file.txt

Example output:

{
 "file": "samples/test_file.txt",
 "sha256": "example_hash",
 "suspicious": false
}
IOC Extraction

Search files for indicators:

python threat_hunter.py --ioc-file samples/ioc_test.log

Detected indicators:

IP Addresses
Domains
Hashes
Example Detection Workflow

Attack scenario:

Failed SSH Login Attempts
          |
          |
Successful Login
          |
          |
Privilege Escalation
          |
          |
Possible Account Compromise

The toolkit helps identify these behaviors and produces investigation reports.

Folder Structure
threat-hunting-toolkit/

├── core/
│   ├── config.py
│   ├── logger.py
│   └── reporter.py
│
├── hunters/
│   ├── file_hunter.py
│   ├── ioc_hunter.py
│   └── log_hunter.py
│
├── samples/
│   ├── security.log
│   ├── ioc_test.log
│   └── test_file.txt
│
├── reports/
│
├── screenshots/
│
├── logs/
│
├── threat_hunter.py
├── requirements.txt
└── README.md
Skills Demonstrated
Blue Team Skills
Threat hunting methodology
Security log analysis
IOC investigation
Incident detection
SOC Analyst Skills
Alert investigation
Evidence collection
Security reporting
Automation workflows
Programming Skills
Python automation
Modular architecture
CLI development
File processing
Report generation
Security Concepts
MITRE ATT&CK mapping
Authentication attacks
Privilege escalation detection
Threat intelligence concepts
Future Improvements
Version 2

Planned improvements:

VirusTotal integration
AbuseIPDB integration
More IOC formats
Advanced detection rules
Version 3

Planned improvements:

Real-time log monitoring
Windows Event Log support
Email alerting
SIEM integration
Version 4

Planned improvements:

Machine learning anomaly detection
Threat scoring engine
Automated incident response actions
Dashboard interface
Screenshots

Add screenshots showing:

CLI execution
Detection results
Generated reports
Log output
License

MIT License

This project is created for educational purposes and defensive security research.
