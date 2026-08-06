"""
Output formatting module.

Creates readable SOC reports.
"""


def create_console_report(
    ioc,
    ioc_type,
    vt_data,
    abuse_data,
    risk_data
):
    """
    Create terminal-friendly report.
    """

    lines = []

    lines.append("=" * 50)
    lines.append("SOC Analysis Report")
    lines.append("=" * 50)

    lines.append("")

    lines.append(
        f"IOC      : {ioc}"
    )

    lines.append(
        f"Type     : {ioc_type}"
    )

    lines.append("")

    lines.append(
        f"Risk     : {risk_data['risk']}"
    )

    lines.append(
        f"Score    : {risk_data['score']}"
    )

    lines.append("")

    lines.append(
        "Threat Intelligence"
    )

    lines.append("-" * 30)

    lines.append(
        f"VirusTotal Malicious : "
        f"{vt_data.get('malicious', 0)}"
    )

    lines.append(
        f"VirusTotal Suspicious: "
        f"{vt_data.get('suspicious', 0)}"
    )

    lines.append(
        f"Abuse Score          : "
        f"{abuse_data.get('abuse_score', 0)}%"
    )

    lines.append("")

    lines.append(
        "Risk Factors"
    )

    lines.append("-" * 30)

    if risk_data["reasons"]:

        for reason in risk_data["reasons"]:
            lines.append(
                f"- {reason}"
            )

    else:
        lines.append(
            "- No threat indicators detected"
        )

    lines.append("")

    lines.append("=" * 50)

    return "\n".join(lines)



def create_json_report(data):
    """
    Prepare JSON-compatible output.
    """

    return data
