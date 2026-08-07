"""
Behavior detection rules for Endpoint Detection & Response Simulator.
"""


SUSPICIOUS_PROCESSES = [
    "powershell.exe",
    "cmd.exe",
    "wscript.exe",
    "cscript.exe",
    "mshta.exe",
    "regsvr32.exe",
]


SUSPICIOUS_COMMANDS = [
    "encodedcommand",
    "-enc",
    "downloadstring",
    "invoke-expression",
    "iex",
    "certutil",
    "bitsadmin",
]


SUSPICIOUS_EXTENSIONS = [
    ".exe",
    ".dll",
    ".ps1",
    ".vbs",
    ".bat",
    ".cmd",
]


SUSPICIOUS_NETWORK_PORTS = [
    4444,
    5555,
    6666,
    8080,
    31337,
]


def is_suspicious_process(
    process_name
):
    """
    Check suspicious process names.

    Args:
        process_name (str)

    Returns:
        bool
    """

    return (
        process_name.lower()
        in SUSPICIOUS_PROCESSES
    )


def contains_suspicious_command(
    command
):
    """
    Detect suspicious command patterns.

    Args:
        command (str)

    Returns:
        bool
    """

    command = command.lower()

    for keyword in SUSPICIOUS_COMMANDS:

        if keyword in command:

            return True

    return False


def is_suspicious_extension(
    filename
):
    """
    Check suspicious file extensions.

    Args:
        filename (str)

    Returns:
        bool
    """

    filename = filename.lower()

    for extension in SUSPICIOUS_EXTENSIONS:

        if filename.endswith(
            extension
        ):

            return True

    return False


def is_suspicious_port(
    port
):
    """
    Check suspicious network ports.

    Args:
        port (int)

    Returns:
        bool
    """

    return port in SUSPICIOUS_NETWORK_PORTS
