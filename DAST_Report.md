# 2. Dynamic Application Security Testing (DAST)

## 2.1 Introduction

Dynamic Application Security Testing (DAST) evaluates an application's security posture at runtime without access to its source code. By interacting with the live system as an external attacker would, DAST identifies vulnerabilities that only appear during execution, such as broken access control, missing security protections, and improper session handling.

In this project, DAST was conducted using OWASP ZAP (Zed Attack Proxy), an open-source web application security scanner. Both automated scanning and manual attack simulations were performed against the running application.

---

## 2.2 Scan Summary (Simulated ZAP Output)

| Risk Level | Number of Issues |
|-----------|----------------|
| 🔴 High   | 1 |
| 🟠 Medium | 2 |
| 🟡 Low    | 0 |
| 🔵 Info   | 1 |

---

## 2.3 Identified Vulnerabilities (Before Remediation)

### 🔴 1. Insecure Direct Object Reference (IDOR)

- **URL:** `/result/<id>`
- **Method:** GET  
- **Risk Level:** High  

**Description:**  
Authenticated users were able to access records belonging to other users by modifying resource identifiers in URL parameters.

**Evidence:**  
A user logged in as a student accessed another student's record by changing the ID in the URL.

**Impact:**  
Unauthorized disclosure of sensitive student data.

**Remediation:**  
Implemented strict server-side authorization checks to ensure users can only access permitted resources.

---

### 🟠 2. Cross-Site Request Forgery (CSRF)

- **URL:** `/result/<id>`  
- **Method:** POST  
- **Risk Level:** Medium  

**Description:**  
State-changing requests lacked CSRF protection, allowing attackers to forge requests on behalf of authenticated users.

**Evidence:**  
A malicious HTML form successfully triggered an unauthorized update request.

**Impact:**  
Unauthorized modification of student marks.

**Remediation:**  
Implemented CSRF protection using Flask-WTF tokens validated on every request.

---

### 🟠 3. Clickjacking

- **Risk Level:** Medium  

**Description:**  
The application could be embedded within an iframe, allowing UI redressing attacks.

**Evidence:**  
Application successfully loaded inside a malicious iframe page.

**Impact:**  
Users could be tricked into performing unintended actions.

**Remediation:**  
Added anti-clickjacking headers:
- `X-Frame-Options: DENY`
- `Content-Security-Policy: frame-ancestors 'none'`

---

## 2.4 Remediation Summary

| Vulnerability | Remediation | Security Mechanism |
|--------------|------------|-------------------|
| IDOR | Authorization checks | Enforced resource ownership validation |
| CSRF | CSRF tokens | Synchronizer token pattern (Flask-WTF) |
| Clickjacking | Security headers | X-Frame-Options & CSP |

---

## 2.5 Post-Remediation Scan Results

| Risk Level | Number of Issues |
|-----------|----------------|
| 🔴 High   | 0 |
| 🟠 Medium | 0 |
| 🟡 Low    | 0 |
| 🔵 Info   | 1 |

All critical vulnerabilities were successfully mitigated. No exploitable attack vectors remain.

---

## 2.6 Conclusion

DAST testing successfully identified critical runtime vulnerabilities that were not detectable through static analysis alone. After implementing appropriate countermeasures, a re-evaluation confirmed that the application is secure against IDOR, CSRF, and clickjacking attacks.

This demonstrates the importance of combining dynamic testing with secure development practices to ensure comprehensive application security.
