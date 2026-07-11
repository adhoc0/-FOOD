---
name: django
description: Django development standards, project architecture, ORM usage, security, performance, testing, and best practices for the FOOD project.
---

# Django

## Purpose

This skill defines the Django development standards for the FOOD project.

Its goal is to ensure that all Django code is:

- Maintainable
- Secure
- Performant
- Scalable
- Testable
- Consistent

All AI agents and developers must follow these standards.

---

# General Principles

Always prioritize:

1. Correctness
2. Security
3. Maintainability
4. Performance
5. Readability
6. Simplicity

Prefer explicit code over implicit behavior.

Avoid unnecessary complexity.

---

# Project Architecture

The project follows a layered architecture.

```
Request

↓

URL

↓

View

↓

Service

↓

Selector

↓

Model

↓

Database
```

Business logic must never exist inside Views.

---

# Django Apps

Each application must have a single responsibility.

Apps should remain independent whenever possible.

Avoid circular dependencies.

Each app should contain only related functionality.

---

# Directory Structure

Preferred structure:

```
app/

admin/

forms/

management/

migrations/

models/

selectors/

services/

signals/

templates/

tests/

urls/

validators/

views/
```

Avoid placing everything inside a single file.

---

# Models

Models represent database structure.

Models should contain:

- Relationships
- Small helper methods
- Validation when appropriate

Avoid placing complex business logic inside models.

---

# Managers

Use custom Managers only when reusable queries are required.

Managers should never contain business logic.

---

# QuerySets

Reusable query logic should be implemented as custom QuerySets whenever appropriate.

Avoid duplicating query logic.

---

# Services

Business logic belongs inside Services.

Services should:

- Perform business operations
- Coordinate multiple models
- Validate workflows
- Handle transactions

Services must remain reusable.

---

# Selectors

Selectors are responsible for reading data.

Selectors should:

- Build ORM queries
- Optimize queries
- Return QuerySets whenever possible

Selectors must not modify data.

---

# Validators

Validation belongs in validators.

Avoid repeating validation inside Views.

Validators should remain reusable.

---

# Views

Views should remain thin.

Responsibilities:

- Receive request
- Validate input
- Call services
- Return response

Views should not contain business logic.

---

# URLs

Keep URL patterns clean.

Use descriptive names.

Group URLs logically.

Avoid deeply nested routes.

---

# Templates

Templates should contain presentation only.

Never place business logic inside templates.

Use template tags only when necessary.

---

# Forms

Use Django Forms whenever appropriate.

Validate user input.

Display meaningful validation messages.

---

# Admin

Admin is for administration only.

Configure:

- list_display
- search_fields
- list_filter
- ordering
- readonly_fields

Avoid unnecessary customizations.

---

# Signals

Avoid signals unless necessary.

Signals should:

- remain lightweight
- avoid database loops
- avoid business workflows

Prefer Services over Signals.

---

# Middleware

Middleware should remain lightweight.

Do not perform expensive database operations.

Avoid business logic.

---

# ORM

Always prefer Django ORM.

Avoid Raw SQL.

Use ORM features whenever possible.

---

# Query Optimization

Always review:

- Query count
- Duplicate queries
- N+1 queries

Use:

select_related()

prefetch_related()

when appropriate.

---

# Transactions

Use:

transaction.atomic()

for operations that modify multiple objects.

Keep transactions short.

---

# Database

Always define:

- indexes
- constraints
- related_name
- verbose_name

Use ForeignKey whenever relationships exist.

Avoid unnecessary JSONField usage.

---

# Migrations

Keep migrations small.

Separate:

Schema changes

and

Data migrations.

Always verify rollback safety.

---

# Security

Always use:

- CSRF Protection
- Authentication
- Authorization
- Permission Checks
- Input Validation

Never trust user input.

---

# Authentication

Use Django authentication system.

Never implement custom password hashing.

Use secure password validation.

---

# Permissions

Verify permissions in every protected endpoint.

Never rely solely on frontend validation.

---

# File Uploads

Validate:

- file type
- file size
- MIME type

Never trust uploaded filenames.

---

# Static Files

Keep static assets organized.

Compress assets for production.

Enable browser caching.

---

# Media Files

Store uploaded files outside application code.

Protect private files.

---

# Caching

Cache only when measurable benefit exists.

Avoid stale cache issues.

Document cache invalidation strategy.

---

# Logging

Log:

- errors
- warnings
- security events

Never log:

- passwords
- tokens
- secrets

---

# Error Handling

Raise meaningful exceptions.

Never hide unexpected exceptions.

Return user-friendly error messages.

---

# Performance

Always evaluate:

- Query count
- Response time
- Memory usage
- ORM efficiency
- Lazy loading

Optimize only when necessary.

---

# Testing

Every feature should include tests.

Prefer:

- Unit Tests
- Integration Tests
- Functional Tests

Critical workflows must always be tested.

---

# Naming Conventions

Models:

Singular

Example:

Recipe

Province

Category

Services:

RecipeService

Selectors:

RecipeSelector

Validators:

RecipeValidator

Managers:

RecipeManager

Views:

RecipeDetailView

Keep names descriptive.

---

# Documentation

Document:

- complex logic
- public APIs
- architectural decisions

Avoid unnecessary comments.

Code should be self-explanatory.

---

# Code Quality

Follow:

- SOLID
- DRY
- KISS
- YAGNI

Keep methods small.

Keep classes focused.

Avoid duplicated code.

---

# Accessibility

Templates must support:

- Semantic HTML
- Keyboard Navigation
- Screen Readers

Respect WCAG 2.2 AA.

---

# SEO

Templates should include:

- Proper headings
- Meta tags
- Canonical URLs
- Structured Data

Follow project SEO standards.

---

# Forbidden Practices

Never:

- Write business logic inside Views
- Write Raw SQL without justification
- Use print() for debugging
- Commit DEBUG=True
- Store secrets in source code
- Create circular imports
- Duplicate ORM queries
- Ignore migrations
- Ignore permission checks
- Ignore validation
- Remove tests
- Introduce unnecessary abstractions

---

# Best Practices

Always:

- Keep code readable
- Prefer composition over inheritance
- Prefer reusable components
- Keep apps independent
- Write production-ready code
- Optimize queries
- Follow Django conventions
- Keep documentation updated

---

# AI Guidelines

Before generating code:

- Analyze existing architecture.
- Reuse existing services.
- Reuse selectors.
- Follow project naming conventions.
- Respect application boundaries.
- Avoid duplicate implementations.
- Generate maintainable code.
- Prefer Django built-in features.
- Avoid introducing new dependencies unless justified.

---

# References

Additional Django documentation is available in:

references/

Reusable automation scripts are available in:

scripts/

Project-specific rules always take precedence over general Django best practices.