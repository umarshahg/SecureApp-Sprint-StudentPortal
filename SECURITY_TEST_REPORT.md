## DAST Testing (OWASP ZAP)

Dynamic Application Security Testing was performed using OWASP ZAP.

### Before Fix:
- IDOR vulnerability detected
- CSRF vulnerability detected
- Clickjacking possible

### After Fix:
- IDOR blocked (403 response)
- CSRF attacks prevented using tokens
- Clickjacking mitigated via X-Frame-Options and CSP

No critical vulnerabilities remain.
