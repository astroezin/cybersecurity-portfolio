# HTTP Header Analyzer

A Python command-line tool that analyzes HTTP response headers and checks for commonly recommended web security headers.

---

## Features

- Analyze HTTP response headers
- Display HTTP status code
- Display server information
- Check for common security headers
- Explain the purpose of each security header
- Simple command-line interface using `argparse`

---

## Technologies Used

- Python 3
- Requests
- argparse

---

## Security Headers Checked

| Header | Purpose |
|---------|---------|
| Strict-Transport-Security | Forces browsers to use HTTPS |
| Content-Security-Policy | Helps prevent Cross-Site Scripting (XSS) |
| X-Frame-Options | Protects against clickjacking attacks |
| X-Content-Type-Options | Prevents MIME type sniffing |
| Referrer-Policy | Controls referrer information sent by the browser |
| Permissions-Policy | Restricts browser features and APIs |

---

## Installation

### Clone the repository

```bash
git clone https://github.com/astroezin/cybersecurity-portfolio.git
```

### Navigate to the project

```bash
cd cybersecurity-portfolio/projects/http-header-analyzer
```

### Create a virtual environment

```bash
python3 -m venv .venv
```

### Activate the virtual environment

Linux/macOS

```bash
source .venv/bin/activate
```

Windows

```powershell
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

Analyze GitHub

```bash
python3 header_analyzer.py https://github.com
```

Analyze OpenAI

```bash
python3 header_analyzer.py https://openai.com
```

Analyze Example.com

```bash
python3 header_analyzer.py https://example.com
```

---

## Example Output

```text
======================================================================
HTTP Header Analysis: https://github.com
======================================================================

Status Code : 200
Server      : GitHub.com

Security Headers
----------------------------------------------------------------------

[FOUND ] Strict-Transport-Security
         max-age=31536000

[FOUND ] Content-Security-Policy
         default-src ...

[FOUND ] X-Frame-Options
         deny

[FOUND ] X-Content-Type-Options
         nosniff

[FOUND ] Referrer-Policy
         origin-when-cross-origin

[MISSING] Permissions-Policy
```

---

## Project Structure

```text
http-header-analyzer/
│
├── header_analyzer.py
├── README.md
├── requirements.txt
├── .gitignore
└── .venv/
```

---

## Skills Demonstrated

- Python Programming
- HTTP Protocol
- Web Security
- Security Header Analysis
- HTTP Requests
- argparse
- Virtual Environments
- Error Handling

---

## Interview Questions

### What are HTTP headers?

HTTP headers are key-value pairs exchanged between a client and a server that provide information about the request or response.

### Why is the `Content-Security-Policy` header important?

It helps mitigate Cross-Site Scripting (XSS) attacks by restricting the sources from which content can be loaded.

### What does `Strict-Transport-Security` (HSTS) do?

It instructs browsers to always use HTTPS when communicating with a website.

### What is clickjacking?

Clickjacking is an attack that tricks users into clicking hidden or disguised elements. The `X-Frame-Options` header helps defend against this.

### Does a missing security header always mean a website is vulnerable?

No. Some headers are only relevant in certain contexts, and their absence alone does not necessarily indicate a vulnerability. Security should be assessed as a whole.

---

## Future Improvements

- Colorized terminal output
- Export results to JSON
- Export results to CSV
- Scan multiple URLs from a file
- Generate HTML reports
- Grade security headers (A–F)
- Support concurrent analysis
- Detect additional headers such as Cache-Control and Set-Cookie

---

## Disclaimer

This project is intended for educational purposes and authorized security testing only.
