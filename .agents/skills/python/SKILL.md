---
name: python
description: Python language standards, coding conventions, type safety, error handling, performance, testing, and best practices for the FOOD project.
---

# Python

## Purpose

This skill defines the Python development standards for the FOOD project.

All Python code must be:

- Readable
- Maintainable
- Secure
- Performant
- Testable
- Production Ready

---

# General Principles

Always prioritize:

1. Correctness
2. Readability
3. Simplicity
4. Maintainability
5. Performance
6. Reusability

Write code for humans first.

---

# Python Version

Target the project's supported Python version.

Use modern Python features whenever appropriate.

Avoid deprecated language features.

---

# Code Style

Follow:

- PEP 8
- PEP 20 (The Zen of Python)
- PEP 257 (Docstrings)
- PEP 484 (Type Hints)

Maintain a consistent coding style.

---

# Naming Conventions

Use:

- snake_case for variables and functions
- PascalCase for classes
- UPPER_CASE for constants

Examples:

```python
recipe_name

calculate_total()

RecipeService

MAX_RESULTS
```

Avoid abbreviated names.

---

# Variables

Prefer:

- descriptive names
- immutable values whenever possible

Avoid:

- unnecessary global variables
- single-letter names (except loop counters)

---

# Functions

Functions should:

- perform one task
- remain short
- be easy to test
- have descriptive names
- return predictable values

Avoid excessive parameters.

---

# Classes

Classes should:

- follow the Single Responsibility Principle
- remain cohesive
- expose a clear public interface

Avoid god classes.

---

# Type Hints

Use type hints for:

- function parameters
- return values
- class attributes
- public APIs

Prefer explicit types.

---

# Docstrings

Document:

- public classes
- public functions
- reusable modules

Explain intent rather than implementation.

---

# Imports

Group imports as:

1. Standard Library
2. Third-party Packages
3. Local Project Imports

Avoid wildcard imports.

Prefer absolute imports.

---

# Error Handling

Catch only expected exceptions.

Never suppress exceptions silently.

Raise meaningful exceptions.

Avoid:

```python
except:
    pass
```

---

# Logging

Use the logging module.

Never use print() for application logging.

Log:

- warnings
- errors
- unexpected events

Never log:

- passwords
- tokens
- secrets

---

# File Handling

Always use context managers.

Example:

```python
with open(...) as file:
```

Close resources automatically.

---

# Context Managers

Prefer context managers whenever resources are acquired.

Examples:

- files
- locks
- database connections

---

# Iteration

Prefer:

- comprehensions
- generators
- iterators

Avoid unnecessary loops.

---

# Generators

Use generators for large datasets.

Avoid loading unnecessary data into memory.

---

# Data Structures

Choose the most appropriate structure.

Examples:

- list
- tuple
- dict
- set
- deque

Avoid inefficient structures.

---

# Mutability

Prefer immutable objects whenever practical.

Avoid unintended side effects.

---

# Performance

Optimize only after measuring.

Avoid:

- repeated calculations
- duplicated work
- unnecessary allocations

---

# Memory Usage

Minimize unnecessary object creation.

Release resources promptly.

Avoid keeping unused references.

---

# Concurrency

Use:

- threading
- multiprocessing
- asyncio

only when appropriate.

Avoid unnecessary concurrency.

---

# Async Programming

Use async only for I/O-bound tasks.

Avoid mixing synchronous and asynchronous code unnecessarily.

---

# Configuration

Store configuration outside source code.

Never hardcode:

- passwords
- API keys
- tokens
- secrets

---

# Security

Validate all external input.

Never execute untrusted code.

Avoid:

- eval()
- exec()

unless absolutely necessary.

---

# Testing

Every public function should be testable.

Write:

- Unit Tests
- Integration Tests
- Regression Tests

when appropriate.

---

# Documentation

Document:

- complex logic
- reusable utilities
- public APIs

Keep documentation up to date.

---

# Dependencies

Prefer the Python Standard Library whenever practical.

Add third-party dependencies only when they provide significant value.

Review dependencies regularly.

---

# Code Quality

Follow:

- SOLID
- DRY
- KISS
- YAGNI

Avoid duplicated code.

---

# FOOD Project Requirements

Python code should:

- follow the project architecture
- remain modular
- separate business logic from infrastructure
- be reusable across applications

Avoid tightly coupled modules.

---

# Forbidden Practices

Never:

- use print() for debugging in production
- ignore exceptions
- hardcode secrets
- use wildcard imports
- duplicate business logic
- create circular imports
- use mutable default arguments
- introduce unnecessary dependencies

---

# Best Practices

Always:

- write readable code
- use descriptive names
- add type hints
- keep functions small
- write reusable components
- handle exceptions properly
- document public APIs
- write tests
- review performance after implementation

---

# AI Guidelines

Before generating Python code:

- Reuse existing modules.
- Follow project architecture.
- Prefer standard library modules.
- Add type hints.
- Keep functions focused.
- Avoid duplicate implementations.
- Respect project naming conventions.
- Generate production-ready code.

---

# References

Additional Python documentation is available in:

references/

Reusable automation scripts are available in:

scripts/

Project-specific rules always take precedence over general Python best practices.