# Nginx Scripts

## Purpose

This directory contains reusable automation scripts for Nginx configuration, validation, optimization, testing, and deployment within the FOOD project.

Scripts are intended to automate repetitive infrastructure tasks, improve deployment consistency, and support developers and AI agents.

Project-specific Nginx standards are defined in:

../SKILL.md

Reference documentation is available in:

../references/

---

## Intended Use

Scripts in this directory may be used to:

- Validate Nginx configuration
- Test virtual hosts
- Verify SSL/TLS configuration
- Generate Nginx configuration files
- Reload Nginx safely
- Analyze access logs
- Analyze error logs
- Verify reverse proxy configuration
- Validate security headers
- Test compression settings
- Prepare production deployments
- Verify containerized deployments

---

## Script Categories

Supported script categories include:

- Configuration Validation
- Configuration Generation
- SSL Verification
- Security Checks
- Performance Analysis
- Compression Validation
- Log Analysis
- Reverse Proxy Verification
- Docker Integration
- Health Checks
- Deployment Automation
- Production Verification

---

## Suggested Scripts

Examples:

```text
check-config.py
generate-config.py
ssl-check.py
security-check.py
performance-check.py
gzip-check.py
brotli-check.py
log-analyzer.py
proxy-validator.py
health-check.py
reload-nginx.py
production-check.py
```

---

## Naming Convention

Use descriptive lowercase filenames.

Examples:

```text
check-config.py
ssl-check.py
proxy-validator.py
```

Avoid:

```text
script.py
temp.py
new.py
test.py
```

---

## Script Requirements

Every script should:

- Perform one specific task.
- Be reusable.
- Produce readable output.
- Exit with appropriate status codes.
- Handle errors gracefully.
- Avoid hardcoded paths.
- Support automation.

---

## Cross-Platform Support

Whenever possible, support multiple operating systems.

Preferred languages:

- Python
- Bash (.sh)
- PowerShell (.ps1)

Avoid operating system specific assumptions.

---

## Guidelines

Scripts should:

- Follow project coding standards.
- Be idempotent whenever possible.
- Validate input before execution.
- Log meaningful errors.
- Minimize external dependencies.
- Produce consistent output.
- Be suitable for CI/CD pipelines.

---

## Notes

This directory contains executable automation scripts only.

Project-specific Nginx rules belong in:

../SKILL.md

Reference documentation belongs in:

../references/

Do not store documentation, configuration files, certificates, private keys, or application source code in this directory.