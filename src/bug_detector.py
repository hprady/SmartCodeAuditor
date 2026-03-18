def detect_bugs(code):

    bugs = []

    if "eval(" in code:
        bugs.append({
            "bug": "Unsafe eval usage",
            "severity": "Critical"
        })

    if "except:" in code:
        bugs.append({
            "bug": "Bare except block",
            "severity": "Major"
        })

    return bugs