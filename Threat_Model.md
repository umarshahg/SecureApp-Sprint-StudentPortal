4. Threat Modeling (STRIDE Approach)
4.1 Introduction

Threat modeling is a proactive approach used to identify, analyze, and mitigate potential security threats in a system. In this project, the STRIDE model, developed by Microsoft, was used to categorize threats.

4.2 STRIDE Analysis
The table below maps each STRIDE category to its manifestation within this system, along with the mitigation applied or planned.

| Threat Category | Definition | System-Specific Example | Mitigation Status |
| **Spoofing** | Impersonating a legitimate user or component | Forged login attempts to gain unauthorized session access | Implemented — authentication system with session validation |
| **Tampering** | Unauthorized modification of data in transit or at rest | Direct manipulation of student marks via unprotected requests | Implemented — RBAC enforcement and input validation |
| **Repudiation** | Denying that an action was performed, with no means to disprove it | A user altering records with no audit trail to attribute the change | Partially addressed — activity logging identified as future work |
| **Information Disclosure** | Exposure of sensitive data to unauthorized parties | IDOR vulnerability allowing access to other students' records | Implemented — server-side authorization checks on all resource access |
| **Denial of Service** | Disrupting availability of the system or its resources | Excessive requests causing server overload and outage | Not yet implemented — rate limiting and throttling identified as future work |
| **Elevation of Privilege** | Gaining access rights beyond those that were granted | A student-level account performing administrative actions | Implemented — strict role validation and privilege boundary enforcement |


4.3 Mitigation Strategy

Mitigations were applied at multiple layers of the application stack to address the threats identified above. Where a control was already in place, it was verified against the relevant STRIDE category. Where a gap was identified — specifically for Repudiation and Denial of Service — remediation has been deferred and recorded as planned future work.

The core controls implemented are:

- **Authentication and session management** — counters Spoofing by ensuring that only verified identities can establish sessions.
- **Role-based access control (RBAC)** — counters Tampering and Elevation of Privilege by enforcing least-privilege boundaries across all user roles.
- **Server-side authorization checks** — counters Information Disclosure by validating resource ownership on every request, regardless of client-supplied parameters.
- **Secure HTTP headers** — counters Clickjacking and related UI-layer attacks through `X-Frame-Options` and `Content-Security-Policy` directives.
- **Input validation** — counters Tampering by rejecting malformed or unexpected data before it reaches application logic or the database.



4.4 Conclusion

Applying the STRIDE framework provided a structured and exhaustive basis for threat identification, ensuring that no broad class of attack was overlooked. By grounding each threat category in a concrete system example and mapping it to a specific control, the analysis produced actionable security decisions rather than abstract risk statements. The two open risks identified — Repudiation and Denial of Service — are documented and prioritized for remediation, ensuring the system's security posture continues to improve beyond the current implementation phase.
