# Log Correlation Engine

A Python-based Security Operations Center (SOC) automation tool that analyzes security logs, detects suspicious activities, correlates multiple events into security incidents, calculates risk scores, generates alerts, builds attack timelines, and creates investigation reports.

This project simulates a simplified SIEM (Security Information and Event Management) workflow used by SOC analysts for threat detection and incident response.

---

# Project Description

Modern security teams receive thousands of security events every day.

A single event may not indicate an attack, but combining multiple events can reveal malicious activity.

Example:

```

Multiple Failed SSH Logins
+
Successful Login
+
Privileged Command Execution

```
        ↓
```

Possible Account Compromise

```

The Log Correlation Engine automates this process by:

- Parsing authentication logs
- Detecting suspicious behavior
- Applying detection rules
- Correlating related events
- Mapping activity to MITRE ATT&CK techniques
- Calculating risk severity
- Generating SOC alerts
- Creating incident reports

---

# Features

## 1. Security Log Parsing

The engine analyzes Linux authentication logs and converts raw log entries into structured security events.

Supported events:

- Failed login attempts
- Successful authentication
- Privileged command execution


Example:

```

Failed password for admin from 192.168.1.50

↓

{
"event_type": "failed_login",
"username": "admin",
"source_ip": "192.168.1.50"
}

```

---

# 2. Detection Rule Engine

The detection engine identifies suspicious activities.

Current detection rules:

## SSH Brute Force Detection

Detects:

- Multiple failed SSH authentication attempts
- Possible credential attacks


MITRE ATT&CK:

```

T1110 - Brute Force

```


---

## Privilege Escalation Detection

Detects:

- Suspicious privileged command execution
- Possible unauthorized privilege usage


MITRE ATT&CK:

```

T1548 - Abuse Elevation Control Mechanism

```

---

# 3. Event Correlation

Individual events may appear harmless.

The correlation engine combines multiple events to identify advanced attacks.

Example:

```

Failed Login Attempts

```
    +
```

Successful Login

```
    +
```

sudo /bin/bash Execution

```
    ↓
```

Possible Account Compromise

```

Detected incident:

```

Possible Account Compromise

```

MITRE ATT&CK Mapping:

```

T1110 - Brute Force

T1078 - Valid Accounts

T1548 - Privilege Escalation

```

---

# 4. Risk Scoring Engine

The engine calculates incident severity.

Risk levels:

| Score | Severity |
|---|---|
| 0 | Informational |
| 10-25 | Low |
| 25-50 | Medium |
| 50-80 | High |
| 80-100 | Critical |

Example:

```

Incident:

Possible Account Compromise

Score:

90/100

Risk:

CRITICAL

````

---

# 5. Alert Management

The system creates structured SOC alerts.

Alert information includes:

- Alert ID
- Timestamp
- Incident title
- Severity
- Risk score
- MITRE ATT&CK techniques
- Alert status


Example:

```json
{
 "alert_id": "ALERT-123456",
 "severity": "CRITICAL",
 "risk_score": 90,
 "status": "NEW"
}
````

---

# 6. Attack Timeline Generation

The engine reconstructs the attack sequence.

Example:

```
Step 1:
Failed Login

Step 2:
Successful Login

Step 3:
sudo Command Execution
```

This helps analysts understand:

* Initial access
* Account compromise
* Privilege escalation
* Attack progression

---

# 7. Incident Report Generation

Automatically generates:

## JSON Reports

Machine-readable format:

```
reports/incident_xxxxxx.json
```

## Markdown Reports

Human-readable investigation report:

```
reports/incident_xxxxxx.md
```

Reports include:

* Incident details
* Severity
* Risk score
* MITRE techniques
* Timeline

---

# Technologies Used

## Programming

* Python 3

## Security Concepts

* SOC Operations
* SIEM Architecture
* Log Analysis
* Detection Engineering
* Incident Response
* Threat Detection
* MITRE ATT&CK Framework

## Environment

* Kali Linux
* Linux CLI
* Git & GitHub

---

# Installation

Clone the repository:

```bash
git clone https://github.com/astroezin/cybersecurity-portfolio.git
```

Navigate to project:

```bash
cd cybersecurity-portfolio/projects/log-correlation-engine
```

Create virtual environment:

```bash
python3 -m venv venv
```

Activate environment:

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

Run the correlation engine:

```bash
python correlation_engine.py samples/auth.log
```

---

# Example Input

Sample log:

```
Failed password for admin from 192.168.1.50

Accepted password for admin from 192.168.1.50

sudo: admin : COMMAND=/bin/bash
```

---

# Example Output

```
==================================================
LOG CORRELATION ENGINE
==================================================

Analyzing: samples/auth.log


[ALERT]

SSH Brute Force Detected

Severity:
HIGH

MITRE:
T1110



[ALERT]

Privilege Escalation Activity

Severity:
HIGH

MITRE:
T1548



==================================================
INCIDENT DETECTED
==================================================


Title:

Possible Account Compromise


Severity:

CRITICAL


Risk:

90/100


Risk Level:

CRITICAL


MITRE ATT&CK:

T1110
T1078
T1548


Reports Generated:


JSON:

reports/incident_xxxxxx.json


Markdown:

reports/incident_xxxxxx.md
```

---

# Folder Structure

```
log-correlation-engine/

├── alerts/
│   └── .gitkeep
│
├── core/
│   ├── alert.py
│   ├── config.py
│   ├── correlator.py
│   ├── parser.py
│   ├── reporter.py
│   ├── rules.py
│   ├── scoring.py
│   └── timeline.py
│
├── reports/
│   └── .gitkeep
│
├── samples/
│   └── auth.log
│
├── screenshots/
│
├── correlation_engine.py
│
├── requirements.txt
│
├── LICENSE
│
└── README.md
```

---

# Skills Demonstrated

## SOC Analyst Skills

* Security event monitoring
* Log investigation
* Alert triage
* Incident detection
* Incident documentation

## Blue Team Skills

* Detection engineering
* SIEM concepts
* Threat correlation
* MITRE ATT&CK mapping
* Security automation

## Python Development Skills

* Object-oriented programming
* Modular project design
* CLI application development
* File processing
* Report automation

---

# Testing

Run:

```bash
python correlation_engine.py samples/auth.log
```

Expected:

* Detect brute force activity
* Detect privilege escalation
* Create incident
* Calculate risk score
* Generate reports

---

# Future Improvements

## Version 2

Planned improvements:

* More Linux log formats
* Windows Event Log support
* JSON log ingestion
* Custom detection rules
* YAML rule configuration
* Improved alert filtering

---

## Version 3

Advanced features:

* Database storage
* Web dashboard
* User authentication
* Alert search system
* Historical investigations

---

## Version 4

Enterprise-style features:

* Real-time log monitoring
* Threat intelligence integration
* Machine learning anomaly detection
* Automated response actions
* SOC analyst dashboard

---

# Learning Outcomes

After completing this project, you understand:

* How SIEM platforms process logs
* How SOC detection rules work
* How event correlation identifies attacks
* How alerts are prioritized
* How incident reports are created
* How MITRE ATT&CK is applied in investigations

---

# License

MIT License

Copyright (c) 2026 Rejin Lama

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files.
