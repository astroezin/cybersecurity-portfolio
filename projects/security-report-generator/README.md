# Security Report Generator

A professional Python tool that converts structured security findings stored in JSON format into clean, well-organized Markdown security assessment reports.

This project demonstrates report automation, structured data processing, and professional security documentation practices commonly used by penetration testers, SOC analysts, incident responders, and security consultants.

---

## Features

* Generate professional Markdown security reports
* Read findings from JSON files
* Executive Summary
* Assessment Scope
* Severity statistics
* Detailed findings
* Actionable remediation recommendations
* Professional report conclusion
* Command-line interface using `argparse`
* Error handling and input validation
* Modular Python architecture

---

## Technologies Used

* Python 3
* JSON
* argparse
* pathlib
* datetime
* Kali Linux
* Git & GitHub

---

## Project Structure

```text
security-report-generator/
├── reports/
├── samples/
│   └── sample_findings.json
├── screenshots/
├── templates/
├── report_builder.py
├── report_generator.py
├── requirements.txt
├── .gitignore
├── README.md
└── LICENSE
```

---

## Installation

```bash
git clone https://github.com/astroezin/cybersecurity-portfolio.git

cd cybersecurity-portfolio/projects/security-report-generator
```

No external libraries are required for Version 1.

---

## Usage

Generate a report:

```bash
python report_generator.py samples/sample_findings.json
```

Generate a report with a custom output path:

```bash
python report_generator.py samples/sample_findings.json --output reports/custom_report.md
```

---

## Example Output

The tool generates a Markdown report containing:

* Report Information
* Scope
* Executive Summary
* Severity Summary
* Detailed Findings
* Recommendations
* Conclusion

---

## Skills Demonstrated

* Security Reporting
* Technical Documentation
* Report Automation
* JSON Processing
* Python CLI Development
* Error Handling
* Modular Software Design
* Defensive Security

---

## Future Improvements

### Version 2

* HTML report generation
* PDF export
* DOCX export
* CVSS scoring
* MITRE ATT&CK mapping

### Version 3

* Charts and graphs
* Company branding
* Executive dashboards
* Multiple report templates

### Version 4

* Automatic integration with portfolio tools
* Interactive reporting
* Docker support
* CI/CD workflow
* Unit testing

---

## License

This project is licensed under the MIT License.
