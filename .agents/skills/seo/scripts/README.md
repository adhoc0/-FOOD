# SEO Scripts

## Purpose

This directory contains reusable automation scripts for Search Engine Optimization (SEO) validation, analysis, auditing, reporting, and production verification within the FOOD project.

Scripts automate repetitive SEO tasks, improve consistency, detect optimization opportunities, and support developers and AI agents throughout the software development lifecycle.

Project-specific SEO standards are defined in:

../SKILL.md

Reference documentation is available in:

../references/

---

## Intended Use

Scripts in this directory may be used to:

- Validate page metadata
- Validate HTML heading hierarchy
- Verify canonical URLs
- Verify robots.txt
- Verify sitemap.xml
- Validate structured data
- Validate JSON-LD
- Analyze internal links
- Detect broken links
- Detect duplicate metadata
- Verify image alt attributes
- Analyze page performance
- Validate Core Web Vitals
- Generate SEO reports
- Prepare production SEO audits

---

## Script Categories

Supported script categories include:

- Metadata Validation
- Structured Data Validation
- Sitemap Validation
- Robots.txt Validation
- Link Analysis
- Broken Link Detection
- Canonical URL Validation
- Heading Structure Validation
- Image SEO Validation
- Keyword Analysis
- Content Analysis
- Performance Analysis
- Core Web Vitals
- SEO Auditing
- Production Verification

---

## Suggested Scripts

Examples:

```text
metadata-check.py
heading-check.py
canonical-check.py
robots-check.py
sitemap-check.py
schema-check.py
jsonld-check.py
link-analysis.py
broken-links.py
image-seo.py
keyword-analysis.py
content-analysis.py
core-web-vitals.py
seo-report.py
production-check.py
```

---

## Naming Convention

Use descriptive lowercase filenames.

Examples:

```text
metadata-check.py
schema-check.py
seo-report.py
```

Avoid:

```text
script.py
temp.py
new.py
seo.py
```

---

## Script Requirements

Every script should:

- Perform one clearly defined task.
- Be reusable.
- Produce structured and readable output.
- Exit with appropriate status codes.
- Handle exceptions gracefully.
- Validate input before execution.
- Avoid hardcoded URLs.
- Support automation.

---

## Output

Scripts should report:

- Start Time
- End Time
- Execution Duration
- SEO Status
- Warnings
- Errors
- Recommendations
- Overall Score

Output should be deterministic and machine-readable whenever possible.

---

## Logging

Scripts should log:

- Executed Checks
- Warnings
- Errors
- Execution Duration

Never log:

- Credentials
- Secrets
- Tokens
- Personal Data
- Environment Variables

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
- Validate project configuration before execution.
- Produce deterministic results.
- Minimize external dependencies.
- Support CI/CD pipelines.
- Preserve application integrity.

---

## Production Rules

Production SEO scripts must:

- Verify metadata completeness.
- Verify canonical URLs.
- Verify sitemap generation.
- Verify robots.txt configuration.
- Verify structured data.
- Verify image accessibility.
- Verify Core Web Vitals.
- Verify internal linking.
- Abort safely when critical SEO issues are detected.

---

## Notes

This directory contains executable automation scripts only.

Project-specific SEO rules belong in:

../SKILL.md

Reference documentation belongs in:

../references/

Do not store:

- Documentation
- Configuration files
- Reports
- Logs
- Environment files
- Credentials
- Application source code

inside this directory.