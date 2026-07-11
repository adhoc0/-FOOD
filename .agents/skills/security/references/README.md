# Security References

## Purpose

This directory contains reference documentation for application security, secure coding practices, authentication, authorization, encryption, vulnerability prevention, and infrastructure security used in the FOOD project.

These documents provide implementation guidance, security standards, attack prevention techniques, and best practices for developers and AI agents.

Project-specific security rules are defined in:

../SKILL.md

---

## Scope

Reference documents may cover topics such as:

- Secure Coding
- OWASP Top 10
- Authentication
- Authorization
- Role-Based Access Control (RBAC)
- Permission Management
- Password Security
- Session Management
- CSRF Protection
- XSS Prevention
- SQL Injection Prevention
- Command Injection Prevention
- File Upload Security
- Input Validation
- Output Encoding
- Cryptography
- HTTPS
- Security Headers
- Secrets Management
- API Security
- Logging and Auditing
- Security Monitoring
- Incident Response

---

## Intended Use

Reference documents should help:

- Explain security concepts.
- Provide secure implementation examples.
- Document defensive programming techniques.
- Support AI-assisted secure development.
- Reduce duplicated knowledge.
- Improve application security posture.

---

## Suggested Documents

Examples:

```text
owasp-top10.md
authentication.md
authorization.md
rbac.md
permissions.md
password-security.md
session-management.md
csrf.md
xss.md
sql-injection.md
command-injection.md
file-upload-security.md
input-validation.md
output-encoding.md
cryptography.md
security-headers.md
https.md
api-security.md
logging.md
incident-response.md
```

---

## File Naming

Use descriptive lowercase filenames.

Examples:

```text
input-validation.md
file-upload-security.md
password-security.md
```

Avoid:

```text
notes.md
temp.md
misc.md
new.md
security.md
```

---

## Guidelines

Reference documents should:

- Focus on a single security topic.
- Be security-specific.
- Be concise and practical.
- Avoid duplicate information.
- Reference official OWASP, NIST, Django, PostgreSQL, and Python documentation whenever appropriate.
- Include secure implementation examples when useful.
- Be reviewed regularly as security standards evolve.

---

## Notes

Do not place project rules in this directory.

Project-specific security standards belong in:

../SKILL.md

Reusable automation belongs in:

../scripts/

Only reference documentation should be stored in this directory.