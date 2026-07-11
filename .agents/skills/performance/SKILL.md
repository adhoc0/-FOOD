---
name: performance
description: Performance engineering, profiling, optimization, scalability, caching, database tuning, frontend optimization, and performance standards for the FOOD project.
---

# Performance

## Purpose

This skill defines the performance engineering standards for the FOOD project.

Performance optimization must improve measurable results while preserving:

- Correctness
- Maintainability
- Readability
- Security

Never sacrifice code quality for insignificant performance gains.

---

# General Principles

Always prioritize:

1. Correctness
2. Simplicity
3. Maintainability
4. Performance
5. Scalability

Measure first.

Optimize second.

Never optimize based on assumptions.

---

# Performance Philosophy

Optimization must always be supported by measurable evidence.

Avoid premature optimization.

Optimize only where bottlenecks exist.

Maintain readable and maintainable code.

---

# Performance Workflow

Always follow this order:

Measure

↓

Identify Bottleneck

↓

Optimize

↓

Measure Again

↓

Document Results

---

# Backend Performance

Review:

- Response Time
- Throughput
- CPU Usage
- Memory Usage
- I/O Operations
- Database Queries

---

# Database

Always prefer Django ORM.

Optimize:

- Query Count
- Query Complexity
- Index Usage
- JOIN Performance
- Filtering
- Ordering
- Aggregation

Avoid unnecessary queries.

---

# ORM

Always review:

- N+1 Queries
- Duplicate Queries
- Missing Indexes

Use:

- select_related()
- prefetch_related()

when appropriate.

Avoid unnecessary ORM evaluations.

---

# Caching

Cache only when measurable benefit exists.

Possible cache layers:

- View Cache
- Template Cache
- Fragment Cache
- Low-Level Cache

Document cache invalidation strategy.

---

# Memory

Avoid:

- Large in-memory collections
- Duplicate objects
- Unnecessary copies

Prefer lazy evaluation whenever practical.

---

# CPU

Optimize:

- Expensive loops
- Nested iterations
- Repeated calculations

Avoid unnecessary computations.

---

# File Processing

Process files incrementally whenever possible.

Avoid loading large files entirely into memory.

---

# Network

Minimize:

- HTTP Requests
- Payload Size
- Redirect Chains

Enable compression where appropriate.

---

# Frontend

Optimize:

- HTML
- CSS
- JavaScript
- Images
- Fonts

Reduce unnecessary assets.

---

# Images

Prefer:

- WebP
- AVIF

Compress images before deployment.

Implement lazy loading.

Serve responsive images.

---

# CSS

Minimize CSS.

Remove unused styles.

Avoid unnecessary selectors.

Prefer reusable styles.

---

# JavaScript

Reduce bundle size.

Avoid unnecessary libraries.

Prefer native browser APIs.

Defer non-critical scripts.

---

# Core Web Vitals

Review:

- Largest Contentful Paint (LCP)
- Interaction to Next Paint (INP)
- Cumulative Layout Shift (CLS)

Optimize only measurable bottlenecks.

---

# Static Assets

Compress:

- CSS
- JavaScript
- SVG

Enable browser caching.

---

# Django Templates

Reduce template complexity.

Avoid unnecessary template tags.

Reuse components.

---

# API Performance

Review:

- Response Time
- Payload Size
- Pagination
- Filtering
- Serialization

Avoid returning unnecessary data.

---

# Pagination

Always paginate large datasets.

Avoid returning entire collections.

---

# Logging

Avoid excessive logging.

Never log inside performance-critical loops.

---

# Profiling

Use profiling tools before optimization.

Measure:

- Execution Time
- Query Count
- Memory Usage
- CPU Usage

---

# Scalability

Design for growth.

Review:

- Database Growth
- Concurrent Users
- Background Jobs
- Queue Processing

Avoid solutions that scale poorly.

---

# Docker

Optimize:

- Image Size
- Build Cache
- Startup Time

Keep runtime containers lightweight.

---

# Nginx

Enable:

- Compression
- Browser Caching
- Static File Optimization

Optimize reverse proxy configuration.

---

# PostgreSQL

Review:

- Indexes
- Query Plans
- Sequential Scans
- Lock Contention
- Transactions

Keep transactions short.

---

# Testing

Performance improvements should be verified through testing.

Possible tests:

- Benchmark Tests
- Load Tests
- Stress Tests
- Profiling Sessions

---

# Performance Metrics

Measure whenever applicable:

- Response Time
- Throughput
- Requests Per Second
- Memory Usage
- CPU Usage
- Database Query Count
- Query Execution Time
- Cache Hit Ratio
- Page Load Time
- Core Web Vitals

---

# FOOD Project Requirements

Optimize:

- Recipe Search
- Province Filtering
- Category Filtering
- Homepage
- Turkey SVG Map
- Recipe Images
- Pagination
- Search Suggestions

Large recipe collections must always be paginated.

---

# Forbidden Practices

Never:

- Optimize without profiling
- Duplicate expensive queries
- Ignore N+1 problems
- Cache everything
- Optimize microseconds while ignoring seconds
- Load entire datasets unnecessarily
- Use unnecessary libraries
- Increase complexity for insignificant gains
- Sacrifice readability for premature optimization

---

# Best Practices

Always:

- Measure before optimizing.
- Keep code simple.
- Optimize database queries.
- Use pagination.
- Compress assets.
- Optimize images.
- Minimize network requests.
- Profile critical paths.
- Validate improvements after optimization.

---

# AI Guidelines

Before suggesting optimizations:

- Measure the current implementation.
- Identify the actual bottleneck.
- Recommend only measurable improvements.
- Preserve readability.
- Respect project architecture.
- Avoid premature optimization.
- Prefer Django built-in optimizations.
- Avoid unnecessary dependencies.

---

# References

Additional performance documentation is available in:

references/

Reusable automation scripts are available in:

scripts/

Project-specific rules always take precedence over general performance best practices.