2. Dynamic Application Security Testing (DAST)

2.1 Introduction

Dynamic Application Security Testing (DAST) evaluates the security of an application during runtime. Unlike SAST, it does not require access to the source code and instead interacts with the application as an external user would. This approach helps identify vulnerabilities that occur during execution.

In this project, DAST testing was conducted using OWASP ZAP, a widely used open-source web application security scanner.

//////////////////////////////////////////////////

2.2 Identified Vulnerabilities (Before Remediation)
IDOR Vulnerability: Users could access unauthorized records by modifying URL parameters.
CSRF Vulnerability: Forms lacked protection against forged requests.
Clickjacking Risk: The application could be embedded within malicious iframes.

//////////////////////////////////////////////////

2.3 Remediation Measures Implemented
Implemented authorization checks to restrict access to authorized users only.
Enabled CSRF tokens for all sensitive form submissions.
Added anti-clickjacking headers to prevent UI redressing attacks.

//////////////////////////////////////////////////

2.4 Conclusion

DAST confirmed that the application is secure against real-world attack scenarios. After remediation, no critical vulnerabilities were observed during runtime testing.
