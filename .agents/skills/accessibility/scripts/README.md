# Accessibility Scripts

## Purpose

This directory contains reusable scripts that help automate accessibility testing, validation, and reporting.

Scripts in this directory should support developers and AI agents in verifying compliance with accessibility standards.

Project accessibility rules are defined in:

../SKILL.md

Reference documentation is located in:

../references/

---

## Intended Use

Scripts may be used to:

- Run automated accessibility audits
- Validate WCAG compliance
- Check semantic HTML
- Detect missing accessibility attributes
- Generate accessibility reports
- Integrate accessibility checks into CI/CD pipelines

---

## Script Categories

Examples of supported scripts:

- axe-core automation
- Lighthouse accessibility audits
- Playwright accessibility tests
- pa11y checks
- HTML validation
- Color contrast analysis
- Keyboard navigation testing
- ARIA validation

---

## Naming Convention

Use descriptive file names.

Examples:

axe-audit.sh

axe-audit.ps1

lighthouse-report.sh

playwright-accessibility.py

keyboard-navigation-test.py

aria-validator.py

color-contrast-check.py

---

## Script Requirements

Every script should:

- Be reusable
- Be documented
- Exit with appropriate status codes
- Produce readable output
- Avoid project-specific hardcoded paths
- Support automation where possible

---

## Cross-Platform Support

Whenever practical, provide scripts for multiple environments.

Preferred formats:

- Python
- Bash (.sh)
- PowerShell (.ps1)

Avoid operating system specific assumptions.

---

## Guidelines

- Keep scripts small and focused.
- One script should perform one task.
- Reuse existing utilities whenever possible.
- Remove obsolete scripts.
- Document required dependencies.
- Validate script output before committing.

---

## Notes

This directory contains executable utilities only.

Accessibility implementation rules belong in:

../SKILL.md

Reference materials belong in:

../references/