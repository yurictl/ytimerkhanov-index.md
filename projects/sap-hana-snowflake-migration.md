# SAP HANA to AWS / Snowflake Migration

- **Company:** EPAM
- **Year / Duration:** 2023, 8 months
- **Stack:** Terraform, CloudFormation, GitHub Actions, GitLab CI/CD, ECS, Aurora DB, DynamoDB, VPC, IAM, Snowflake
- **Role:** DevOps lead for a team of 10; owned all AWS infrastructure work

## Problem

A large pharmaceutical company needed to migrate its Marketing Analytics Reporting System from SAP HANA to a cloud-native AWS + Snowflake stack. At the same time, GitLab support was ending — forcing a simultaneous pipeline migration to GitHub. The infrastructure situation was messy: 200+ AWS resources described partly in nested CloudFormation stacks and partly managed manually, with only 70% code coverage. Application parameters were scattered across multiple locations including the application code itself.

## What I Did

- Rewrote 3,500 lines of CloudFormation into reusable Terraform modules
- Imported all 200+ AWS resources without drift and without disrupting the team's ongoing development work
- Migrated CI/CD pipelines from GitLab to GitHub, rebuilding all environments on fresh AWS accounts
- Centralized all environment-specific configuration into GitHub configs and secrets (previously scattered in application code and multiple repos)
- Conducted knowledge transfer for the operations team at project close

The migration from CloudFormation to Terraform was not just a rewrite — nested CloudFormation stacks made the infrastructure hard to reason about and slow to change. Terraform modules made dependencies explicit and reusable across environments.

## Outcome

- Project delivered on schedule
- Infrastructure code coverage: 70% → 95%
- Infrastructure costs reduced by 3x+
- Deployments 4x faster
- Clean knowledge transfer: operations team able to continue independently
