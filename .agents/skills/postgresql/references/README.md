# PostgreSQL References

## Purpose

This directory contains reference documentation for PostgreSQL development, administration, optimization, security, backup, replication, and database design used in the FOOD project.

These documents provide implementation guidance, database architecture references, optimization techniques, and best practices for developers and AI agents.

Project-specific PostgreSQL rules are defined in:

../SKILL.md

---

## Scope

Reference documents may cover topics such as:

- PostgreSQL Architecture
- Database Design
- Normalization
- Constraints
- Indexes
- Query Optimization
- Execution Plans
- Transactions
- Locking
- MVCC
- Views
- Materialized Views
- Functions
- Triggers
- Full Text Search
- JSON / JSONB
- Backup and Restore
- Replication
- Partitioning
- Performance Tuning
- Security
- Monitoring

---

## Intended Use

Reference documents should help:

- Explain PostgreSQL concepts.
- Provide implementation examples.
- Document optimization strategies.
- Describe database administration practices.
- Support AI-assisted database development.
- Reduce duplicated knowledge.

---

## Suggested Documents

Examples:

```text
architecture.md
database-design.md
normalization.md
indexes.md
query-optimization.md
execution-plans.md
transactions.md
locking.md
mvcc.md
jsonb.md
full-text-search.md
partitioning.md
backup.md
replication.md
performance.md
security.md
monitoring.md
```

---

## File Naming

Use descriptive lowercase filenames.

Examples:

```text
query-optimization.md
database-design.md
full-text-search.md
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
- Be PostgreSQL-specific.
- Be concise and practical.
- Avoid duplicate information.
- Reference official PostgreSQL documentation whenever appropriate.
- Include SQL examples when useful.
- Be reviewed periodically.

---

## Notes

Do not place project rules in this directory.

Project-specific PostgreSQL standards belong in:

../SKILL.md

Reusable automation belongs in:

../scripts/

Only reference documentation should be stored in this directory.