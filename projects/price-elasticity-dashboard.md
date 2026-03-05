# Price Elasticity Dashboard — MLOps for Pricing Analytics

- **Company:** EPAM
- **Year / Duration:** 2023, 3 months
- **Stack:** Terraform, EKS, GitHub Actions, GitLab CI/CD, ECS, ECR, Kubeflow, Aurora DB, MongoDB, Glue, IAM
- **Role:** Solo DevOps engineer; de facto Solution Architect (no architect on the team)

## Problem

EPAM had an internally developed ML product — a pricing analytics dashboard with price elasticity modeling — sold as a pilot to a client. The client's tech stack was significantly different from the internal demo environment. There was no Solution Architect on the team and no predefined target architecture. The team was small: 1 PM, 1 analyst, 1 full-stack developer, 2 data scientists. The demo deadline was two months out.

## What I Did

- Took ownership of the target architecture from scratch — designed it, wrote all Terraform code for the required AWS resources including an EKS cluster with Kubeflow for ML pipeline orchestration
- Migrated CI/CD pipelines from GitLab to GitHub, adapting to the client's tooling
- Created separate environments for development, testing, and the client presentation
- Mid-project, shifted approach after PM feedback: stopped optimizing for the "correct" long-term architecture and prioritized demo readiness. The right call for the phase — the client's goal was to validate the product, not audit the infrastructure
- Conducted full knowledge transfer to a successor engineer in one week

## Outcome

- Demo delivered on time within two months of active start
- Client approved the product for further development
- Knowledge transfer completed in one week, successor able to continue independently

**Lesson internalized:** The definition of success changes by phase. In a pilot with a hard demo date and no architect, the job is to make the demo work — not to build the ideal architecture. Anchoring to the wrong success criteria would have failed the team.
