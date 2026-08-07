# Endpoint Detection & Response (EDR) Simulator

A professional Blue Team security tool that simulates an Endpoint Detection and Response (EDR) platform.

The project analyzes endpoint activity, detects suspicious behavior, maps threats to MITRE ATT&CK techniques, calculates risk severity, and generates incident investigation reports.

Designed to demonstrate SOC analyst workflows and defensive security automation.

---

# Features

## Process Monitoring

Detects suspicious endpoint processes:

- PowerShell abuse
- Command shell execution
- Suspicious scripting activity
- Malicious command patterns


Example detections:

```

powershell.exe -enc <encoded_command>

cmd.exe suspicious execution

```

MITRE ATT&CK:

```

T1059 - Command and Scripting Interpreter

T1059.001 - PowerShell

```

---

# Persistence Detection

Identifies possible persistence mechanisms:

- Startup entries
- Suspicious executable locations
- Script-based persistence


MITRE ATT&CK:

```

T1547 - Boot or Logon Autostart Execution

```

---

# File Activity Monitoring

Detects suspicious file behavior:

- Executable file creation
- Script files
- Potential malware drops


MITRE ATT&CK:

```

T1204 - User Execution

```

---

# Network Behavior Detection

Analyzes endpoint network events:

Detects:

- Suspicious outbound connections
- Known risky ports
- Command and control indicators


MITRE ATT&CK:

```

T1071 - Application Layer Protocol

```

---

# Risk Engine

The built-in risk engine calculates:

```

LOW
MEDIUM
HIGH
CRITICAL

```

Based on:

- Detection severity
- Number of alerts
- Threat behavior


Example:

```

Risk Level: CRITICAL

Risk Score: 100/100

```

---

# Incident Reporting

Generates:

## JSON Report

```

reports/

edr_incident_report.json

```


## Markdown Report

```

reports/

edr_incident_report.md

```

Reports include:

- Incident ID
- Detection summary
- Risk assessment
- MITRE ATT&CK mapping
- Timestamp

---

# Technologies Used

- Python 3
- JSON
- MITRE ATT&CK Framework
- Security Automation
- Blue Team Concepts
- SOC Investigation Workflow


---

# Installation

Clone repository:

```bash
git clone https://github.com/astroezin/cybersecurity-portfolio.git
```

Navigate:

```bash
cd cybersecurity-portfolio/projects/endpoint-detection-response
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

Install requirements:

```bash
pip install -r requirements.txt
```

---

# Usage

Run the EDR simulator:

```bash
python edr_agent.py
```

Example output:

```
============================================================
ENDPOINT DETECTION & RESPONSE SIMULATOR
============================================================

Detections: 8

Risk Level: CRITICAL

Risk Score: 100/100

Detection Summary
----------------------------------------
HIGH:
Suspicious process detected: powershell.exe

CRITICAL:
Suspicious command pattern detected

HIGH:
Suspicious outbound connection detected


Reports Generated:

edr_incident_report.json
edr_incident_report.md
```

---

# Project Structure

```
endpoint-detection-response/

├── core/
│   ├── config.py
│   ├── database.py
│   ├── logger.py
│   └── reporter.py
│
├── detection/
│   ├── behavior_rules.py
│   ├── process_monitor.py
│   ├── persistence_detector.py
│   ├── file_monitor.py
│   └── network_detector.py
│
├── intelligence/
│   ├── mitre_mapping.py
│   └── risk_engine.py
│
├── samples/
│   ├── processes.json
│   ├── startup_entries.json
│   └── network_events.json
│
├── reports/
│
├── logs/
│
├── screenshots/
│
├── edr_agent.py
├── requirements.txt
├── LICENSE
└── README.md
```

---

# Skills Demonstrated

This project demonstrates:

* Endpoint monitoring concepts
* SOC analyst workflow
* Threat detection engineering
* MITRE ATT&CK mapping
* Security automation
* Incident response reporting
* Python security development

---

# Future Improvements

Possible enhancements:

* Real-time process monitoring
* Windows event log integration
* Sysmon support
* YARA integration
* Threat intelligence API integration
* Machine learning anomaly detection
* Web dashboard interface
* Automated endpoint isolation

---

# Security Notice

This project is intended for:

* Cybersecurity education
* Defensive security research
* SOC analyst training
* Authorized environments only

Do not use this tool to monitor systems without permission.

---

# License

MIT License
