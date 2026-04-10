2. Dynamic Application Security Testing (DAST)

2.1 Introduction

Dynamic Application Security Testing (DAST) evaluates an application's security posture at runtime, without access to its source code. By interacting with the running application as an external attacker would, DAST surfaces vulnerabilities that only manifest during execution — such as improper access control enforcement, missing security headers, or broken session handling — which static analysis alone cannot detect.

In this project, DAST was conducted using OWASP ZAP (Zed Attack Proxy), an open-source web application scanner maintained by the OWASP Foundation. ZAP was configured to perform both automated scanning and targeted manual testing against the live application.


2.2 Identified Vulnerabilities (Before Remediation)
Testing revealed three exploitable vulnerabilities in the running application:

**Insecure Direct Object Reference (IDOR).** Authenticated users were able to access records belonging to other users by modifying resource identifiers in URL parameters. No server-side ownership check was performed to verify that the requesting user was entitled to the requested resource.

**Cross-Site Request Forgery (CSRF).** State-changing form submissions lacked anti-CSRF tokens, meaning an attacker could craft a malicious page that silently submits requests on behalf of an authenticated victim — for example, altering a student's grade without their knowledge.

**Clickjacking.** The application did not set framing-control HTTP headers, leaving it embeddable within a third-party iframe. This enabled UI redressing attacks, where a transparent overlay tricks users into interacting with the application unintentionally.



2.3 Remediation Measures Implemented
Each vulnerability was addressed with a targeted countermeasure:

| Vulnerability | Remediation | Mechanism |

| IDOR | Server-side authorization checks | Every request validates that the authenticated user owns or is permitted to access the requested resource, independent of what the URL parameter claims |

| CSRF | Synchronizer token pattern | All state-changing forms include a unique, session-bound CSRF token, validated server-side before any action is processed |

| Clickjacking | Anti-framing HTTP headers | `X-Frame-Options: DENY` and `Content-Security-Policy: frame-ancestors 'none'` were added to all responses, preventing the application from being embedded in external frames |


2.4 Conclusion

DAST testing successfully identified three exploitable vulnerabilities that were not apparent from static review alone. Following remediation, a re-scan with OWASP ZAP confirmed that all three attack vectors were closed, with no critical vulnerabilities detected in the application's runtime behaviour. The process demonstrates the value of runtime testing as a complement to code-level review — together, the two approaches provide substantially stronger assurance than either alone.

