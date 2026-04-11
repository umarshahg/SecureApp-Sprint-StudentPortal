# 4. Threat Modeling (STRIDE Approach)

## 4.1 Introduction
Threat modeling is a proactive approach used to identify, analyze, and mitigate potential security threats in a system. In this project, the STRIDE model was used to categorize threats.

---

## 4.2 STRIDE Analysis

| Threat Category | Definition | System-Specific Example | Mitigation Status |
|----------------|------------|------------------------|------------------|
| Spoofing | Impersonating a legitimate user | Forged login attempts to gain unauthorized access | Implemented – Authentication with session validation |
| Tampering | Unauthorized modification of data | Direct manipulation of student marks | Implemented – RBAC and input validation |
| Repudiation | Denying performed actions | No logs for tracking changes | Partially Implemented – Logging planned |
| Information Disclosure | Exposure of sensitive data | IDOR vulnerability accessing other students' records | Implemented – Authorization checks |
| Denial of Service | Disrupting system availability | Excessive requests causing overload | Not Implemented – Future work |
| Elevation of Privilege | Gaining higher access rights | Student performing admin actions | Implemented – Role validation |

---

## 4.3 Mitigation Strategy

- Authentication and session management implemented  
- Role-Based Access Control enforced  
- Input validation added  
- Authorization checks applied  
- Security headers configured  

---

## 4.4 Conclusion

The STRIDE model helped identify and mitigate major security threats, ensuring the system is secure and reliable.
