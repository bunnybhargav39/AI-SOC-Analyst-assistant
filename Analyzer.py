def analyze_log(log):

    log = str(log).lower()

    if "failed password" in log:
        return {
            "severity": "Medium",
            "reason": "Failed login attempt detected"
        }

    elif "malicious" in log:
        return {
            "severity": "High",
            "reason": "Malicious activity detected"
        }

    elif "deny" in log:
        return {
            "severity": "Medium",
            "reason": "Traffic was blocked"
        }

    else:
        return {
            "severity": "Low",
            "reason": "No obvious threat detected"
        }
