3. Protection Needs Elicitation (PNE)

3.1 Introduction

Protection Needs Elicitation (PNE) is a systematic process used to identify critical assets, potential threats, and necessary security requirements. It serves as the foundation for designing a secure system by understanding what needs to be protected and why.

///////////////////////////////

3.2 Asset Identification

The following key assets were identified in the system:

Student Data: Includes names, marks, and academic records.
Authentication System: Handles user login credentials and session management.
Administrative Privileges: Allows modification of sensitive data such as student marks.

///////////////////////////////

3.3 Threat Identification

The system was evaluated for potential threats, including:

Unauthorized access to sensitive data (IDOR)
Forged requests (CSRF)
User interface manipulation (Clickjacking)
Privilege escalation (students gaining admin rights)

///////////////////////////////

3.4 Security Requirements

Based on the identified threats, the following security requirements were established:

Implementation of strong authentication mechanisms
Enforcement of role-based access control
Protection against CSRF attacks
Use of secure HTTP headers
Input validation and session security

///////////////////////////////

3.5 Conclusion

PNE provided a structured approach to identifying security needs and guided the implementation of appropriate countermeasures to protect system assets effectively.
