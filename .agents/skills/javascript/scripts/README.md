# JavaScript Scripts

## Purpose

This directory contains reusable automation scripts for JavaScript development within the FOOD project.

Scripts are intended to automate repetitive tasks, improve code quality, validate implementations, and support developers and AI agents throughout the development lifecycle.

Project-specific JavaScript standards are defined in:

../SKILL.md

Reference documentation is available in:

../references/

---

## Intended Use

Scripts in this directory may be used to:

- Validate JavaScript syntax
- Check code quality
- Detect unused code
- Verify browser compatibility
- Analyze performance
- Validate accessibility
- Validate DOM structure
- Verify event handling
- Analyze bundle size
- Prepare production builds

---

## Script Categories

Supported script categories include:

- Syntax Validation
- Linting
- Formatting
- Type Checking
- DOM Validation
- Accessibility Checks
- Performance Analysis
- Bundle Analysis
- Dependency Validation
- Security Checks
- Browser Compatibility
- Production Verification

---

## Suggested Scripts

Examples:

```text
lint.py
format.py
bundle-analysis.py
performance-check.py
dom-validator.py
accessibility-check.py
security-check.py
browser-check.py
dependency-check.py
production-check.py
```

---

## Naming Convention

Use descriptive lowercase filenames.

Examples:

```text
bundle-analysis.py
performance-check.py
browser-check.py
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

Project-specific JavaScript rules belong in:

../SKILL.md

Reference documentation belongs in:

../references/

Do not store documentation, configuration files, or application source code in this directory.