# Testing Scripts

## Purpose

This directory contains reusable automation scripts for software testing, validation, quality assurance, coverage analysis, and release verification within the FOOD project.

Scripts automate repetitive testing tasks, improve software quality, reduce human error, and support developers and AI agents throughout the development lifecycle.

Project-specific testing standards are defined in:

../SKILL.md

Reference documentation is available in:

../references/

---

## Intended Use

Scripts in this directory may be used to:

- Run unit tests
- Run integration tests
- Run functional tests
- Run API tests
- Run regression tests
- Run performance tests
- Run security tests
- Validate migrations
- Validate fixtures
- Generate coverage reports
- Generate test reports
- Detect flaky tests
- Verify release readiness
- Execute production smoke tests

---

## Script Categories

Supported script categories include:

- Unit Testing
- Integration Testing
- Functional Testing
- API Testing
- Regression Testing
- Database Testing
- Migration Validation
- Fixture Validation
- Coverage Analysis
- Security Testing
- Performance Testing
- Smoke Testing
- Test Reporting
- Production Verification

---

## Suggested Scripts

Examples:

```text
run-unit-tests.py
run-integration-tests.py
run-api-tests.py
run-functional-tests.py
run-regression-tests.py
run-performance-tests.py
run-security-tests.py
migration-validator.py
fixture-validator.py
coverage-report.py
flaky-test-check.py
test-report.py
smoke-test.py
production-check.py
```

---

## Naming Convention

Use descriptive lowercase filenames.

Examples:

```text
run-unit-tests.py
coverage-report.py
production-check.py
```

Avoid:

```text
script.py
temp.py
new.py
testing.py
```

---

## Script Requirements

Every script should:

- Perform one clearly defined task.
- Be reusable.
- Produce structured and readable output.
- Exit with appropriate status codes.
- Handle exceptions gracefully.
- Validate execution environment.
- Support automation.
- Avoid hardcoded configuration.

---

## Output

Scripts should report:

- Start Time
- End Time
- Execution Duration
- Total Tests
- Passed Tests
- Failed Tests
- Skipped Tests
- Coverage Percentage
- Warnings
- Overall Status

Output should be deterministic and machine-readable whenever possible.

---

## Logging

Scripts should log:

- Executed Tests
- Warnings
- Errors
- Execution Duration

Never log:

- Passwords
- API Keys
- Tokens
- Secrets
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
- Validate project state before execution.
- Produce deterministic results.
- Minimize external dependencies.
- Support CI/CD pipelines.
- Preserve application integrity.

---

## Production Rules

Production verification scripts must:

- Execute critical test suites.
- Verify application startup.
- Verify database migrations.
- Verify API health.
- Verify authentication.
- Verify critical user flows.
- Generate release reports.
- Abort deployment if critical tests fail.

---

## Notes

This directory contains executable automation scripts only.

Project-specific testing rules belong in:

../SKILL.md

Reference documentation belongs in:

../references/

Do not store:

- Documentation
- Test Reports
- Coverage Reports
- Logs
- Configuration Files
- Credentials
- Environment Files
- Application Source Code

inside this directory.