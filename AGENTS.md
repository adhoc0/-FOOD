# GEMINI.md

## Project Context

You are working on a long-term software project.

This project is a production-grade application.

Every architectural decision must prioritize long-term maintainability over short-term convenience.

Never generate temporary or quick-fix solutions.

---

# Mandatory Documentation

Before writing, modifying or deleting any code, always read the following documents in order.

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

These documents define the project's architecture and coding rules.

Never generate code that violates them.

---

# Project Goal

Build the highest quality Turkish regional food platform.

The project must be

- scalable
- secure
- maintainable
- performant
- SEO friendly
- accessible
- production ready

Quality is always more important than speed.

---

# Architecture

The project follows Clean Architecture.

Business Logic must only exist inside Services.

Views must remain thin.

Selectors are responsible for reading data.

Validators are responsible for validation.

Models define data only.

Templates contain presentation only.

JavaScript contains UI behaviour only.

Never violate these rules.

---

# Code Quality

Always generate

- clean code
- readable code
- reusable code
- testable code

Avoid clever code.

Prefer explicit code.

---

# Before Writing Code

Always check whether

- similar code already exists
- a reusable component already exists
- a service already exists
- a selector already exists
- a validator already exists

Never duplicate code.

---

# While Writing Code

Follow PEP8.

Follow project naming conventions.

Use meaningful variable names.

Never use wildcard imports.

Never use magic numbers.

Never hardcode values.

Never generate dead code.

---

# Django Rules

Never place Business Logic inside

- View
- Model
- Template
- JavaScript

Always use

Service Layer

for business rules.

---

# Database

Always prefer Django ORM.

Never use Raw SQL unless absolutely necessary.

Optimize queries using

- select_related()
- prefetch_related()

Always think about indexes.

Always think about future scalability.

---

# Security

Every feature must consider

CSRF

XSS

SQL Injection

Authentication

Authorization

Rate Limiting

Input Validation

Output Escaping

Never ignore security.

---

# Performance

Always minimize

Database Queries

DOM Updates

JavaScript Execution

Network Requests

Images

CSS Size

Bundle Size

Always think about Core Web Vitals.

---

# UI

Every UI component should look

minimal

premium

modern

consistent

accessible

professional

Avoid unnecessary decorations.

Whitespace is important.

Typography is important.

Consistency is mandatory.

---

# SEO

Every page must support

Title

Meta Description

Canonical

OpenGraph

Twitter Card

Schema.org

Breadcrumb

Friendly URLs

---

# Refactoring

If existing code can be improved without changing behaviour,

suggest the improvement.

Do not leave poor quality code in the project.

---

# Before Completing Any Task

Verify

Architecture

Security

Performance

Readability

SEO

Accessibility

Maintainability

If any of these are weak,

improve them before finishing.

---

# Never Do

Never generate temporary fixes.

Never duplicate code.

Never ignore documentation.

Never violate architecture.

Never optimize prematurely.

Never over-engineer.

Never create unnecessary abstractions.

Never add dependencies without justification.

Never change project structure without explanation.

---

# If Unsure

Stop.

Explain the trade-offs.

Recommend the most maintainable solution.

Do not guess.

---

# Response Style

Be concise.

Be technically accurate.

Explain important architectural decisions.

Prefer long-term solutions.

Maintain consistency across the entire project.