# SIEM Alert Dashboard

A professional web-based Security Information and Event Management (SIEM) dashboard built with Python and Flask. The application simulates a Security Operations Center (SOC) environment by displaying security alerts, dashboard statistics, MITRE ATT&CK mappings, and detailed alert information through a clean Bootstrap interface.

This project is designed for cybersecurity learning and to showcase SOC analyst skills in a professional portfolio.

---

# Features

## Dashboard

* Real-time style SIEM dashboard
* Total alert count
* Severity statistics
* Alert status summary
* MITRE ATT&CK technique counts
* Alert source statistics

## Alert Management

* View all security alerts
* Individual alert detail page
* Severity badges
* Alert status tracking
* Detection rule information
* Source and destination IP addresses
* User information
* Event timestamps

## MITRE ATT&CK Mapping

Displays ATT&CK technique IDs associated with each alert, allowing analysts to correlate detections with known adversary behaviors.

Examples:

* T1110 – Brute Force
* T1548 – Abuse Elevation Control Mechanism
* T1059.001 – PowerShell
* T1046 – Network Service Discovery
* T1204 – User Execution
* T1105 – Ingress Tool Transfer

## Reporting

Dashboard includes summaries for:

* Alert severities
* Alert status
* Alert sources
* MITRE ATT&CK techniques

## User Interface

* Bootstrap 5 responsive layout
* Searchable alerts table
* Responsive cards
* Clean SOC-style dashboard
* Mobile-friendly interface

---

# Technologies Used

* Python 3
* Flask
* Jinja2
* Bootstrap 5
* HTML5
* CSS3
* JavaScript

---

# Installation

Clone the repository:

```bash
git clone https://github.com/astroezin/cybersecurity-portfolio.git
```

Navigate to the project:

```bash
cd cybersecurity-portfolio/projects/siem-alert-dashboard
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it:

Linux/macOS:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Usage

Start the application:

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

# Project Structure

```text
siem-alert-dashboard/
├── app.py
├── core/
│   ├── __init__.py
│   ├── config.py
│   ├── loader.py
│   ├── logger.py
│   └── statistics.py
├── templates/
│   ├── layout.html
│   ├── index.html
│   ├── alert.html
│   └── reports.html
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── dashboard.js
│   └── icons/
├── samples/
│   └── alerts.json
├── reports/
├── logs/
├── screenshots/
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

# Dashboard Capabilities

* Dashboard overview
* Alert statistics
* Severity breakdown
* Status monitoring
* MITRE ATT&CK mapping
* Alert detail pages
* Search functionality
* Responsive design

---

# Skills Demonstrated

* Security Operations Center (SOC) concepts
* SIEM alert analysis
* MITRE ATT&CK mapping
* Incident investigation workflow
* Python web development
* Flask application development
* JSON data processing
* Dashboard design
* Security reporting
* Front-end integration

---

# Future Improvements

* Authentication and role-based access
* CSV and PDF report export
* Dark mode
* Elasticsearch integration
* Splunk data ingestion
* Microsoft Sentinel integration
* Sigma rule support
* Live alert streaming with WebSockets
* Interactive charts using Chart.js
* REST API for external integrations

---

# Screenshots

Create and add screenshots of:

* Dashboard
* Alert Details page
* Reports page
* Search functionality

Store them in:

```text
screenshots/
```

---

# Security Notice

This project is intended for:

* Cybersecurity education
* SOC analyst practice
* Portfolio demonstrations
* Authorized security testing

Do not use this project to monitor systems without proper authorization.

---

# License

MIT License

Copyright (c) 2026 Rejin Lama
