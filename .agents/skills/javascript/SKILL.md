---
name: javascript
description: Modern JavaScript standards, DOM manipulation, browser APIs, accessibility, performance, security, and frontend best practices for the FOOD project.
---

# JavaScript

## Purpose

This skill defines the JavaScript development standards for the FOOD project.

All JavaScript code must be:

- Maintainable
- Secure
- Performant
- Accessible
- Progressive
- Production Ready

---

# General Principles

Always prioritize:

1. Simplicity
2. Readability
3. Performance
4. Accessibility
5. Maintainability
6. Security

Use JavaScript only when necessary.

Prefer native browser APIs over third-party libraries whenever practical.

---

# Project Philosophy

JavaScript should enhance the user experience.

The application must remain functional whenever possible without JavaScript.

Prefer Progressive Enhancement.

Avoid unnecessary client-side rendering.

---

# Language Standard

Use modern ECMAScript.

Prefer:

- const
- let
- Arrow Functions
- Modules
- async / await
- Template Literals
- Optional Chaining
- Nullish Coalescing

Avoid obsolete syntax.

---

# Variables

Use:

- const by default
- let only when reassignment is required

Never use:

- var

---

# Functions

Functions should:

- Have one responsibility
- Remain small
- Use descriptive names
- Return predictable values

Avoid deeply nested functions.

---

# Modules

Organize JavaScript into reusable modules.

Avoid global variables.

Keep module dependencies minimal.

---

# DOM Manipulation

Minimize DOM updates.

Cache DOM elements whenever appropriate.

Avoid unnecessary DOM queries.

Use:

- querySelector()
- querySelectorAll()

Prefer data-* attributes over fragile selectors.

---

# Events

Register events using:

addEventListener()

Avoid inline event handlers.

Example:

onclick

onchange

onmouseover

Use event delegation when appropriate.

---

# Forms

Validate forms on the client only for user experience.

Always perform server-side validation.

Never trust client-side validation.

---

# AJAX

Use:

Fetch API

Prefer:

async / await

Handle all network errors gracefully.

Avoid synchronous requests.

---

# Error Handling

Always handle:

- Network Errors
- Invalid Responses
- Unexpected Exceptions

Provide user-friendly error messages.

Never silently ignore errors.

---

# Performance

Optimize:

- DOM Manipulation
- Event Listeners
- Rendering
- Animations
- Memory Usage

Avoid:

- Unnecessary reflows
- Layout thrashing
- Excessive timers

---

# Accessibility

Support:

- Keyboard Navigation
- Screen Readers
- Focus Management

Never require a mouse for interaction.

Respect:

prefers-reduced-motion

---

# Responsive Behavior

JavaScript should adapt to:

- Desktop
- Tablet
- Mobile

Avoid viewport-specific hacks.

---

# Animations

Prefer CSS animations.

Use JavaScript animations only when necessary.

Avoid unnecessary animations.

---

# Browser APIs

Prefer native APIs.

Examples:

- Fetch API
- Intersection Observer
- Resize Observer
- Mutation Observer
- Clipboard API
- History API

Avoid unnecessary polyfills.

---

# Storage

Use:

- sessionStorage
- localStorage

only for non-sensitive data.

Never store:

- Passwords
- Tokens
- Secrets

Sensitive information must remain on the server.

---

# Security

Always:

- Validate external input.
- Escape dynamic HTML.
- Protect against XSS.
- Respect Content Security Policy.

Never use:

eval()

new Function()

Avoid dynamically generating executable code.

---

# Django Integration

JavaScript should integrate cleanly with Django Templates.

Avoid embedding business logic inside templates.

Prefer external JavaScript files.

Use Django-generated data safely.

---

# SEO

JavaScript should not block:

- Content Rendering
- Metadata
- Structured Data
- Navigation

Critical content should remain server-rendered.

---

# Naming Conventions

Use descriptive camelCase names.

Examples:

loadRecipes()

updateSearchResults()

toggleMenu()

Avoid:

function1()

test()

temp()

---

# Code Organization

Separate code into:

- Components
- Utilities
- Services
- Helpers

Avoid monolithic files.

---

# Dependencies

Prefer native browser APIs.

Only introduce third-party libraries when they provide significant value.

Review dependencies regularly.

---

# Logging

Use console logging only during development.

Remove unnecessary logs before production.

Avoid exposing sensitive information.

---

# Testing

JavaScript should be testable.

Test:

- User interactions
- Event handling
- DOM updates
- API requests
- Error handling

---

# FOOD Project Requirements

Support:

- Recipe Search
- Province Filtering
- Category Filtering
- Favorites
- Ratings
- Interactive Turkey Map
- Lazy Loading
- Infinite Scroll (if implemented)

All interactions must remain accessible.

---

# Forbidden Practices

Never:

- Use var
- Use eval()
- Use inline JavaScript
- Modify HTML using unsafe innerHTML
- Store secrets in JavaScript
- Ignore Promise rejections
- Create unnecessary global variables
- Duplicate code
- Depend on JavaScript for critical navigation

---

# Best Practices

Always:

- Write modular code.
- Prefer native APIs.
- Keep files small.
- Handle errors gracefully.
- Optimize performance.
- Respect accessibility.
- Follow project conventions.
- Write production-ready code.

---

# AI Guidelines

Before generating JavaScript:

- Reuse existing modules.
- Avoid unnecessary libraries.
- Prefer modern JavaScript.
- Keep code modular.
- Respect accessibility.
- Respect Django architecture.
- Optimize DOM manipulation.
- Avoid duplicate implementations.

---

# References

Additional JavaScript documentation is available in:

references/

Reusable automation scripts are available in:

scripts/

Project-specific rules always take precedence over general JavaScript best practices.