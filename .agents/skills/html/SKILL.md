---
name: html
description: HTML5 development standards, semantic markup, accessibility, SEO, responsive structure, and template guidelines for the FOOD project.
---

# HTML

## Purpose

This skill defines the HTML development standards for the FOOD project.

All HTML must be:

- Semantic
- Accessible
- Responsive
- SEO Friendly
- Maintainable
- Production Ready

---

# General Principles

Always prioritize:

1. Semantic HTML
2. Accessibility
3. Readability
4. SEO
5. Performance
6. Maintainability

Prefer native HTML elements over unnecessary JavaScript.

---

# Document Structure

Every page should follow this structure:

```html
<!DOCTYPE html>
<html lang="">
<head>
</head>
<body>
<header></header>
<main></main>
<footer></footer>
</body>
</html>
```

Only one `<main>` element is allowed per page.

---

# Semantic HTML

Prefer semantic elements.

Use:

- header
- nav
- main
- article
- section
- aside
- footer
- figure
- figcaption
- address

Avoid excessive use of:

```html
<div>
```

Use semantic elements whenever appropriate.

---

# Headings

Maintain a logical hierarchy.

Correct example:

```
H1

H2

H3

H3

H2
```

Only one H1 per page.

Never skip heading levels.

---

# Navigation

Navigation should use:

```html
<nav>
```

Navigation links must have descriptive text.

Avoid generic labels such as:

- Click Here
- Read More
- More

---

# Links

Links should:

- Be descriptive
- Use meaningful anchor text
- Indicate external destinations when appropriate

Never use JavaScript instead of hyperlinks for navigation.

---

# Buttons

Always use:

```html
<button>
```

Never use:

```html
<div onclick="">
```

Buttons must contain descriptive text.

---

# Forms

Every form should include:

- label
- fieldset when appropriate
- legend when appropriate

Each input must have:

- id
- name
- label

Required fields should be clearly identified.

Never replace labels with placeholders.

---

# Images

Every image requires:

```html
alt=""
```

Decorative images should use:

```html
alt=""
```

Meaningful images require descriptive alternative text.

Use responsive images whenever appropriate.

---

# SVG

Accessible SVGs should include:

- title
- desc

Interactive SVGs should support keyboard navigation.

---

# Tables

Tables should only present tabular data.

Every table should include:

- thead
- tbody
- th
- scope

Avoid using tables for layout.

---

# Lists

Use:

```html
<ul>
```

for unordered content.

Use:

```html
<ol>
```

for ordered steps.

Recipe instructions should always use ordered lists.

Ingredient lists should always use unordered lists.

---

# Metadata

Every page should include:

- title
- meta description
- viewport
- charset

When applicable:

- canonical
- Open Graph
- Twitter Cards

---

# Structured Data

Support structured data using JSON-LD.

Recipe pages should include:

- Recipe Schema
- Breadcrumb Schema

Category pages should include:

- Breadcrumb Schema

Search pages should avoid structured data unless appropriate.

---

# Accessibility

Support:

- Screen Readers
- Keyboard Navigation
- Focus Indicators
- Semantic HTML
- WCAG 2.2 AA

Prefer native HTML before ARIA.

---

# Responsive Design

HTML should support:

- Mobile
- Tablet
- Desktop

Avoid layout-dependent markup.

Presentation belongs in CSS.

---

# Performance

Optimize:

- Lazy-loaded images
- Responsive images
- Preload critical assets
- Reduce unnecessary DOM nodes

Avoid deeply nested HTML.

---

# Django Templates

Templates should contain presentation only.

Avoid business logic.

Use:

- include
- extends
- block

Keep templates modular.

---

# Template Organization

Use reusable partials.

Separate:

- layout
- components
- pages

Avoid duplicate markup.

---

# FOOD Project Requirements

Recipe pages must include:

- Title
- Description
- Ingredients
- Instructions
- Nutrition Information
- Preparation Time
- Cooking Time
- Images
- Breadcrumb Navigation

Province pages must include:

- Province Name
- Region
- Recipe List
- Pagination

Category pages must include:

- Category Name
- Recipe List
- Breadcrumbs

---

# Naming Conventions

Use lowercase element attributes.

Use descriptive class names.

Avoid meaningless identifiers.

Examples:

recipe-card

province-list

recipe-image

search-form

---

# Forbidden Practices

Never:

- Use tables for layout
- Use div as button
- Skip heading levels
- Omit alt attributes
- Duplicate IDs
- Inline JavaScript
- Inline CSS unless necessary
- Use deprecated HTML elements
- Generate invalid HTML
- Create inaccessible navigation

---

# Best Practices

Always:

- Write valid HTML5
- Keep markup clean
- Use semantic elements
- Keep templates modular
- Support accessibility
- Improve SEO
- Optimize for performance
- Validate generated HTML

---

# AI Guidelines

Before generating HTML:

- Follow semantic HTML.
- Respect accessibility standards.
- Generate valid HTML5.
- Optimize for SEO.
- Keep templates reusable.
- Minimize unnecessary markup.
- Respect Django template conventions.
- Avoid duplicate structures.

---

# References

Additional HTML documentation is available in:

references/

Reusable automation scripts are available in:

scripts/

Project-specific rules always take precedence over general HTML best practices.