---
name: seo
description: Search Engine Optimization standards, structured data, metadata, content optimization, technical SEO, Core Web Vitals, and search engine best practices for the FOOD project.
---

# SEO

## Purpose

This skill defines the Search Engine Optimization (SEO) standards for the FOOD project.

All pages must prioritize:

- Crawlability
- Indexability
- Accessibility
- User Experience
- Performance
- High-Quality Content

SEO improvements should always benefit users first.

---

# General Principles

Always prioritize:

1. Content Quality
2. Technical SEO
3. User Experience
4. Performance
5. Accessibility
6. Maintainability

Follow Google's Search Essentials.

Avoid manipulative SEO techniques.

---

# Content

Every page should provide:

- Original content
- Useful information
- Clear structure
- Logical hierarchy

Avoid duplicate or low-quality content.

---

# Metadata

Every page should include:

- Title
- Meta Description
- Canonical URL
- Robots Meta (when required)

Metadata must accurately describe page content.

---

# Titles

Titles should:

- Be unique
- Be descriptive
- Reflect page intent
- Contain primary keywords naturally

Avoid clickbait.

---

# Meta Descriptions

Descriptions should:

- Summarize page content
- Encourage clicks naturally
- Remain unique

Avoid keyword stuffing.

---

# URL Structure

URLs should be:

- Short
- Readable
- Stable
- Lowercase

Use hyphens instead of underscores.

Avoid unnecessary parameters.

---

# Headings

Maintain a logical heading structure.

Use:

- One H1
- Hierarchical H2
- Hierarchical H3

Never skip heading levels.

---

# Structured Data

Use JSON-LD.

Implement appropriate Schema.org types.

Examples:

- Recipe
- BreadcrumbList
- Organization
- WebSite
- FAQPage

Validate all structured data.

---

# Breadcrumbs

Every content page should provide breadcrumb navigation.

Breadcrumbs should match the URL hierarchy.

---

# Internal Linking

Create meaningful internal links.

Link related:

- Recipes
- Categories
- Provinces
- Ingredients

Avoid orphan pages.

---

# Images

Images should:

- Include descriptive alt text
- Use meaningful filenames
- Be optimized
- Support lazy loading

Prefer WebP or AVIF when appropriate.

---

# Sitemap

Maintain a valid XML sitemap.

Include only indexable pages.

Update automatically after content changes.

---

# Robots

Use robots.txt to control crawler access.

Never block important public pages accidentally.

---

# Canonical URLs

Every indexable page should define a canonical URL.

Avoid duplicate canonical references.

---

# Pagination

Large content collections must support pagination.

Use descriptive navigation.

Avoid excessively deep pagination.

---

# Search Pages

Search result pages should generally not be indexed unless there is a clear SEO strategy.

---

# Recipe Pages

Recipe pages should include:

- Title
- Description
- Ingredients
- Instructions
- Preparation Time
- Cooking Time
- Servings
- Nutrition Information (if available)
- Images
- Breadcrumbs
- Structured Data

---

# Province Pages

Province pages should include:

- Province Name
- Region
- Description
- Recipe List
- Pagination
- Breadcrumbs

---

# Category Pages

Category pages should include:

- Category Name
- Description
- Recipe List
- Breadcrumbs

---

# Content Quality

Write for users first.

Avoid:

- Duplicate content
- Thin content
- Automatically generated spam
- Hidden text

Prioritize helpful content.

---

# Keyword Usage

Use keywords naturally.

Include primary keywords in:

- Title
- H1
- Meta Description
- Opening Paragraph
- Image Alt Text (when appropriate)

Avoid keyword stuffing.

---

# Core Web Vitals

Optimize:

- Largest Contentful Paint (LCP)
- Interaction to Next Paint (INP)
- Cumulative Layout Shift (CLS)

Monitor these metrics regularly.

---

# Mobile SEO

Every page must:

- Be responsive
- Load efficiently
- Support touch navigation
- Avoid horizontal scrolling

---

# Accessibility

SEO should support accessibility.

Use:

- Semantic HTML
- Proper heading hierarchy
- Descriptive links
- Accessible images

---

# Performance

Reduce:

- Page Load Time
- Render Blocking Resources
- Unused CSS
- Unused JavaScript

Optimize critical rendering paths.

---

# Security

Serve all public pages over HTTPS.

Avoid mixed content.

Protect user privacy.

---

# Analytics

Monitor:

- Organic Traffic
- Click-Through Rate (CTR)
- Index Coverage
- Search Performance
- Core Web Vitals

Use data to guide improvements.

---

# FOOD Project Requirements

Optimize:

- Homepage
- Recipe Pages
- Province Pages
- Category Pages
- Search Functionality
- Turkey Map Navigation

Every public page should be discoverable and properly linked.

---

# Forbidden Practices

Never:

- Stuff keywords
- Create duplicate pages
- Cloak content
- Hide text
- Buy links
- Use doorway pages
- Publish thin content
- Generate misleading metadata
- Ignore canonical URLs
- Block important pages unintentionally

---

# Best Practices

Always:

- Write unique content.
- Use semantic HTML.
- Optimize metadata.
- Implement structured data.
- Maintain internal links.
- Optimize images.
- Improve Core Web Vitals.
- Monitor search performance.
- Follow Google Search Essentials.

---

# AI Guidelines

Before generating SEO-related code or content:

- Prioritize users over search engines.
- Generate unique metadata.
- Use structured data appropriately.
- Avoid duplicate content.
- Follow semantic HTML.
- Respect project architecture.
- Improve crawlability.
- Improve indexability.
- Generate production-ready SEO implementations.

---

# References

Additional SEO documentation is available in:

references/

Reusable automation scripts are available in:

scripts/

Project-specific rules always take precedence over general SEO best practices.