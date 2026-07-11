---
name: accessibility
description: Accessibility (WCAG 2.2 AA) guidelines, semantic HTML, ARIA usage, keyboard navigation, screen reader compatibility, and inclusive user interface standards for the FOOD project.
---

# Accessibility

## Purpose

This skill defines the accessibility standards for the FOOD project.

All user interfaces must be usable by everyone, including people using:

- Screen Readers
- Keyboard Navigation
- Voice Control
- High Contrast Mode
- Reduced Motion
- Mobile Accessibility Features

The project targets **WCAG 2.2 Level AA** compliance.

---

# General Principles

Always prioritize:

- Accessibility
- Simplicity
- Readability
- Consistency
- Inclusiveness

Accessibility must never be treated as an optional enhancement.

---

# Semantic HTML

Always use semantic HTML.

Prefer:

- header
- nav
- main
- article
- section
- aside
- footer
- figure
- figcaption

Avoid using generic `<div>` elements when semantic elements exist.

---

# Forms

Every form element must have:

- Associated label
- Clear validation messages
- Accessible error messages
- Keyboard support

Never use placeholder text instead of labels.

Required fields must be clearly identified.

Validation errors must explain how to fix the problem.

---

# Buttons

Buttons must:

- Be real `<button>` elements.
- Have descriptive text.
- Be keyboard accessible.
- Have visible focus styles.

Do not use `<div>` or `<span>` as buttons.

---

# Links

Links must:

- Have descriptive text.
- Clearly indicate their destination.
- Be distinguishable from normal text.

Avoid generic labels such as:

- Click Here
- More
- Read More

---

# Keyboard Navigation

Every interactive element must be accessible using only the keyboard.

Support:

- Tab
- Shift + Tab
- Enter
- Space
- Escape
- Arrow Keys (where appropriate)

Focus order must be logical.

Never remove focus outlines.

---

# Focus Management

Focus must:

- Always remain visible.
- Move logically.
- Return correctly after dialogs close.

Avoid keyboard traps.

---

# Images

Every image must include:

- Meaningful alt text

Decorative images should use:

```html
alt=""
```

Do not repeat nearby visible text inside alt attributes.

---

# SVG Accessibility

Accessible SVGs must include:

- title
- desc
- aria-label (when appropriate)

Interactive SVG elements must support keyboard navigation.

---

# Tables

Tables should be used only for tabular data.

Every table must include:

- Caption (when appropriate)
- Table headers
- Scope attributes

Never use tables for layout.

---

# Headings

Maintain a logical heading hierarchy.

Correct example:

```
H1

H2

H3

H3

H2
```

Do not skip heading levels.

---

# Color

Never rely solely on color to communicate information.

Provide:

- Text
- Icons
- Patterns

Minimum contrast ratio:

- Normal text: 4.5:1
- Large text: 3:1

---

# Typography

Minimum body text size:

16px

Maintain readable:

- Line height
- Paragraph spacing
- Character spacing

Avoid long line lengths.

---

# Motion

Respect user preferences.

Support:

```css
prefers-reduced-motion
```

Avoid unnecessary animations.

---

# Responsive Design

Every page must work on:

- Desktop
- Tablet
- Mobile

Touch targets must be at least:

44 × 44 px

---

# Screen Reader Support

Verify compatibility with:

- NVDA
- JAWS
- VoiceOver

Provide:

- Meaningful labels
- Proper landmarks
- ARIA only when necessary

Prefer semantic HTML over ARIA.

---

# ARIA

Use ARIA only when semantic HTML cannot solve the problem.

Avoid unnecessary ARIA attributes.

Incorrect ARIA is worse than no ARIA.

---

# Accessibility Testing

Accessibility should be verified using:

- axe-core
- Lighthouse
- Keyboard Navigation
- Screen Reader Testing

Manual testing is required.

Automated tools are not sufficient.

---

# Django Guidelines

Templates must:

- Use semantic HTML
- Display accessible form errors
- Include CSRF protection
- Support keyboard navigation

Forms should use Django validation messages.

---

# FOOD Project Requirements

Recipe pages must include:

- Accessible ingredient lists
- Ordered cooking steps
- Accessible nutrition information
- Proper heading hierarchy
- Accessible images

Province map must:

- Support keyboard navigation
- Include accessible labels
- Provide screen reader descriptions
- Display visible focus indicators

Search must:

- Be fully keyboard accessible
- Provide accessible suggestions
- Announce search results

---

# Performance

Accessibility improvements must not significantly reduce performance.

Prefer:

- Native HTML
- Lightweight JavaScript
- Progressive Enhancement

---

# Forbidden Practices

Never:

- Remove focus outlines
- Use div as button
- Use placeholder instead of label
- Depend only on color
- Skip heading levels
- Hide important content from screen readers
- Block keyboard navigation
- Use inaccessible modal dialogs
- Disable browser zoom
- Use autoplay media with sound

---

# Best Practices

Always:

- Use semantic HTML
- Keep interfaces simple
- Write descriptive labels
- Provide meaningful alt text
- Test with keyboard only
- Validate contrast ratios
- Respect reduced motion settings
- Support screen readers
- Keep navigation predictable

---

# References

Additional documentation is available in:

- references/

Automation utilities are available in:

- scripts/

Project-specific accessibility rules take precedence over general recommendations.