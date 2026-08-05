# SIEM Log Analyzer

A Python-based Security Information and Event Management (SIEM) style log analysis tool that detects suspicious activity from Linux authentication logs.

This project simulates a basic SOC (Security Operations Center) monitoring workflow by collecting authentication events, normalizing logs, applying detection rules, generating alerts, and creating security reports.

---

# Project Overview

Security analysts constantly monitor authentication logs to identify threats such as:

- SSH brute force attacks
- Unauthorized login attempts
- Account compromise
- Privilege escalation
- Suspicious root access attempts

This tool automates the first stage of security monitoring by analyzing Linux authentication logs and generating actionable security alerts.

---

# Features

## Log Analysis

- Reads Linux authentication logs
- Parses SSH authentication events
- Converts raw logs into structured security events

## Threat Detection

Detects:

- Failed SSH login attempts
- SSH brute force attacks
- Successful login after brute force attempts
- Root account login attempts
- Privilege escalation through sudo commands

## Security Reporting

Generates:

- Terminal SOC-style alerts
- Severity classification
- JSON security reports

---

# Detection Rules

| Detection | Severity | Description |
|---|---|---|
| SSH Brute Force | HIGH | Multiple failed login attempts from the same IP |
| Account Compromise | CRITICAL | Successful login after brute force activity |
| Root Login Attempt | MEDIUM | Attempts to authenticate as root |
| Privilege Escalation | MEDIUM | User executes commands with root privileges |

---

# Technologies Used

- Python 3
- Linux Authentication Logs
- Regular Expressions
- JSON Reporting
- Command Line Interface (argparse)
- Linux CLI

---

# Installation

Clone the repository:

```bash
git clone https://github.com/astroezin/cybersecurity-portfolio.git
