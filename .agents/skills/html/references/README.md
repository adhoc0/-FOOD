# HTML Skill Reference Documentation

This directory contains reference documentation for the HTML skill, detailing HTML standards, best practices, and project-specific guidelines.

## Table of Contents

- [HTML5 Semantic Elements](#html5-semantic-elements)
- [ARIA Roles for Accessibility](#aria-roles-for-accessibility)
- [Best Practices Checklist](#best-practices-checklist)
- [Project-Specific Guidelines](#project-specific-guidelines)

---

## HTML5 Semantic Elements

Semantic HTML improves SEO and accessibility by using elements that describe their meaning.

| Element | Purpose |
|---------|---------|
| `<header>` | Introductory content for a section or page |
| `<nav>` | Navigation links |
| `<main>` | Main content of the document |
| `<article>` | Self-contained content (e.g., blog post, news story) |
| `<section>` | Thematic grouping of content |
| `<aside>` | Tangential content (e.g., sidebar) |
| `<footer>` | Concluding content for a section or page |
| `<figure>` and `<figcaption>` | Images, diagrams, code samples with captions |

**When to use:**
- Use `<main>` once per page for the primary content
- Use `<article>` for independent content like blog posts or product listings
- Use `<section>` for thematic groupings that need headings
- Use `<nav>` for primary navigation menus

---

## ARIA Roles for Accessibility

ARIA (Accessible Rich Internet Applications) roles supplement HTML5 semantic elements to improve accessibility for assistive technologies.

### Common ARIA Roles

| Role | Purpose |
|------|---------|
| `navigation` | Landmarks for navigation sections |
| `main` | Main content landmark |
| `complementary` | Sidebars and tangential content |
| `banner` | Header or site-wide announcement |
| `contentinfo` | Footer or site-wide information |
| `search` | Search functionality |
| `alert` | Important, time-sensitive messages |
| `status` | Updates that don't require user action |
| `dialog` | Modal dialogs or popups |
| `tab`, `tablist`, `tabpanel` | Tab interface |
| `tooltip` | Helpful information revealed on hover |

### ARIA States and Properties

| Property | Usage |
|----------|-------|
| `aria-label="text"` | Provides accessible name when no visible text exists |
| `aria-labelledby="id"` | Associates an element with a label element |
| `aria-describedby="id"` | Associates an element with a description |
| `aria-expanded="true/false"` | Indicates expandable/collapsible state |
| `aria-hidden="true/false"` | Hides/shows elements from screen readers |
| `aria-live="polite/assertive"` | Defines live regions for dynamic updates |
| `aria-haspopup="dialog/menu/true"` | Indicates element opens a popup |
| `aria-required="true/false"` | Indicates required form fields |

**When to use:**
- Use `aria-label` on buttons with only icons
- Use `aria-expanded` on accordion headers and disclosure widgets
- Use `aria-live` for real-time notifications (e.g., form submission status)
- Use `role="dialog"` on modal windows with `aria-modal="true"`

---

## Best Practices Checklist

### HTML Best Practices

- [ ] Use semantic HTML5 elements (e.g., `<header>`, `<nav>`, `<main>`, `<article>`, `<section>`) instead of generic `<div>` elements
- [ ] Include proper `lang` attribute on `<html>` tag (e.g., `<html lang="en">`)
- [ ] Add `charset="UTF-8"` to `<meta>` tag in `<head>`
- [ ] Set appropriate `<title>` tag for each page
- [ ] Use `<meta name="viewport" content="width=device-width, initial-scale=1.0">` for responsive design
- [ ] Include `alt` attributes for all `<img>` tags
- [ ] Use `<h1>` for main page heading, one per page only
- [ ] Nest headings properly (e.g., `<h1>` -> `<h2>` -> `<h3>`)
- [ ] Link related pages using semantic HTML (not just `<div>` with `onclick`)
- [ ] Validate HTML using W3C Validator

### Accessibility (A11y) Best Practices

- [ ] Provide keyboard navigation for all interactive elements
- [ ] Use proper focus management for modals and dynamic content
- [ ] Ensure sufficient color contrast (WCAG AA minimum: 4.5:1 for normal text, 3:1 for large text)
- [ ] Use `<button>` for actions and `<a>` for navigation
- [ ] Add `aria-label` to icon-only buttons
- [ ] Use `aria-expanded` for expandable/collapsible content
- [ ] Use `aria-live` for real-time updates
- [ ] Ensure form fields have associated `<label>` elements
- [ ] Use `fieldset` and `legend` for related form controls
- [ ] Test with screen readers (e.g., NVDA, VoiceOver, JAWS)

### Performance Best Practices

- [ ] Optimize images (compress, use appropriate formats like WebP, implement lazy loading)
- [ ] Minify HTML files
- [ ] Avoid excessive nested tables (max 3-4 levels)
- [ ] Use CSS for layout, not HTML tables
- [ ] Enable browser caching for static assets
- [ ] Use `async` or `defer` attributes for non-critical JavaScript
- [ ] Implement lazy loading for offscreen content
- [ ] Use content delivery networks (CDNs) for static assets

---

## Project-Specific Guidelines

### Component Architecture

- Use component-based architecture
- Each component should be self-contained with HTML, CSS, and JS (if needed)
- Use semantic HTML for component structure
- Maintain consistent HTML structure across components
- Follow the naming conventions defined in [SKILL.md](../SKILL.md)

### HTML Standards

- All HTML files must validate without errors
- UTF-8 encoding is mandatory
- At least one heading (`<h1>`-`<h6>`) per page
- Maximum one `<h1>` per page
- Semantic HTML preferred over generic `<div>`
- CSS classes should follow BEM methodology
- All interactive elements must be keyboard accessible
- Forms must have proper labels and validation

### Accessibility Requirements

- WCAG 2.1 AA compliance minimum
- Keyboard navigation support for all components
- ARIA attributes used where needed
- Color contrast ratio of 4.5:1 or higher
- Focus states clearly visible
- Screen reader testing required

---

## Useful Tools

### Validators and Testing Tools

- [W3C HTML Validator](https://validator.w3.org/) - Validate HTML standards
- [Lighthouse](https://developers.google.com/web/tools/lighthouse) - Performance and accessibility audits
- [ axe DevTools](https://www.deque.com/axe/browser-extensions/) - Accessibility testing extension
- [ WAVE Accessibility Tool](https://wave.webaim.org/) - Visual accessibility checker

### Browser Developer Tools

- [Chrome DevTools](https://developer.chrome.com/docs/devtools) - Comprehensive web development tools
- [Firefox Developer Tools](https://developer.mozilla.org/en-US/docs/Tools) - Firefox-specific development tools
- [Edge DevTools](https://docs.microsoft.com/en-us/microsoft-edge/devtools-guide-chromium) - Edge development tools
- [Safari Web Inspector](https://developer.apple.com/safari/tools/) - Safari development tools

### Design and Accessibility Resources

- [Web Content Accessibility Guidelines (WCAG)](https://www.w3.org/WAI/standards-guidelines/wcag/)
- [Material Design Accessibility Guidelines](https://material.io/design/usability/accessibility.html)
- [Color Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [MDN Web Docs](https://developer.mozilla.org/en-US/)

---

## Notes

This reference documentation should be used in conjunction with [SKILL.md](../SKILL.md) which contains project-specific implementation guidelines. Refer to [SKILL.md](../SKILL.md) for information on:

- Component architecture
- Naming conventions
- Folder structure
- Development workflow
