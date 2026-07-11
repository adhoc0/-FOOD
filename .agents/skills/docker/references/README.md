# Django References

## Purpose

This directory contains reference documentation for Django development used in the FOOD project.

These documents support developers and AI agents by providing implementation guidance, technical notes, architectural references, and best practices.

Project-specific development rules are defined in:

../SKILL.md

---

## Scope

Reference documents may cover topics such as:

- Django Architecture
- Django ORM
- Query Optimization
- Models
- Managers
- QuerySets
- Services
- Selectors
- Validators
- Forms
- Views
- Templates
- Middleware
- Signals
- Authentication
- Authorization
- Permissions
- File Uploads
- Static Files
- Media Files
- Caching
- Logging
- Testing
- Deployment

---

## Intended Use

Reference documents should help:

- Explain Django concepts.
- Provide implementation examples.
- Document architectural decisions.
- Describe best practices.
- Support AI-assisted development.
- Reduce duplicated knowledge.

---

## Suggested Documents

Examples include:

```text
architecture.md
orm.md
models.md
services.md
selectors.md
validators.md
views.md
templates.md
middleware.md
signals.md
authentication.md
permissions.md
caching.md
testing.md
deployment.md
```

---

## File Naming

Use descriptive lowercase filenames.

Examples:

```text
services.md
query-optimization.md
authentication.md
permissions.md
```

Avoid:

```text
notes.md
new.md
temp.md
misc.md
```

---

## Guidelines

Reference documents should:

- Focus on one topic.
- Be framework-specific.
- Remain concise.
- Avoid duplicate information.
- Reference official Django documentation whenever appropriate.
- Be reviewed periodically.

---

## Notes

Do not place project rules in this directory.

Project rules belong in:

../SKILL.md

Reusable automation belongs in:

../scripts/

Only reference documentation should be stored here.