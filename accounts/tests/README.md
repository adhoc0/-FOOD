# Accounts Tests

This directory contains all automated tests for the Accounts application.

## Structure

- unit/
  - Models
  - Managers
  - QuerySets
  - Selectors
  - Services
  - Validators

- integration/
  - Views
  - URLs
  - Admin
  - Forms

## Rules

- Every new feature must include tests.
- Unit tests must be isolated.
- Integration tests must verify complete workflows.
- Use Django TestCase unless a lower-level test is required.
- Keep tests deterministic and independent.
