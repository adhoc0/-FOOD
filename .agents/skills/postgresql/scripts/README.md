# PostgreSQL Scripts

## Purpose

This directory contains reusable automation scripts for PostgreSQL administration, database maintenance, optimization, validation, backup, monitoring, and deployment within the FOOD project.

Scripts are intended to automate repetitive database tasks, improve consistency, reduce human error, and support developers and AI agents throughout the project lifecycle.

Project-specific PostgreSQL standards are defined in:

../SKILL.md

Reference documentation is available in:

../references/

---

## Intended Use

Scripts in this directory may be used to:

- Create databases
- Initialize database environments
- Apply migrations
- Validate migrations
- Load fixtures
- Seed development data
- Verify indexes
- Analyze query performance
- Generate execution plans
- Check database integrity
- Backup databases
- Restore databases
- Monitor database health
- Generate performance reports
- Prepare production deployments

---

## Script Categories

Supported script categories include:

- Database Initialization
- Migration Validation
- Fixture Management
- Data Seeding
- Backup
- Restore
- Index Validation
- Query Analysis
- Execution Plan Analysis
- Performance Analysis
- Database Monitoring
- Health Checks
- Security Validation
- Production Verification

---

## Suggested Scripts

Examples:

```text
create-database.py
initialize-db.py
verify-migrations.py
load-fixtures.py
seed-data.py
backup.py
restore.py
index-check.py
query-analysis.py
execution-plan.py
database-health.py
performance-report.py
security-check.py
production-check.py
```

---

## Naming Convention

Use descriptive lowercase filenames.

Examples:

```text
backup.py
restore.py
query-analysis.py
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
- Produce clear and readable output.
- Exit with appropriate status codes.
- Handle errors gracefully.
- Avoid hardcoded credentials.
- Avoid hardcoded database names.
- Support automation.

---

## Cross-Platform Support

Whenever possible, support multiple operating systems.

Preferred languages:

- Python
- Bash (.sh)
- PowerShell (.ps1)

Avoid operating system-specific assumptions.

---

## Guidelines

Scripts should:

- Follow project coding standards.
- Be idempotent whenever possible.
- Validate input before execution.
- Log meaningful errors.
- Minimize external dependencies.
- Produce consistent output.
- Support CI/CD pipelines.
- Protect production data.

---

## Safety Rules

Database scripts should:

- Verify the target database before execution.
- Confirm destructive operations when appropriate.
- Create backups before irreversible changes.
- Never expose credentials.
- Validate database connections.
- Verify transaction success.
- Roll back safely on failure whenever possible.

---

## Notes

This directory contains executable automation scripts only.

Project-specific PostgreSQL rules belong in:

../SKILL.md

Reference documentation belongs in:

../references/

Do not store documentation, configuration files, SQL dumps, backups, credentials, or application source code in this directory.