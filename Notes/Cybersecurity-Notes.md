# Cybersecurity Notes

This document summarizes core cybersecurity concepts that I have learned while building projects, completing CTFs, and studying security fundamentals.

---

# Table of Contents

1. CIA Triad
2. Types of Hackers
3. Malware
4. Cryptography
5. Authentication
6. Common Cyber Attacks
7. Web Security
8. Network Security
9. Security Operations Center (SOC)
10. Incident Response
11. Digital Forensics
12. Threat Intelligence
13. MITRE ATT&CK
14. OWASP Top 10
15. NIST Cybersecurity Framework
16. Security Best Practices
17. Common Security Tools

---

# CIA Triad

The CIA Triad is the foundation of information security.

## Confidentiality

Protect information from unauthorized access.

Examples:

- Encryption
- Access Control
- Multi-Factor Authentication

---

## Integrity

Ensure information has not been modified.

Examples:

- Hashing
- Digital Signatures

---

## Availability

Ensure systems remain accessible.

Examples:

- Backups
- Redundancy
- Load Balancers

---

# Types of Hackers

## White Hat

Authorized security professionals.

## Black Hat

Unauthorized attackers.

## Gray Hat

Operate between ethical and unethical boundaries.

---

# Malware

Common malware types:

- Virus
- Worm
- Trojan
- Ransomware
- Spyware
- Adware
- Rootkit
- Botnet

Typical infection vectors:

- Phishing
- Malicious downloads
- USB devices
- Software vulnerabilities

---

# Cryptography

## Symmetric Encryption

Same key for encryption and decryption.

Examples:

- AES
- 3DES

## Asymmetric Encryption

Uses a public/private key pair.

Examples:

- RSA
- ECC

## Hashing

One-way function.

Examples:

- SHA-256
- SHA-512

---

# Authentication

Common authentication factors:

- Something you know (password)
- Something you have (token)
- Something you are (fingerprint)

Use Multi-Factor Authentication (MFA) whenever possible.

---

# Common Cyber Attacks

- Phishing
- SQL Injection
- Cross-Site Scripting (XSS)
- CSRF
- Directory Traversal
- Command Injection
- Brute Force
- Password Spraying
- Man-in-the-Middle (MITM)
- Denial of Service (DoS)
- Distributed DoS (DDoS)

---

# Web Security

Key defenses:

- Input validation
- Output encoding
- HTTPS
- Content Security Policy (CSP)
- Secure cookies
- Least privilege

---

# Network Security

Important technologies:

- Firewalls
- IDS/IPS
- VPN
- VLAN
- Network Segmentation
- Proxy Servers

---

# Security Operations Center (SOC)

SOC responsibilities include:

- Monitor alerts
- Investigate incidents
- Threat hunting
- Malware analysis
- Log analysis
- Reporting

Common tools:

- Splunk
- Wazuh
- Microsoft Sentinel
- Elastic Security

---

# Incident Response

The standard lifecycle:

1. Preparation
2. Identification
3. Containment
4. Eradication
5. Recovery
6. Lessons Learned

---

# Digital Forensics

Evidence sources include:

- Authentication logs
- Event logs
- Memory dumps
- Network captures (PCAP)
- Browser history
- File metadata

Maintain evidence integrity using cryptographic hashes.

---

# Threat Intelligence

Threat intelligence helps organizations understand:

- Threat actors
- Indicators of Compromise (IOCs)
- Tactics, Techniques, and Procedures (TTPs)

---

# MITRE ATT&CK

MITRE ATT&CK documents attacker behavior.

Common tactics include:

- Initial Access
- Execution
- Persistence
- Privilege Escalation
- Defense Evasion
- Credential Access
- Discovery
- Lateral Movement
- Collection
- Exfiltration
- Impact

---

# OWASP Top 10

- Broken Access Control
- Cryptographic Failures
- Injection
- Insecure Design
- Security Misconfiguration
- Vulnerable Components
- Authentication Failures
- Software Integrity Failures
- Logging & Monitoring Failures
- SSRF

---

# NIST Cybersecurity Framework

Five core functions:

- Identify
- Protect
- Detect
- Respond
- Recover

---

# Security Best Practices

- Keep systems updated.
- Use strong passwords.
- Enable MFA.
- Follow the Principle of Least Privilege.
- Encrypt sensitive data.
- Perform regular backups.
- Monitor logs.
- Conduct vulnerability assessments.

---

# Common Security Tools

Network:

- Nmap
- Wireshark
- tcpdump

Web:

- Burp Suite
- Gobuster
- ffuf

Exploitation:

- Metasploit

OSINT:

- theHarvester
- Amass

Password Auditing:

- John the Ripper
- Hashcat

Forensics:

- Autopsy
- Volatility

---

# References

- NIST Cybersecurity Framework
- MITRE ATT&CK
- OWASP Top 10
- CIS Controls
