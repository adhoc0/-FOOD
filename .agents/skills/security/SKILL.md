---
name: security
description: Secure coding standards, authentication, authorization, data protection, vulnerability prevention, and application security guidelines for the FOOD project.
---

# Security

## Purpose

This skill defines the security standards for the FOOD project.

All code must prioritize:

- Confidentiality
- Integrity
- Availability
- Privacy
- Reliability
- Compliance

Security is mandatory.

---

# General Principles

Always prioritize:

1. Secure by Default
2. Least Privilege
3. Defense in Depth
4. Fail Securely
5. Input Validation
6. Output Encoding

Never trust user input.

---

# Secure Development

Every feature must be reviewed for:

- Authentication
- Authorization
- Input Validation
- Output Encoding
- Data Exposure
- Logging
- Error Handling

---

# Authentication

Always require authentication where appropriate.

Use Django Authentication.

Never implement custom password hashing.

Require strong passwords.

Support secure password reset.

---

# Authorization

Verify permissions for every protected resource.

Never trust frontend authorization.

Validate permissions on every request.

Apply least privilege.

---

# User Roles

Separate user roles clearly.

Grant only required permissions.

Review permissions regularly.

Avoid excessive privileges.

---

# Password Security

Passwords must:

- Be hashed
- Never be logged
- Never be stored in plain text
- Never be exposed through APIs

Use strong password policies.

---

# Session Security

Protect user sessions.

Always:

- Expire inactive sessions
- Regenerate sessions after login
- Protect session cookies

Never expose session identifiers.

---

# CSRF Protection

Enable CSRF protection.

Never disable CSRF without justification.

Validate all state-changing requests.

---

# XSS Protection

Escape dynamic output.

Never trust HTML provided by users.

Avoid unsafe HTML rendering.

Sanitize user-generated content.

---

# SQL Injection

Always use Django ORM.

Avoid Raw SQL.

If Raw SQL is unavoidable:

- Use parameterized queries.
- Never concatenate SQL strings.

---

# Input Validation

Validate every external input.

Validate:

- Type
- Length
- Format
- Range
- Business Rules

Reject invalid input early.

---

# Output Encoding

Encode output according to context.

Protect against:

- HTML Injection
- JavaScript Injection
- Attribute Injection
- URL Injection

---

# File Upload Security

Validate uploaded files.

Verify:

- MIME Type
- Extension
- File Size
- Content

Never trust filenames.

Store uploads outside executable directories.

---

# API Security

Protect APIs using:

- Authentication
- Authorization
- Rate Limiting
- Validation

Never expose sensitive information.

---

# Secrets Management

Never commit:

- Passwords
- API Keys
- Secret Keys
- Tokens
- Certificates
- Private Keys

Use environment variables.

Rotate secrets regularly.

---

# Cryptography

Use trusted cryptographic libraries.

Never implement custom encryption.

Use secure random generators.

Protect encryption keys.

---

# HTTPS

Use HTTPS in production.

Redirect HTTP to HTTPS.

Protect cookies with:

- Secure
- HttpOnly
- SameSite

---

# Security Headers

Enable appropriate security headers.

Examples:

- CSP
- HSTS
- X-Frame-Options
- X-Content-Type-Options
- Referrer-Policy
- Permissions-Policy

---

# Logging

Log:

- Authentication failures
- Authorization failures
- Security events
- Unexpected exceptions

Never log:

- Passwords
- Tokens
- Secrets
- Session IDs
- Personal Data

---

# Error Handling

Never expose:

- Stack Traces
- Database Errors
- Internal Paths
- Sensitive Configuration

Return generic error messages.

Log detailed information internally.

---

# Rate Limiting

Protect against abuse.

Apply rate limits to:

- Login
- Registration
- Password Reset
- Search
- API Endpoints

---

# Dependency Security

Review dependencies regularly.

Remove unused packages.

Update vulnerable packages promptly.

Use trusted sources only.

---

# Database Security

Use dedicated database users.

Grant minimum privileges.

Protect database backups.

Encrypt sensitive data when appropriate.

---

# Docker Security

Run containers with least privilege.

Avoid running containers as root.

Keep images updated.

Scan images regularly.

---

# Nginx Security

Enable:

- HTTPS
- Security Headers
- Rate Limiting

Hide unnecessary server information.

---

# Monitoring

Monitor:

- Failed Logins
- Suspicious Activity
- Permission Violations
- Security Exceptions

Review security logs regularly.

---

# Incident Response

When a security issue is detected:

- Contain the issue.
- Preserve evidence.
- Notify responsible personnel.
- Verify recovery.
- Document the incident.

---

# FOOD Project Requirements

Protect:

- User Accounts
- Recipes
- Ratings
- Favorites
- Administrative Features
- Uploaded Images

Administrative functionality must always require authorization.

---

# Forbidden Practices

Never:

- Disable authentication
- Disable authorization
- Disable CSRF protection
- Store passwords in plain text
- Hardcode secrets
- Use eval() on user input
- Trust client-side validation
- Expose debug information
- Ignore security warnings
- Ignore dependency vulnerabilities

---

# Best Practices

Always:

- Validate input.
- Escape output.
- Protect secrets.
- Review permissions.
- Use HTTPS.
- Keep dependencies updated.
- Follow OWASP recommendations.
- Log security events.
- Perform regular security reviews.

---

# AI Guidelines

Before generating code:

- Validate all external input.
- Use Django ORM.
- Avoid insecure APIs.
- Protect sensitive data.
- Reuse existing security mechanisms.
- Respect authentication.
- Respect authorization.
- Avoid introducing vulnerabilities.
- Generate production-ready secure code.

---

# References

Additional security documentation is available in:

references/

Reusable automation scripts are available in:

scripts/

Project-specific rules always take precedence over general security best practices.