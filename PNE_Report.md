3. Protection Needs Elicitation (PNE)
Overview
![alt text](image-1.png)


3.1 Introduction

Protection Needs Elicitation (PNE) refers to a systematic approach to systematically discovering the security needs of a system. Determining what needs to be protected, what threats to be considered, and what controls are required, PNE lays the security basis against which all further design decisions will be based. Instead of considering security as the post-implementation factor, PNE makes sure that an understanding of protection requirements are considered prior to the onset of implementation.

3.2 Asset Identification
The comprehensiveness of a security analysis can only be as complete as the comprehensiveness of the knowledge of that which is at stake. Critical assets that were identified in the system included:
Student information involves names and addresses, grades and school records. This data is highly-valued and has an obligation to academic-based data protection because of its sensitivity.
Authentication system deals with user credentials and restricts access using session management. Breach of this aspect means a gateway threat - vulnerability in this aspect will put the whole system on the table.
Administrative privileges allow one to change student records such as marks. There is a direct risk of data manipulation and academic fraud in case of unauthorized access to this privilege level.

3.3 Threat Identification
The system was tested on a structured threat model. The subsequent attack vectors were found to be pertinent to the assets mentioned above:
The risk of Insecure Direct Object References (IDOR) may permit unauthorized users to view records to which they should not have access to by altering the resource identifiers in the requests - such as a student altering an ID in the URL in order to view the marks of another user.
Cross-site Request Forgery (CSRF) is a risk of hackers when they lure authenticated users into unauthorizedly making a request that modulates the grades or accounts without their permission.
With clickjacking, the attackers can superimpose the open and fully transparent elements of the user interface with the application interface, and thus users can engage with the interface by reaching out to non-disclosed controls and every time run a privileged action unintentionally.
Privilege escalation is the vulnerability of the low-privileged user privilege (e.g. a student) to acquire administrative access either as a result of flaws in application logic, session vulnerabilities, or erroneous implementation of access controls.

3.4 Security Requirements

Based on the identified threats, the following security requirements were established:

Strong multi-factor authentication
Role-based access control (RBAC)
CSRF token validation on state-changing requests
Protection against CSRF attacks
Secure HTTP headers
Strict input validation and session integrity checks

3.5 Conclusion

The PNE process offered a systematic foundation to the comprehension of the security posture of the system. It helped make focused, defensible security choices, instead of generic hardening choices, by mapping assets to threats and threats to controls. The requirements made herein are traceable constraints during the system design and implementation.
