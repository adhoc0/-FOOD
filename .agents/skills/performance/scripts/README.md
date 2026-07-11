# Performance Scripts

## Purpose

This directory contains reusable automation scripts for measuring, analyzing, validating, and improving application performance within the FOOD project.

Scripts are intended to automate performance testing, identify bottlenecks, generate reports, and support developers and AI agents throughout the development lifecycle.

Project-specific performance standards are defined in:

../SKILL.md

Reference documentation is available in:

../references/

---

## Intended Use

Scripts in this directory may be used to:

- Benchmark application performance
- Profile CPU usage
- Profile memory usage
- Analyze database queries
- Detect N+1 queries
- Measure page load times
- Validate Core Web Vitals
- Analyze API response times
- Verify caching effectiveness
- Analyze static asset performance
- Generate performance reports
- Prepare production performance audits

---

## Script Categories

Supported script categories include:

- Benchmarking
- Profiling
- Database Analysis
- ORM Analysis
- Query Analysis
- Cache Validation
- Memory Analysis
- CPU Analysis
- API Performance
- Frontend Performance
- Core Web Vitals
- Load Testing
- Stress Testing
- Performance Reporting
- Production Verification

---

## Suggested Scripts

Examples:

```text
benchmark.py
profile-cpu.py
profile-memory.py
query-analysis.py
orm-analysis.py
cache-check.py
api-performance.py
core-web-vitals.py
load-test.py
stress-test.py
performance-report.py
production-check.py
```

---

## Naming Convention

Use descriptive lowercase filenames.

Examples:

```text
benchmark.py
query-analysis.py
load-test.py
```

Avoid:

```text
script.py
temp.py
new.py
test.py
```

---

## Script Requirements

Every script should:

- Perform one specific task.
- Be reusable.
- Produce clear and readable output.
- Exit with appropriate status codes.
- Handle errors gracefully.
- Avoid hardcoded paths.
- Support automation.
- Generate measurable results whenever possible.

---

## Cross-Platform Support

Whenever possible, support multiple operating systems.

Preferred languages:

- Python
- Bash (.sh)
- PowerShell (.ps1)

Avoid operating system-specific assumptions.

---

## Guidelines

Scripts should:

- Follow project coding standards.
- Be idempotent whenever possible.
- Validate input before execution.
- Log meaningful errors.
- Minimize external dependencies.
- Produce consistent output.
- Support CI/CD pipelines.
- Avoid modifying production data unless explicitly intended.

---

## Performance Metrics

Whenever applicable, scripts should measure:

- Execution Time
- Response Time
- Throughput
- Memory Usage
- CPU Usage
- Database Query Count
- Query Execution Time
- Cache Hit Ratio
- Core Web Vitals
- Resource Utilization

---

## Notes

This directory contains executable automation scripts only.

Project-specific performance rules belong in:

../SKILL.md

Reference documentation belongs in:

../references/

Do not store documentation, configuration files, benchmark results, logs, or application source code in this directory.