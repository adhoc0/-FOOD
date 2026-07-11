---
name: git
description: Git workflow, branching strategy, commit conventions, repository management, and version control standards for the FOOD project.
---

# Git

## Purpose

This skill defines the Git workflow and version control standards for the FOOD project.

All contributors and AI agents must follow these rules to maintain a clean, traceable, and reliable Git history.

---

# General Principles

Always prioritize:

1. Repository Integrity
2. Traceability
3. Consistency
4. Simplicity
5. Collaboration

Never rewrite shared history.

---

# Branch Strategy

Use dedicated branches.

Examples:

- main
- develop
- feature/*
- bugfix/*
- hotfix/*
- release/*

Never commit directly to main.

---

# Branch Naming

Use lowercase.

Examples:

feature/recipe-search

feature/user-profile

bugfix/login-error

hotfix/security-patch

release/v1.2.0

Avoid:

test

new

branch1

---

# Commit Messages

Use clear and descriptive commit messages.

Preferred prefixes:

feat:

fix:

refactor:

perf:

docs:

style:

test:

build:

ci:

chore:

revert:

Examples:

feat: add province filtering

fix: correct recipe slug generation

refactor: simplify search selector

---

# Commit Rules

Each commit should represent one logical change.

Avoid combining unrelated changes.

Keep commits small and reviewable.

---

# Pull Requests

Every Pull Request should:

- Have a clear description
- Explain why changes were made
- Reference related issues
- Pass all tests
- Pass code review

---

# Merge Strategy

Prefer:

- Squash Merge
- Rebase Merge

Avoid unnecessary merge commits.

---

# Conflict Resolution

Resolve conflicts before merging.

Never ignore conflicts.

Review all resolved files carefully.

---

# Repository Hygiene

Remove:

- Temporary files
- Build artifacts
- Cache files

Keep .gitignore updated.

---

# Versioning

Follow Semantic Versioning.

MAJOR.MINOR.PATCH

Examples:

1.0.0

1.2.5

2.0.0

---

# Tags

Tag every production release.

Example:

v1.0.0

v1.1.0

---

# Rollback

Every release should support rollback.

Never merge untested rollback strategies.

---

# Documentation

Update documentation whenever code changes affect:

- APIs
- Architecture
- Deployment
- Configuration

---

# Security

Never commit:

- .env
- Secrets
- Passwords
- API Keys
- Certificates
- Private Keys

---

# AI Guidelines

AI should:

- Generate meaningful commit messages.
- Respect branching strategy.
- Never rewrite Git history.
- Avoid unnecessary commits.
- Keep changes atomic.
- Preserve repository consistency.

---

# Forbidden Practices

Never:

- Commit directly to main
- Force push shared branches
- Commit generated files
- Commit secrets
- Commit binaries unnecessarily
- Leave merge conflicts unresolved
- Use meaningless commit messages

---

# Best Practices

Always:

- Pull before pushing
- Review changes
- Keep commits atomic
- Keep history readable
- Write meaningful commit messages
- Tag releases
- Update documentation

---

# References

Additional Git documentation is available in:

references/

Reusable Git automation scripts are available in:

scripts/

Project-specific rules always take precedence.