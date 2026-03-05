# Chatbot Systems — Internal Employee Chatbot

- **Company:** EPAM
- **Year / Duration:** 2022, 6 months
- **Stack:** Jenkins, Terraform, AWS (SageMaker, Cognito, ECS, ELB, EBS, Route53, Aurora DB), Python
- **Role:** DevOps lead; joined an in-flight project 4 months in

## Problem

A large pharmaceutical company was building an internal chatbot backed by an ML model (SageMaker) and a search engine (Coveo). When I joined, the last release had taken a full month to prepare — it was the only way the team knew how to ship. Three environments (dev, staging, prod) had been set up manually by different people at different times. Configurations were inconsistent across environments, IAM permissions were ad-hoc, and there were no automated deployment pipelines.

## What I Did

- Standardized IAM roles across all three environments — rewrote the permission model so all environments matched a single baseline
- Rewrote the Terraform infrastructure code from scratch, recreating some resources and importing others to eliminate drift
- Resolved the hardest blocker: Cognito configuration that required cross-team manual coordination. Worked through the request processes systematically rather than creating workarounds
- Built Jenkins CI/CD pipelines from scratch for all environments, including automated tests and static code analysis
- Did all of this without blocking the development team's ongoing work

## Outcome

- Release frequency: monthly → weekly
- Releases became stable and predictable — the team could ship new features without DevOps becoming a bottleneck
- Environment configurations became consistent across dev, staging, and production
