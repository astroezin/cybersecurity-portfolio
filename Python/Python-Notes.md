# Python Notes for Cybersecurity

This document summarizes the Python concepts and libraries used throughout my cybersecurity projects.

---

# Table of Contents

1. Variables
2. Data Types
3. Operators
4. Conditional Statements
5. Loops
6. Functions
7. Modules
8. File Handling
9. Exception Handling
10. JSON
11. Regular Expressions
12. argparse
13. socket
14. threading
15. requests
16. hashlib
17. os
18. subprocess
19. Best Practices

---

# Variables

```python
name = "Rejin"
age = 25
```

---

# Data Types

```python
str
int
float
bool
list
tuple
dict
set
```

Example:

```python
numbers = [1,2,3]

user = {
    "name":"Rejin",
    "role":"Cybersecurity"
}
```

---

# Operators

Arithmetic

```python
+
-
*
/
%
**
//
```

Comparison

```python
==
!=
<
>
<=
>=
```

Logical

```python
and
or
not
```

---

# Conditional Statements

```python
if score >= 90:
    print("Excellent")
elif score >= 75:
    print("Good")
else:
    print("Try Again")
```

---

# Loops

For Loop

```python
for i in range(5):
    print(i)
```

While Loop

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

---

# Functions

```python
def greet(name):
    return f"Hello {name}"

print(greet("Rejin"))
```

---

# Modules

Import

```python
import os
import socket
import hashlib
```

Specific Import

```python
from pathlib import Path
```

---

# File Handling

Read

```python
with open("file.txt") as f:
    print(f.read())
```

Write

```python
with open("file.txt","w") as f:
    f.write("Hello")
```

Append

```python
with open("file.txt","a") as f:
    f.write("World")
```

---

# Exception Handling

```python
try:
    number = int(input())
except ValueError:
    print("Invalid number")
```

---

# JSON

Write

```python
import json

with open("data.json","w") as f:
    json.dump(data,f,indent=4)
```

Read

```python
with open("data.json") as f:
    data = json.load(f)
```

---

# Regular Expressions

```python
import re

email = "user@example.com"

pattern = r"\S+@\S+\.\S+"

if re.match(pattern,email):
    print("Valid")
```

Useful Functions

```python
re.search()
re.findall()
re.match()
re.sub()
```

---

# argparse

Used for command-line arguments.

Example

```python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("host")

args = parser.parse_args()

print(args.host)
```

Useful for:

- Port Scanner
- DNS Lookup
- WHOIS Lookup
- Password Generator

---

# socket

Used for networking.

Example

```python
import socket

sock = socket.socket()

sock.connect(("google.com",80))
```

Common Functions

```python
connect()

connect_ex()

recv()

send()

close()

settimeout()
```

Projects

- Port Scanner
- Banner Grabber
- Network Scanner

---

# threading

Run multiple tasks simultaneously.

Example

```python
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=100) as executor:
    executor.submit(scan_port)
```

Benefits

- Faster scanning
- Better performance
- Parallel execution

Projects

- Network Scanner

---

# requests

HTTP library.

Install

```bash
pip install requests
```

Example

```python
import requests

response = requests.get("https://example.com")

print(response.status_code)
```

Useful Properties

```python
response.text

response.headers

response.json()

response.status_code
```

Projects

- HTTP Header Analyzer
- Future Web Scanner

---

# hashlib

Cryptographic hashing.

Example

```python
import hashlib

sha = hashlib.sha256()

sha.update(b"Hello")

print(sha.hexdigest())
```

Algorithms

- MD5
- SHA1
- SHA224
- SHA256
- SHA384
- SHA512

Projects

- File Integrity Monitor
- Malware Hash Checker

---

# os

Interact with the operating system.

Examples

```python
os.listdir()

os.walk()

os.path.exists()

os.path.join()

os.mkdir()
```

Projects

- File Integrity Monitor

---

# subprocess

Execute system commands.

Example

```python
import subprocess

subprocess.run(["ls","-la"])
```

Useful For

- Running Nmap
- Running external tools
- Automation

---

# Best Practices

- Use meaningful variable names.
- Write reusable functions.
- Handle exceptions gracefully.
- Use virtual environments.
- Follow PEP 8 style guidelines.
- Add comments only when they improve clarity.
- Use `argparse` instead of manually parsing `sys.argv`.
- Use `with open(...)` for file operations.
- Store dependencies in `requirements.txt`.
- Keep projects modular.

---

# Cybersecurity Libraries to Learn Next

- scapy
- paramiko
- dnspython
- python-whois
- beautifulsoup4
- selenium
- flask
- fastapi
- yara-python
- pefile
- pycryptodome
- psutil

---

# References

- Python Official Documentation
- OWASP
- NIST
- MITRE ATT&CK
