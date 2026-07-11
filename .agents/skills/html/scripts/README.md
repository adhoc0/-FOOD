# HTML Scripts

## Purpose

This directory contains reusable automation scripts for HTML development within the FOOD project.

Scripts are intended to automate repetitive HTML validation, optimization, accessibility verification, and quality assurance tasks for developers and AI agents.

Project-specific HTML standards are defined in:

../SKILL.md

Reference documentation is available in:

../references/

---

## Intended Use

Scripts in this directory may be used to:

- Validate HTML syntax
- Verify semantic HTML structure
- Detect accessibility issues
- Validate metadata
- Check heading hierarchy
- Detect broken internal links
- Verify image attributes
- Validate structured data
- Generate HTML reports
- Prepare HTML for production

---

## Script Categories

Supported script categories include:

- HTML Validation
- Semantic Analysis
- Accessibility Checks
- Metadata Validation
- Structured Data Validation
- Link Validation
- Image Optimization Checks
- SEO Analysis
- Performance Analysis
- Production Verification

---

## Suggested Scripts

Examples:

```text
validate-html.py
semantic-check.py
heading-check.py
meta-validator.py
link-check.py
image-validator.py
schema-validator.py
accessibility-check.py
seo-check.py
production-check.py
```

---

## Naming Convention

Use descriptive lowercase filenames.

Examples:

```text
validate-html.py
schema-validator.py
link-check.py
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

---

## Notes

This directory contains executable automation scripts only.

Project-specific HTML rules belong in:

../SKILL.md

Reference documentation belongs in:

../references/

Do not store documentation, configuration files, or application source code in this directory.