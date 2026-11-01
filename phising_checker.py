"""EWB Phishing URL Awareness Checker.

Educational, defensive tool. It only reads URL TEXT.
It never opens a URL, scans a website or sends data anywhere.
"""

import re
from urllib.parse import urlparse

# Improvement D: a plain-language reason for every warning.
REASONS = {
    "Contains an @ symbol; inspect carefully.":
        "The browser ignores text before @, so the link can look like one site but go to another.",
    "Unusually long URL (over 100 characters).":
        "Long links can hide the real destination far to the right.",
    "Uses an IP address instead of a familiar domain.":
        "Real brands normally use names, not number addresses.",
    "Contains many hostname segments/subdomains.":
        "Stacking many names (a.b.c.d.e) can make a link look official.",
    "Contains a punycode-style hostname.":
        "Punycode (xn--) can hide look-alike foreign letters that mimic real names.",
    "Uses HTTP. HTTPS alone does not prove trust.":
        "HTTP is not encrypted, so data can be seen on the way.",
}

# Messages that are information, not real warnings.
INFO_MESSAGES = (
    "No URL entered",
    "Could not identify",
    "This text is not a valid URL",
    "No listed warning",
)


def inspect_url(raw_url):
    """Check visible URL text for selected warning signs. Returns a list of messages."""
    url = raw_url.strip()
    findings = []

    if not url:
        return ["No URL entered."]

    candidate = url if "://" in url else "http://" + url

    # Improvement C: malformed input (e.g. "http://[bad") must not crash.
    try:
        parsed = urlparse(candidate)
        host = (parsed.hostname or "").lower()
    except ValueError:
        return ["This text is not a valid URL format."]

    if not host:
        return ["Could not identify a hostname."]

    # Check 1: @ symbol
    if "@" in candidate:
        findings.append("Contains an @ symbol; inspect carefully.")

    # Check 2: very long URL
    if len(url) > 100:
        findings.append("Unusually long URL (over 100 characters).")

    # Check 3: IP address hostname
    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append("Uses an IP address instead of a familiar domain.")

    # Check 4: many hostname segments
    labels = [part for part in host.split(".") if part]
    if len(labels) >= 5:
        findings.append("Contains many hostname segments/subdomains.")

    # Check 5: punycode marker
    if "xn--" in host:
        findings.append("Contains a punycode-style hostname.")

    # Check 6: HTTP scheme
    if parsed.scheme.lower() == "http":
        findings.append("Uses HTTP. HTTPS alone does not prove trust.")

    if not findings:
        findings.append("No listed warning signs found. This does NOT prove safety.")

    return findings


def has_warnings(findings):
    """Improvement B helper: True only if the list holds real warnings."""
    return not findings[0].startswith(INFO_MESSAGES)


def main():
    print("EWB Phishing URL Awareness Checker")
    print("Text checks only - this program does not open URLs.")

    # Improvement A: loop until the user quits.
    while True:
        raw_url = input("\nEnter a sample URL (or type q to quit): ")
        if raw_url.strip().lower() in ("q", "quit", "exit"):
            print("Goodbye! Stay alert online.")
            break

        findings = inspect_url(raw_url)
        print("\nResult:")
        for number, item in enumerate(findings, start=1):  # Improvement E: numbered output
            print(f"{number}. {item}")
            reason = REASONS.get(item)
            if reason:
                print(f"   Why it matters: {reason}")

        if has_warnings(findings):
            print(f"\nREVIEW CAREFULLY: {len(findings)} warning sign(s) found.")
        print("Never enter passwords from unexpected links.")


if __name__ == "__main__":
    main()