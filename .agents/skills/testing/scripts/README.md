---
name: testing
description: Software testing standards, quality assurance, test automation, verification strategies, and testing best practices for the FOOD project.
---

# Testing

## Purpose

This skill defines the software testing standards for the FOOD project.

Every feature, bug fix, and refactoring must be verified through testing before being considered complete.

Testing is a mandatory part of development.

---

# General Principles

Always prioritize:

1. Correctness
2. Reliability
3. Repeatability
4. Maintainability
5. Automation
6. Test Coverage

Never assume code works without verification.

---

# Testing Philosophy

Every bug should result in a regression test.

Every feature should have appropriate automated tests.

Tests should verify behavior, not implementation details.

Tests should remain independent and deterministic.

---

# Test Pyramid

Follow the Test Pyramid.

Prioritize:

- Unit Tests
- Integration Tests
- Functional Tests
- End-to-End Tests

Keep End-to-End tests limited to critical user flows.

---

# Unit Testing

Unit tests should:

- Test one behavior.
- Be isolated.
- Execute quickly.
- Avoid external dependencies.
- Produce deterministic results.

Mock external systems only.

---

# Integration Testing

Verify:

- Database Integration
- ORM Behavior
- Service Integration
- Cache Integration
- API Integration
- Third-Party Services

---

# Functional Testing

Verify complete business workflows.

Focus on:

- User actions
- Business rules
- Feature correctness

---

# API Testing

Every public API should verify:

- HTTP Status Codes
- Request Validation
- Response Format
- Authentication
- Authorization
- Error Responses
- Pagination
- Filtering

---

# Database Testing

Verify:

- Migrations
- Constraints
- Relationships
- Transactions
- Indexes
- Query Results

Test migration safety.

---

# Fixtures

Fixtures should be:

- Small
- Reusable
- Predictable
- Independent

Avoid unnecessary fixture duplication.

---

# Mocking

Mock only:

- External APIs
- Email Services
- Payment Services
- File Storage
- Time
- Randomness

Avoid mocking application logic.

---

# Coverage

Focus on meaningful coverage.

Prioritize:

- Business Logic
- Security
- Data Validation
- Critical User Flows

Coverage percentage is not the primary goal.

---

# Regression Testing

Every resolved bug should include a regression test.

Prevent previously fixed defects from returning.

---

# Performance Testing

Measure:

- Response Time
- Query Count
- Memory Usage
- CPU Usage

Optimize only after measurement.

---

# Security Testing

Verify:

- Authentication
- Authorization
- CSRF Protection
- Input Validation
- XSS Protection
- SQL Injection Prevention
- Permission Enforcement

---

# Error Handling

Tests should verify:

- Expected Failures
- Validation Errors
- Exception Handling
- Edge Cases

Never ignore failure scenarios.

---

# Continuous Integration

Automated tests should execute during CI.

Deployment should fail when:

- Critical tests fail.
- Migration validation fails.
- Security tests fail.

---

# Test Naming

Use descriptive names.

Examples:

```python
test_recipe_creation_requires_title()

test_only_admin_can_delete_recipe()

test_search_returns_matching_recipes()
```

Avoid generic names.

---

# Test Structure

Follow:

Arrange

Act

Assert

Keep each test focused on one behavior.

---

# Test Data

Use minimal data required.

Avoid unnecessary records.

Create reusable factories when appropriate.

---

# Django Testing

Use:

- Django TestCase
- TransactionTestCase
- Client
- RequestFactory

Test:

- Models
- Views
- Forms
- Services
- Middleware
- Management Commands

---

# FOOD Project Requirements

Critical features requiring tests:

- Authentication
- User Registration
- Recipe Management
- Province Management
- Category Management
- Search
- Favorites
- Ratings
- Image Upload
- Admin Panel
- API Endpoints

No critical feature should be merged without tests.

---

# Forbidden Practices

Never:

- Skip critical tests.
- Ignore failing tests.
- Depend on test execution order.
- Use production data.
- Leave flaky tests unresolved.
- Write tests without assertions.
- Duplicate test logic.
- Mock business logic unnecessarily.

---

# Best Practices

Always:

- Keep tests independent.
- Write readable tests.
- Test edge cases.
- Test failure scenarios.
- Test security.
- Test permissions.
- Test business rules.
- Maintain deterministic execution.
- Keep tests fast.

---

# AI Guidelines

Before generating code:

- Generate appropriate tests.
- Reuse existing fixtures.
- Avoid duplicate tests.
- Verify critical paths.
- Test edge cases.
- Follow project architecture.
- Produce deterministic tests.
- Keep tests maintainable.

---

# References

Additional testing documentation is available in:

references/

Reusable automation scripts are available in:

scripts/

Project-specific rules always take precedence over general software testing best practices.