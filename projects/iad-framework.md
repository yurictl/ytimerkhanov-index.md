# IAD Framework / IDP Platform — FinOps & Monitoring Migration

- **Company:** EPAM
- **Year / Duration:** 2023–2024, ~1 year
- **Stack:** Terraform, Terragrunt, EKS, AKS, Vault, Consul, Jenkins, Prometheus, Grafana, AppDynamics, Azure OpenAI
- **Role:** Senior System Engineer; led multiple workstreams on a large internal developer platform

## Context

The Internal Application Development (IAD) platform was a large-scale internal developer platform shared across the organization: 57 base modules, 293 component modules, 51 AWS accounts, 194 environments. I worked across multiple workstreams on this platform over roughly a year, contributing to module releases, FinOps, and a major monitoring migration.

## Problem

Three monitoring subscriptions — AppDynamics and Splunk — were costing the organization $150,000 per month. Leadership set a hard end-of-year deadline to exit them. No migration plan existed, no one on the team had done this kind of transition before, and the target architecture was undefined at the start. Separately, cloud spend was trending upward with no systematic review process.

## What I Did

Led the proof-of-concept for migrating from AppDynamics to Prometheus + Grafana:

- Started by mapping actual monitoring requirements rather than assuming feature parity
- Identified a neighboring team with a comparable setup and adapted their approach rather than starting from scratch — saved weeks of trial-and-error
- While running cost analysis for the monitoring migration, noticed broader cloud spend anomalies across accounts — ran a full audit of backup policies, idle resources, and usage patterns (outside original task scope)
- Contributed to 25+ major Terraform module releases across the platform lifecycle
- Conducted 15+ technical interviews in 2024 as part of team growth

## Outcome

- POC completed and became the foundation for the full migration plan
- Annual cloud costs reduced by $100,000+, reversing a growing cost trend
- Monitoring migration enabled exit from $150,000/month subscription contracts on deadline
