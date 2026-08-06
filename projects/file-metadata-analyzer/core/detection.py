"""
Suspicious file detection engine
"""

from pathlib import Path



SUSPICIOUS_EXTENSIONS = [

    ".exe",
    ".dll",
    ".bat",
    ".cmd",
    ".ps1",
    ".vbs",
    ".scr"

]


SUSPICIOUS_KEYWORDS = [

    "password",
    "credential",
    "dump",
    "keylog",
    "payload",
    "malware"

]



def detect_suspicious_metadata(
        file_path,
        entropy
):

    path = Path(file_path)


    findings = []



    if path.name.startswith("."):

        findings.append(
            "Hidden file detected"
        )



    for ext in SUSPICIOUS_EXTENSIONS:

        if path.name.lower().endswith(ext):

            findings.append(
                f"Suspicious extension: {ext}"
            )



    filename = path.name.lower()


    for keyword in SUSPICIOUS_KEYWORDS:

        if keyword in filename:

            findings.append(
                f"Suspicious keyword: {keyword}"
            )



    if entropy >= 7:

        findings.append(
            "High entropy detected - possible packed/encrypted content"
        )



    return findings
