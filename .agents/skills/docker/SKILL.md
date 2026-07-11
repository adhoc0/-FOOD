---
name: docker
description: Docker development, containerization, Docker Compose, image optimization, networking, volumes, and deployment standards for the FOOD project.
---

# Docker

## Purpose

This skill defines the Docker standards for the FOOD project.

All containerized services must be:

- Reproducible
- Secure
- Lightweight
- Maintainable
- Production Ready

---

# General Principles

Always prioritize:

1. Security
2. Simplicity
3. Small Image Size
4. Fast Build Times
5. Reproducibility

Avoid unnecessary complexity.

---

# Container Philosophy

Each container should have a single responsibility.

Examples:

- Django
- PostgreSQL
- Redis
- Nginx
- Celery
- Celery Beat

Do not combine unrelated services into a single container.

---

# Docker Images

Prefer official images whenever possible.

Examples:

- python
- postgres
- redis
- nginx

Avoid unofficial or unmaintained images.

---

# Image Optimization

Always:

- Use slim images.
- Minimize image size.
- Remove unnecessary packages.
- Remove build dependencies after installation.
- Combine RUN instructions when appropriate.
- Use .dockerignore.

Avoid large base images unless required.

---

# Multi-Stage Builds

Use multi-stage builds whenever they reduce image size.

Keep runtime images clean.

Never include development tools in production images.

---

# Dockerfile

Dockerfiles should:

- Be readable.
- Be deterministic.
- Use explicit versions.
- Minimize layers.
- Use COPY instead of ADD unless necessary.

Avoid duplicate commands.

---

# Python Containers

Always:

- Install dependencies from requirements files.
- Disable bytecode generation.
- Enable unbuffered output.
- Run collectstatic during deployment.
- Run migrations separately.

Avoid running unnecessary commands during startup.

---

# User Permissions

Never run containers as root unless absolutely necessary.

Create a dedicated application user.

Use least privilege.

---

# Environment Variables

Store configuration in environment variables.

Never hardcode:

- Passwords
- API Keys
- Secret Keys
- Tokens

Use .env files for development.

---

# Secrets

Use secure secret management.

Do not commit:

- .env
- certificates
- credentials

Secrets must remain outside the repository.

---

# Networking

Use Docker networks.

Do not expose unnecessary ports.

Only expose services that require external access.

Prefer internal communication between containers.

---

# Volumes

Persist data using volumes.

Examples:

- PostgreSQL
- Media Files
- Logs

Do not store persistent data inside containers.

---

# Docker Compose

Use docker-compose for local development.

Separate:

- Development
- Testing
- Production

Compose files should remain readable.

---

# Health Checks

Every long-running service should define a health check.

Health checks should verify:

- Service availability
- Database connectivity
- Application readiness

---

# Logging

Use stdout and stderr.

Do not write logs directly into containers.

Centralize logging whenever possible.

---

# Static Files

Static files should be collected during deployment.

Serve static files through Nginx.

---

# Media Files

Persist uploaded media using volumes or external object storage.

Never store uploaded files inside ephemeral containers.

---

# Database

PostgreSQL data must always use persistent volumes.

Backups should never depend on container lifetime.

---

# Performance

Optimize:

- Build cache
- Layer ordering
- Dependency installation
- Image size
- Startup time

Avoid unnecessary rebuilds.

---

# Security

Always:

- Scan images for vulnerabilities.
- Use trusted base images.
- Update dependencies regularly.
- Remove unused packages.
- Minimize attack surface.

---

# Deployment

Production containers must:

- Use DEBUG=False
- Use HTTPS
- Run behind Nginx
- Restart automatically
- Include health checks

---

# Backup

Database backups must be independent of containers.

Verify restore procedures periodically.

---

# Monitoring

Production deployments should support:

- Health checks
- Logging
- Metrics
- Error monitoring

---

# Naming Conventions

Use descriptive names.

Examples:

- food-web
- food-db
- food-nginx
- food-redis

Avoid generic names.

---

# Forbidden Practices

Never:

- Run as root
- Commit .env files
- Hardcode secrets
- Store persistent data inside containers
- Use latest tag in production
- Expose unnecessary ports
- Disable health checks
- Build production images with development dependencies
- Install unnecessary packages

---

# Best Practices

Always:

- Keep images small.
- Keep builds reproducible.
- Use explicit versions.
- Use Docker volumes.
- Use health checks.
- Follow least privilege.
- Document Docker configuration.
- Separate development and production environments.

---

# AI Guidelines

Before generating Docker configuration:

- Reuse existing Docker files.
- Avoid unnecessary containers.
- Minimize image size.
- Follow Docker best practices.
- Respect project architecture.
- Generate production-ready configurations.
- Never expose secrets.
- Keep Docker Compose files maintainable.

---

# References

Additional Docker documentation is available in:

references/

Reusable automation scripts are available in:

scripts/

Project-specific rules always take precedence over general Docker best practices.