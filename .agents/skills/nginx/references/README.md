# Nginx References

## Purpose

This directory contains reference documentation for Nginx configuration, reverse proxy, load balancing, security, performance optimization, and deployment within the FOOD project.

These documents provide implementation guidance, best practices, and architectural references for developers and AI agents.

Project-specific Nginx rules are defined in:

../SKILL.md

---

## Scope

Reference documents may cover topics such as:

- Nginx Architecture
- Reverse Proxy
- Load Balancing
- SSL/TLS
- HTTPS Configuration
- HTTP/2
- HTTP/3
- Static File Serving
- Media File Serving
- Caching
- Compression
- Security Headers
- Rate Limiting
- Logging
- Monitoring
- Performance Optimization
- Docker Integration
- Django Deployment

---

## Intended Use

Reference documents should help:

- Explain Nginx concepts.
- Provide implementation examples.
- Document deployment strategies.
- Describe performance optimization techniques.
- Support AI-assisted infrastructure development.
- Reduce duplicated knowledge.

---

## Suggested Documents

Examples:

```text
architecture.md
reverse-proxy.md
ssl.md
http2.md
http3.md
gzip.md
brotli.md
caching.md
security-headers.md
rate-limiting.md
logging.md
load-balancing.md
docker.md
django.md
performance.md
```

---

## File Naming

Use descriptive lowercase filenames.

Examples:

```text
reverse-proxy.md
security-headers.md
load-balancing.md
```

Avoid:

```text
notes.md
temp.md
misc.md
new.md
```

---

## Guidelines

Reference documents should:

- Focus on a single topic.
- Be Nginx-specific.
- Be concise and practical.
- Avoid duplicate information.
- Reference official Nginx documentation whenever appropriate.
- Be reviewed periodically.
- Remain compatible with current stable Nginx releases.

---

## Notes

Do not place project rules in this directory.

Project-specific Nginx standards belong in:

../SKILL.md

Reusable automation belongs in:

../scripts/

Only reference documentation should be stored in this directory.