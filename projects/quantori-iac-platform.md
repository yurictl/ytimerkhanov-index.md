# Quantori IaC Platform — Multi-Database Provisioning & CI/CD Standardization

- **Company:** Quantori
- **Year / Duration:** 2024–2025 (ongoing)
- **Stack:** Terraform, Terratest, Checkov, GitHub Actions, Roadie (Backstage), Aurora, PostgreSQL, Oracle
- **Role:** Senior System Engineer; owned IaC quality, database provisioning automation, and hiring pipeline tooling

## Problem

30+ Terraform modules with no shared testing standard — each team applied different patterns, making cross-team reuse fragile and code review slow. Database provisioning (Aurora, PostgreSQL, Oracle) across environments was manual: no Day-0 automation, no unified configuration baseline, high risk of human error. Junior DevOps hiring was ad hoc with no structured onboarding pipeline.

## What I Did

**IaC testing framework**
- Built a unified CI/CD and end-to-end testing framework for all 30+ Terraform modules
- Standardized reusable Terratest patterns across teams — reduced variance in module structure and made reviews predictable

**Multi-database provisioning**
- Standardized provisioning and configuration for Aurora, PostgreSQL, and Oracle across all environments
- Automated Day-0 database setup via GitHub Actions and Roadie (Backstage) templates — developers request a database and get a ready-to-use instance without involving ops

**Hiring and knowledge pipeline**
- Streamlined the technical interview process: unified question sets, evaluation forms, and structured feedback templates
- Co-developed Cloud/DevOps School curriculum and practical labs — created a repeatable internal source of junior DevOps talent

## Outcome

- Development time across Terraform modules reduced 2–3× through standardized workflows and reusable patterns
- Operational overhead for database provisioning cut ~40%; manual error risk minimized
- Interview throughput and TA pipeline efficiency improved ~30%
