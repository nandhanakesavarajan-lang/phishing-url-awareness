# EWB Phishing URL Awareness Checker

## Overview
Phishing is a trick where fake links or messages try to make people share passwords, card numbers or OTPs. This command-line tool reads the text of a URL and lists visible warning signs. It never visits the link.

## Features
- Detects an @ symbol in the URL
- Flags unusually long URLs (over 100 characters)
- Flags IP-address hostnames
- Flags many hostname segments (5 or more)
- Flags punycode-style hostnames (xn--)
- Flags the HTTP scheme
- Loop mode: check many URLs, type q to quit
- "REVIEW CAREFULLY" summary with a warning count
- Safe handling of malformed input (no crashes)
- A plain-language "Why it matters" line under each warning
- Numbered output

## Requirements
Python 3.10 or later. No extra packages.

## How to Run
Windows: `python phishing_checker.py`
Mac/Linux: `python3 phishing_checker.py`

## Example Output
```
Enter a sample URL (or type q to quit): http://192.0.2.10/account

Result:
1. Uses an IP address instead of a familiar domain.
   Why it matters: Real brands normally use names, not number addresses.
2. Uses HTTP. HTTPS alone does not prove trust.
   Why it matters: HTTP is not encrypted, so data can be seen on the way.

REVIEW CAREFULLY: 2 warning sign(s) found.
Never enter passwords from unexpected links.
```

## Testing
| # | Input | Expected | Actual | Result |
|---|-------|----------|--------|--------|
| 1 | https://www.example.com/login | No warning signs | No listed warning signs found | PASS |
| 2 | http://192.0.2.10/account | IP + HTTP | IP address, HTTP | PASS |
| 3 | http://example.com@sample.invalid/login | @ + HTTP | @ symbol, HTTP | PASS |
| 4 | https://a.b.c.d.e.example.invalid/path | Many segments | Many hostname segments | PASS |
| 5 | https://xn--example.invalid/ | Punycode | Punycode-style hostname | PASS |

Full table: `tests/test_samples.md`. Automated tests: `python tests/test_phishing_checker.py`.

## Screenshots
![Sample run](screenshots/![alt text](<Screenshot 2026-10-29 205659.png>) ![alt text](<Screenshot 2026-10-29 205724.png>) ![alt text](<Screenshot 2026-10-29 205740.png>) ![alt text](<Screenshot 2026-10-29 205801.png>) ![alt text](<Screenshot 2026-10-29 213503.png>))
![Test results](screenshots/![alt text](<Screenshot 2026-11-01 082835.png>) ![alt text](<Screenshot 2026-11-01 082854.png>) ![alt text](<Screenshot 2026-11-01 082910.png>) ![alt text](<Screenshot 2026-11-01 082929.png>) ![alt text](<Screenshot 2026-11-01 083036.png>)

## Improvements
1. Loop with quit - the program repeats until q, so I can test many URLs without restarting. Tested by entering several URLs, then q.
2. Review-carefully summary and malformed-input handling - a helper `has_warnings()` prints a count of warnings, and try/except stops `http://[bad` from crashing. Re-ran all five tests after the change.
3. Explanations - a dictionary maps each warning to a simple reason.

## Limitations
This is an educational tool. It only reads URL text. It does not visit URLs, scan for malware or prove that a URL is safe. No warning signs found does NOT mean a URL is safe.

## Ethical Use
Use sample strings only. Do not collect credentials. Do not use this project to deceive anyone or to test websites without permission.

## Author
Nandhana K, AI Powered Cybersecurity Internship , EWB Courses
