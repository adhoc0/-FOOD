# Security Scripts

## Purpose

This directory contains reusable automation scripts for application security validation, vulnerability detection, configuration auditing, secret scanning, and production security verification within the FOOD project.

Scripts automate repetitive security tasks, reduce human error, improve consistency, and support developers and AI agents throughout the software development lifecycle.

Project-specific security standards are defined in:

../SKILL.md

Reference documentation is available in:

../references/

---

## Intended Use

Scripts in this directory may be used to:

- Scan source code for security issues
- Detect hardcoded secrets
- Validate environment configuration
- Verify HTTPS configuration
- Check security headers
- Analyze dependency vulnerabilities
- Verify authentication configuration
- Verify authorization rules
- Validate file upload security
- Detect insecure permissions
- Validate password policies
- Analyze session configuration
- Verify CSRF protection
- Verify Content Security Policy
- Generate security reports
- Prepare production security audits

---

## Script Categories

Supported script categories include:

- Static Security Analysis
- Secret Scanning
- Dependency Auditing
- Authentication Validation
- Authorization Validation
- Session Validation
- CSRF Validation
- Security Header Validation
- HTTPS Verification
- File Upload Validation
- Permission Auditing
- Configuration Validation
- Vulnerability Scanning
- Production Security Verification

---

## Suggested Scripts

Examples:

```text
secret-scan.py
dependency-audit.py
security-audit.py
authentication-check.py
authorization-check.py
permission-check.py
csrf-check.py
headers-check.py
https-check.py
session-check.py
password-policy.py
upload-security.py
configuration-check.py
vulnerability-scan.py
production-security.py
```

---

## Naming Convention

Use descriptive lowercase filenames.

Examples:

```text
secret-scan.py
dependency-audit.py
csrf-check.py
```

Avoid:

```text
script.py
temp.py
new.py
security.py
```

---

## Script Requirements

Every script should:

- Perform one clearly defined task.
- Be reusable.
- Produce structured and readable output.
- Exit with appropriate status codes.
- Handle exceptions gracefully.
- Validate input before execution.
- Avoid hardcoded credentials.
- Support automation.

---

## Output

Scripts should report:

- Start Time
- End Time
- Execution Duration
- Security Status
- Warnings
- Critical Findings
- Recommendations

Output should be deterministic and machine-readable whenever possible.

---

## Logging

Scripts should log:

- Executed Checks
- Warnings
- Errors
- Execution Duration

Never log:

- Passwords
- API Keys
- Tokens
- Secrets
- Session Identifiers
- Private Keys
- Personal Data

---

## Cross-Platform Support

Whenever possible, support:

- Python
- Bash (.sh)
- PowerShell (.ps1)

Avoid operating system-specific assumptions.

---

## Guidelines

Scripts should:

- Follow project coding standards.
- Be idempotent whenever possible.
- Validate the environment before execution.
- Produce deterministic results.
- Minimize external dependencies.
- Support CI/CD pipelines.
- Preserve system integrity.

---

## Production Rules

Production security scripts must:

- Verify HTTPS configuration.
- Verify security headers.
- Verify secret management.
- Verify authentication.
- Verify authorization.
- Verify dependency security.
- Verify environment configuration.
- Abort safely when critical vulnerabilities are detected.

---

## Notes

This directory contains executable automation scripts only.

Project-specific security rules belong in:

../SKILL.md

Reference documentation belongs in:

../references/

Do not store:

- Credentials
- Secrets
- API Keys
- Private Keys
- Certificates
- Environment files
- Security reports
- Documentation
- Application source code

inside this directory.