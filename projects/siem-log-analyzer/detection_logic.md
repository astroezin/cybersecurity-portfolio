# SIEM Log Analyzer Detection Logic

## Detection Rules

1. SSH Brute Force Detection
- Count failed logins by IP
- Trigger alert when threshold is exceeded

2. Account Compromise Detection
- Detect successful login after multiple failures

3. Root Login Detection
- Detect root account authentication

4. Privilege Escalation Detection
- Detect sudo commands executed with elevated privileges
