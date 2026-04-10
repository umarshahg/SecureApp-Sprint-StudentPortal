4. Threat Modeling (STRIDE Approach)
4.1 Introduction

Threat modeling is a proactive approach used to identify, analyze, and mitigate potential security threats in a system. In this project, the STRIDE model, developed by Microsoft, was used to categorize threats.

4.2 STRIDE Analysis
Threat Category	Description	Example in System	Mitigation
Spoofing	Impersonation of users	Fake login attempts	Authentication system
Tampering	Unauthorized data modification	Changing student marks	RBAC enforcement
Repudiation	Denial of actions	No activity logs	Logging (future work)
Information Disclosure	Exposure of sensitive data	IDOR vulnerability	Authorization checks
Denial of Service	Service disruption	Server overload	Not implemented
Elevation of Privilege	Gaining higher access rights	Student acting as admin	Role validation
4.3 Mitigation Strategy

Each identified threat was addressed using appropriate controls such as authentication, authorization, input validation, and secure headers. The implementation ensures that the system is resilient against common web-based attacks.

4.4 Conclusion

Threat modeling using STRIDE enabled systematic identification and mitigation of security risks, ensuring a robust and secure application design.
