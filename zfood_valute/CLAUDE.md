---
name: turkish-regional-food-platform
description: Production-grade Django uygulamalarında uzun vadeli sürdürülebilirlik, Clean Architecture, güvenlik, performans, SEO, erişilebilirlik ve kod kalitesi standartlarını uygulayan yazılım geliştirme skill'i.
---

# Turkish Regional Food Platform — Development Rules

You are Claude working on a long-term software project.

This project is a production-grade Django application.

Every architectural decision must prioritize long-term maintainability over short-term convenience.

Never generate temporary or quick-fix solutions.

---

# Mandatory Documentation

Before writing, modifying, or deleting any code, always read the following documents in order:

1. `docs/AI_CONTEXT.md`
2. `docs/ARCHITECTURE.md`
3. `docs/CODING_STANDARDS.md`
4. `docs/DATABASE.md`
5. `docs/DECISIONS.md`
6. `docs/SECURITY.md`
7. `docs/SEO.md`
8. `docs/DEPLOYMENT.md`
9. `docs/ROADMAP.md`
10. `docs/CHANGELOG.md`

These documents define the project's architecture, technical decisions, and coding rules.

Never generate code that violates them.

---

# Project Goal

Build the highest-quality Turkish regional food platform.

The project must be:

- scalable
- secure
- maintainable
- performant
- SEO-friendly
- accessible
- production-ready

Quality is always more important than speed.

---

# Architecture

The project follows Clean Architecture.

Business logic must exist only inside the Service Layer.

Views must remain thin.

Selectors are responsible for reading data.

Validators are responsible for validation.

Models define data and persistence concerns.

Templates contain presentation only.

JavaScript contains UI behavior only.

Never violate these architectural boundaries.

---

# Code Quality

Always generate:

- clean code
- readable code
- reusable code
- testable code
- maintainable code

Avoid clever code.

Prefer explicit and understandable implementations.

Follow DRY and SOLID principles where they provide meaningful architectural value.

Do not introduce abstractions without justification.

---

# Before Writing Code

Always check whether:

- similar code already exists
- a reusable component already exists
- a service already exists
- a selector already exists
- a validator already exists
- an existing utility can be reused
- the required functionality already exists elsewhere in the project

Never duplicate existing functionality.

---

# While Writing Code

Follow PEP 8.

Follow project naming conventions.

Use meaningful variable and function names.

Never use wildcard imports.

Avoid magic numbers and magic strings.

Do not hardcode configuration values.

Use project configuration and environment variables where appropriate.

Never generate dead code.

Keep functions and classes focused on a single responsibility.

---

# Django Rules

Never place business logic inside:

- Views
- Models
- Templates
- JavaScript

Use the Service Layer for business rules.

Use Selectors for complex read operations.

Use Validators for validation and domain input rules.

Keep Django Views responsible for HTTP concerns and orchestration.

Keep Models responsible for persistence, relationships, constraints, and data representation.

---

# Database

Prefer Django ORM.

Never use raw SQL unless it is technically justified and the Django ORM cannot provide an appropriate solution.

Optimize database access using appropriate techniques such as:

- `select_related()`
- `prefetch_related()`
- `Exists()`
- `Subquery()`
- `annotate()`
- appropriate indexes

Always consider:

- query count
- N+1 queries
- indexing
- constraints
- transaction boundaries
- data integrity
- future scalability

Do not optimize blindly. Measure or reason about the actual bottleneck before introducing complexity.

---

# Security

Every feature must consider:

- CSRF
- XSS
- SQL Injection
- authentication
- authorization
- rate limiting
- input validation
- output escaping
- secure file handling
- sensitive data exposure
- session security
- permission boundaries

Never ignore security requirements.

Never trust user-controlled input.

Follow Django security best practices.

---

# Performance

Always consider minimizing:

- database queries
- unnecessary database writes
- DOM updates
- JavaScript execution
- network requests
- image payloads
- CSS size
- JavaScript bundle size

Always consider Core Web Vitals.

Prefer server-side rendering where appropriate.

Use caching only when its invalidation strategy and consistency requirements are understood.

Do not introduce premature optimization.

---

# UI

Every UI component should be:

- minimal
- premium
- modern
- consistent
- accessible
- professional
- responsive

Avoid unnecessary decoration.

Whitespace is important.

Typography is important.

Consistency is mandatory.

Use reusable components instead of duplicating markup.

---

# HTML

Use semantic HTML5 elements.

Ensure correct document structure.

Use accessible labels and relationships.

Do not use non-semantic elements when a semantic HTML element is appropriate.

Ensure interactive elements are keyboard accessible.

Maintain appropriate heading hierarchy.

---

# Accessibility

Follow WCAG principles.

Consider:

- keyboard navigation
- focus states
- semantic HTML
- accessible names
- form labels
- color contrast
- screen readers
- reduced motion
- responsive layouts

Accessibility must be considered during component design, not added as an afterthought.

---

# CSS

Use the project's established Design System.

Prefer semantic design tokens.

Avoid arbitrary values when an existing token is available.

Keep styles component-oriented and maintainable.

Avoid unnecessary specificity.

Avoid excessive nesting.

Do not introduce global styles without architectural justification.

---

# JavaScript

JavaScript must contain UI behavior only.

Do not place business rules inside frontend JavaScript.

Prefer progressive enhancement where appropriate.

Avoid unnecessary JavaScript.

Avoid duplicate event handlers.

Clean up event listeners when required.

Do not introduce a frontend dependency when native browser APIs or existing project utilities are sufficient.

---

# SEO

Every indexable page must consider:

- title
- meta description
- canonical URL
- Open Graph metadata
- Twitter Card metadata
- Schema.org structured data
- breadcrumbs
- semantic HTML
- friendly URLs
- internal linking
- appropriate heading hierarchy

Avoid duplicate content.

Avoid accidental indexing of administrative, private, or non-indexable pages.

SEO implementation must not compromise accessibility or performance.

---

# Responsive Design

Every UI component must work across:

- mobile
- tablet
- desktop
- large desktop displays

Prefer responsive layouts over device-specific hacks.

Do not assume a fixed viewport size.

---

# Refactoring

If existing code can be improved without changing behavior, identify the improvement.

When modifying existing code:

- preserve existing behavior unless a behavior change is explicitly required
- avoid unnecessary rewrites
- remove duplication
- improve readability
- preserve architectural boundaries
- update affected tests
- update documentation when architectural behavior changes

Do not leave known architectural violations when they are directly related to the task.

---

# Testing

Every meaningful feature or behavior change must consider automated tests.

Prefer testing:

- business rules
- services
- selectors
- validators
- permissions
- important model behavior
- HTTP behavior
- critical user flows

Tests must verify behavior rather than implementation details where possible.

Do not reduce test coverage merely to make a change easier.

---

# Documentation

When an architectural decision changes, update the appropriate documentation.

When introducing a significant technical decision, document:

- the problem
- the chosen solution
- important alternatives
- trade-offs
- consequences

Keep documentation synchronized with the implementation.

---

# Dependencies

Do not add dependencies without justification.

Before adding a dependency, consider:

- whether Django or Python already provides the required functionality
- whether an existing project dependency can solve the problem
- maintenance status
- security history
- license
- performance
- long-term compatibility

Every dependency must provide sufficient value to justify its maintenance cost.

---

# Project Structure

Do not change the project structure without architectural justification.

Before creating a new:

- application
- service
- selector
- validator
- utility
- component
- module
- dependency

verify that an existing architectural location is not already appropriate.

Avoid unnecessary abstractions.

---

# Git and Change Safety

Make changes that are:

- focused
- minimal
- reviewable
- reversible

Do not modify unrelated files.

Do not silently change existing behavior.

Do not remove functionality unless explicitly required or clearly obsolete and documented.

---

# Before Completing Any Task

Verify:

- architecture
- security
- performance
- readability
- SEO
- accessibility
- maintainability
- test coverage
- documentation consistency

If any relevant area is weak, improve it before finishing.

---

# Never Do

Never:

- generate temporary fixes
- duplicate code
- ignore project documentation
- violate architecture
- optimize prematurely
- over-engineer
- create unnecessary abstractions
- add dependencies without justification
- hardcode configuration
- ignore security
- ignore accessibility
- ignore SEO requirements
- change project structure without explanation
- modify unrelated code
- guess when required information is unavailable

---

# If Unsure

Stop.

Identify the uncertainty.

Explain the relevant trade-offs.

Recommend the most maintainable solution based on the available project documentation.

Do not guess about undocumented project behavior.

---

# Response Style

Be concise.

Be technically accurate.

Explain important architectural decisions.

Prefer long-term solutions over short-term convenience.

Maintain consistency across the entire project.

When modifying existing code, clearly identify what changed and why.

Always verify the final implementation against the project's architectural, security, performance, SEO, accessibility, and maintainability requirements.