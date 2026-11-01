Test Samples — Phishing URL Awareness Checker

Test 1

Input: "https://www.example.com/login"

Expected result: No listed warning signs found.

Observed result: 
Status: [PASS or FAIL]

Test 2

Input: "http://example.com@sample.invalid/login"

Expected result: Warning about the @ symbol and HTTP.

Observed result: [Write what your program displayed.]

Status: [PASS or FAIL]

Test 3

Input: "http://192.0.2.10/account"

Expected result: Warning about an IP address and HTTP.

Observed result: [Write what your program displayed.]

Status: [PASS or FAIL]

Test 4

Input: "https://a.b.c.d.e.example.invalid/path"

Expected result: Warning about many hostname segments/subdomains.

Observed result: [Write what your program displayed.]

Status: [PASS or FAIL]

Test 5

Input: "https://xn--example.invalid/"

Expected result: Warning about a punycode-style hostname.

Observed result: [Write what your program displayed.]

Status: [PASS or FAIL]

Conclusion

The program checks website addresses for selected warning signs. It does not prove that a website is safe or unsafe.