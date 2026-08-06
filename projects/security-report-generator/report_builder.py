"""
Security Report Builder

Builds professional Markdown security reports from JSON findings.
"""

from datetime import datetime


SEVERITY_ORDER = ["Critical", "High", "Medium", "Low", "Informational"]


def count_severity(findings):
    """
    Count findings by severity.
    """
    counts = {severity: 0 for severity in SEVERITY_ORDER}

    for finding in findings:
        severity = finding.get("severity", "Informational")
        if severity not in counts:
            severity = "Informational"

        counts[severity] += 1

    return counts


def generate_markdown(data):
    """
    Generate a professional Markdown security report.
    """
    findings = data.get("findings", [])
    summary = count_severity(findings)

    lines = []

    lines.append(f"# {data['report_title']}")
    lines.append("")

    lines.append("## Report Information")
    lines.append("")
    lines.append(f"- **Target:** {data['target']}")
    lines.append(f"- **Assessment Date:** {data['assessment_date']}")
    lines.append(
        f"- **Report Generated:** "
        f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )
    lines.append(f"- **Assessor:** {data['assessor']}")
    lines.append("")

    # Scope
    lines.append("## Scope")
    lines.append("")
    lines.append(f"- **Assessment Target:** {data['target']}")
    lines.append(f"- **Assessment Type:** {data['report_title']}")
    lines.append("- **Methodology:** Manual review and automated analysis")
    lines.append("")

    # Executive Summary
    lines.append("## Executive Summary")
    lines.append("")
    lines.append(
        f"This assessment identified **{len(findings)}** security finding(s)."
    )
    lines.append("")

    lines.append("| Severity | Count |")
    lines.append("|----------|------:|")

    for severity in SEVERITY_ORDER:
        lines.append(f"| {severity} | {summary[severity]} |")

    lines.append("")
    lines.append("## Findings")
    lines.append("")

    for index, finding in enumerate(findings, start=1):
        lines.append(f"### {index}. {finding['title']}")
        lines.append("")
        lines.append(f"**Severity:** {finding['severity']}")
        lines.append("")
        lines.append(f"**Description:** {finding['description']}")
        lines.append("")
        lines.append(
            f"**Recommendation:** {finding['recommendation']}"
        )
        lines.append("")

    # Conclusion
    lines.append("## Conclusion")
    lines.append("")

    if summary["Critical"] > 0:
        priority = "Critical"
    elif summary["High"] > 0:
        priority = "High"
    elif summary["Medium"] > 0:
        priority = "Medium"
    elif summary["Low"] > 0:
        priority = "Low"
    else:
        priority = "Informational"

    lines.append(
        f"The assessment identified **{len(findings)}** security finding(s)."
    )
    lines.append("")
    lines.append(
        f"Immediate remediation should prioritize **{priority}** severity findings."
    )
    lines.append("")
    lines.append(
        "Regular security assessments, vulnerability management, and "
        "continuous monitoring are recommended."
    )
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("*End of Report*")

    return "\n".join(lines)
