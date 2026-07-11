# Python Scripts

## Purpose

This directory contains reusable automation scripts for Python development within the FOOD project.

Scripts automate repetitive development tasks, improve code quality, support testing, validate project standards, and assist developers and AI agents throughout the software development lifecycle.

Project-specific Python standards are defined in:

../SKILL.md

Reference documentation is available in:

../references/

---

## Intended Use

Scripts in this directory may be used to:

- Create project modules
- Generate boilerplate code
- Validate project structure
- Verify coding standards
- Format source code
- Analyze static types
- Run unit tests
- Run integration tests
- Generate test coverage reports
- Validate dependencies
- Analyze code complexity
- Detect duplicated code
- Check documentation
- Generate project reports
- Prepare production releases

---

## Script Categories

Supported script categories include:

- Project Initialization
- Code Generation
- Code Formatting
- Static Analysis
- Type Checking
- Dependency Validation
- Code Quality
- Complexity Analysis
- Duplicate Code Detection
- Test Automation
- Coverage Reporting
- Documentation Generation
- Security Analysis
- Performance Analysis
- Production Verification

---

## Suggested Scripts

Examples:

```text
create-module.py
generate-code.py
format-code.py
lint.py
type-check.py
dependency-check.py
complexity-check.py
duplicate-check.py
run-tests.py
coverage-report.py
documentation-check.py
security-check.py
performance-check.py
production-check.py
```

---

## Naming Convention

Use descriptive lowercase filenames.

Examples:

```text
run-tests.py
type-check.py
dependency-check.py
```

Avoid:

```text
script.py
temp.py
new.py
test.py
python.py
```

---

## Script Requirements

Every script should:

- Perform one clearly defined task.
- Be reusable.
- Produce clear and readable output.
- Exit with appropriate status codes.
- Handle exceptions gracefully.
- Validate all input.
- Avoid hardcoded paths.
- Avoid hardcoded configuration values.
- Support automation.

---

## Output

Scripts should report:

- Start Time
- End Time
- Execution Duration
- Success Status
- Warning Summary
- Error Summary
- Recommendations

Use structured and readable output.

---

## Logging

Scripts should log:

- Executed Operations
- Warnings
- Errors
- Execution Time

Never log:

- Passwords
- Secrets
- Tokens
- API Keys
- Sensitive User Data

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
- Validate environment before execution.
- Produce deterministic results.
- Minimize external dependencies.
- Support CI/CD pipelines.
- Preserve project integrity.

---

## Production Rules

Production scripts must:

- Validate configuration.
- Verify dependencies.
- Run quality checks.
- Execute tests.
- Generate reports.
- Abort safely when validation fails.

---

## Notes

This directory contains executable automation scripts only.

Project-specific Python rules belong in:

../SKILL.md

Reference documentation belongs in:

../references/

Do not store:

- Documentation
- Configuration files
- Environment files
- Credentials
- Temporary files
- Application source code
- Generated reports

inside this directory.