# Scripts
Bu klasör yardımcı scriptleri içerir.
# Django Scripts

## Purpose

This directory contains reusable automation scripts for Django development within the FOOD project.

Scripts are intended to automate repetitive tasks, improve consistency, and support AI agents and developers during development, testing, and deployment.

Project-specific Django development rules are defined in:

../SKILL.md

Reference documentation is available in:

../references/

---

## Intended Use

Scripts in this directory may be used to:

- Create Django applications
- Generate project boilerplate
- Validate project structure
- Run quality assurance checks
- Execute database maintenance tasks
- Verify coding standards
- Automate testing
- Prepare production releases

---

## Script Categories

Supported script categories include:

- Project Initialization
- App Creation
- Model Generation
- Migration Automation
- Fixture Management
- Static File Management
- Media Cleanup
- Test Automation
- Code Formatting
- Linting
- Type Checking
- Security Checks
- Performance Analysis
- Deployment Preparation

---

## Suggested Scripts

Examples:

```text
create-app.py
create-model.py
run-tests.py
check-project.py
collect-static.py
cleanup-media.py
verify-migrations.py
load-fixtures.py
security-check.py
performance-check.py
release-check.py
```

---

## Naming Convention

Use descriptive lowercase filenames.

Examples:

```text
create-app.py
verify-migrations.py
run-tests.py
```

Avoid:

```text
script.py
new.py
temp.py
test.py
```

---

## Script Requirements

Every script should:

- Perform one specific task.
- Be reusable.
- Be documented.
- Exit with appropriate status codes.
- Produce clear output.
- Handle errors gracefully.
- Avoid hardcoded project paths.

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
- Be safe to execute multiple times.

---

## Notes

This directory contains executable automation only.

Project rules belong in:

../SKILL.md

Reference documentation belongs in:

../references/

Do not store documentation or configuration files in this directory.