# GEMINI.md

## Purpose

This document defines the rules that Gemini must follow while working on this repository.

This project is a long-term, production-grade Django application.

Never prioritize speed over quality.

Never generate temporary or quick-fix solutions.

---

# Read First

Before writing, modifying, or deleting any code, always read the following documents in order.

1. docs/AI_CONTEXT.md
2. docs/ARCHITECTURE.md
3. docs/CODING_STANDARDS.md
4. docs/DATABASE.md
5. docs/DECISIONS.md
6. docs/SECURITY.md
7. docs/SEO.md
8. docs/DEPLOYMENT.md
9. docs/ROADMAP.md
10. docs/CHANGELOG.md

These documents are the project's single source of truth.

Never generate code that violates them.

---

# Working Principles

Every change must be

- architecturally consistent
- secure
- maintainable
- testable
- performant
- production ready

Prefer long-term maintainability over short-term convenience.

---

# Code Rules

Business Logic belongs only in the Service layer.

Views handle HTTP requests only.

Selectors are responsible for reading data.

Validators are responsible for validation.

Models define data.

Templates render presentation only.

JavaScript handles UI behaviour only.

Never violate these responsibilities.

---

# Before Writing Code

Always determine whether

- similar code already exists
- a reusable component exists
- a Service already exists
- a Selector already exists
- a Validator already exists

Reuse existing code whenever possible.

Avoid duplication.

---

# Django Rules

Prefer Django ORM.

Avoid Raw SQL unless absolutely necessary.

Optimize queries using

- select_related()
- prefetch_related()

Always consider

- scalability
- indexes
- migrations
- transaction safety

---

# Security

Every feature must consider

- Authentication
- Authorization
- CSRF
- XSS
- SQL Injection
- Rate Limiting
- Input Validation
- Output Escaping

Security is never optional.

---

# Performance

Always minimize

- database queries
- network requests
- JavaScript execution
- CSS size
- image size
- unnecessary rendering

Optimize for Core Web Vitals.

---

# SEO

Every public page should support

- Title
- Meta Description
- Canonical
- OpenGraph
- Twitter Card
- Schema.org
- Breadcrumb
- Friendly URLs

---

# UI

Every component should be

- modern
- minimal
- accessible
- responsive
- consistent
- professional

---

# Never Do

Never

- duplicate code
- place Business Logic inside Views or Models
- use Raw SQL without justification
- hardcode values
- use magic numbers
- write inline CSS
- write inline JavaScript
- ignore documentation
- violate the project architecture
- add unnecessary dependencies
- generate placeholder implementations

---

# Before Completing Any Task

Verify

- Architecture
- Security
- Performance
- Readability
- Accessibility
- SEO
- Maintainability

If any area can be improved without changing behaviour, improve it before finishing.

---

# Response Style

Study the existing implementation before generating code.

Reuse existing architecture whenever possible.

Explain important architectural decisions briefly.

Recommend maintainable solutions.

Do not guess.

If requirements are unclear, explain the available options before implementing.