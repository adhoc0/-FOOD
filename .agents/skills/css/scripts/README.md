# CSS Scripts

## Purpose

This directory contains reusable scripts that help automate CSS development, optimization, testing, and maintenance tasks.

Scripts in this directory should support developers and AI agents in maintaining consistent, high-performance CSS.

Project CSS rules are defined in:

../SKILL.md

Reference documentation is located in:

../references/

---

## Intended Use

Scripts may be used to:

- Generate CSS patterns
- Optimize CSS delivery
- Automate cross-browser testing
- Validate CSS against best practices
- Generate design token files
- Automate responsive breakpoints
- Create accessible color utilities
- Simplify CSS workflow tasks

---

## Script Categories

Examples of supported scripts:

- css-variable-generator.js
- breakpoint-calculator.js
- optimize-css.js
- css-lint.sh
- design-token-sync.js
- accessibility-utilities.js
- browser-compatibility-tester.js
- stylelint-configurator.js

---

## Naming Convention

Use descriptive, lowercase file names.

Examples:

```text
css-variable-generator.js
breakpoint-calculator.js
optimize-css.js
```

Avoid:

```text
temp.js
notes.js
new.js
```

---

## Script Requirements

Every script should:

- Be reusable across projects
- Be documented with clear comments
- Exit with appropriate status codes
- Produce stable output
- Avoid project-specific hardcoded values
- Support automation where possible

---

## Cross-Platform Support

Whenever practical, provide scripts for multiple environments.

Preferred formats:

- JavaScript (.js)
- Bash (.sh)
- PowerShell (.ps1)

Avoid operating system specific assumptions where possible.

---

## Guidelines

- Keep scripts small and focused.
- One script should perform one task.
- Prefer using existing libraries over custom implementations.
- Document required dependencies.
- Validate script output before committing.
- Remove obsolete scripts.

---

## Notes

This directory contains executable utilities only.

CSS implementation rules belong in:

../SKILL.md

Reference materials belong in:

../references/
