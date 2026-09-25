import re


def analyze_log(log_text: str):
    """
    Analyze application/server logs and detect
    errors, warnings and important events.
    """

    if not log_text:
        return {
            "status": "empty",
            "message": "No log content provided",
            "errors": [],
            "warnings": [],
            "info": []
        }

    errors = []
    warnings = []
    info = []

    # Split log into individual lines
    lines = log_text.splitlines()

    for line in lines:
        line = line.strip()

        if not line:
            continue

        line_lower = line.lower()

        # Detect errors
        if (
            "error" in line_lower
            or "exception" in line_lower
            or "failed" in line_lower
            or "failure" in line_lower
            or "traceback" in line_lower
        ):
            errors.append(line)

        # Detect warnings
        elif (
            "warning" in line_lower
            or "warn" in line_lower
        ):
            warnings.append(line)

        # Detect informational logs
        elif (
            "info" in line_lower
            or "started" in line_lower
            or "success" in line_lower
            or "completed" in line_lower
        ):
            info.append(line)

    # Determine overall status
    if errors:
        status = "error"
    elif warnings:
        status = "warning"
    else:
        status = "success"

    return {
        "status": status,
        "total_lines": len(lines),
        "error_count": len(errors),
        "warning_count": len(warnings),
        "info_count": len(info),
        "errors": errors,
        "warnings": warnings,
        "info": info
    }


def extract_error_messages(log_text: str):
    """
    Extract only error-related lines from logs.
    """

    result = analyze_log(log_text)

    return result["errors"]


def generate_summary(log_text: str):
    """
    Generate a simple summary of the log analysis.
    """

    result = analyze_log(log_text)

    if result["status"] == "error":
        return (
            f"Log analysis completed. "
            f"Found {result['error_count']} error(s) "
            f"and {result['warning_count']} warning(s)."
        )

    elif result["status"] == "warning":
        return (
            f"Log analysis completed. "
            f"No critical errors found, but "
            f"{result['warning_count']} warning(s) detected."
        )

    else:
        return "Log analysis completed successfully. No errors or warnings found."