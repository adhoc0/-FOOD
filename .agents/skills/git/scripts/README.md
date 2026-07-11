# Git Scripts

## Purpose

This directory contains reusable automation scripts for Git operations within the FOOD project.

Scripts should automate repetitive repository maintenance tasks while preserving repository integrity.

Project-specific Git rules are defined in:

../SKILL.md

Reference documentation is available in:

../references/

---

## Intended Use

Scripts may be used to:

- Verify repository status
- Validate commit messages
- Check branch names
- Generate changelogs
- Create release tags
- Verify version numbers
- Clean repository artifacts
- Prepare releases
- Automate Git hooks

---

## Script Categories

Examples:

- Commit Validation
- Branch Validation
- Version Verification
- Release Automation
- Repository Cleanup
- Changelog Generation
- Git Hook Automation

---

## Suggested Scripts

Examples:

check-branch.py

check-commit.py

generate-changelog.py

create-release.py

cleanup.py

verify-version.py

install-hooks.py

---

## Naming Convention

Use descriptive lowercase filenames.

Examples:

generate-changelog.py

verify-version.py

check-branch.py

Avoid:

script.py

temp.py

new.py

---

## Script Requirements

Every script should:

- Perform one task.
- Be reusable.
- Produce readable output.
- Exit with proper status codes.
- Handle errors gracefully.
- Avoid hardcoded paths.

---

## Cross-Platform Support

Whenever possible support:

- Python
- Bash (.sh)
- PowerShell (.ps1)

Avoid operating system specific assumptions.

---

## Guidelines

Scripts should:

- Follow project coding standards.
- Be idempotent whenever possible.
- Validate input.
- Log meaningful errors.
- Minimize external dependencies.

---

## Notes

This directory contains executable automation only.

Project rules belong in:

../SKILL.md

Reference documentation belongs in:

../references/

Do not store documentation or configuration files in this directory.