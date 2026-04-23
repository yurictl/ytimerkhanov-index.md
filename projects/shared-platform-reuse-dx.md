# Enterprise R&D Data Platform — Fast Prototyping on Shared Corporate Infrastructure

- **Company:** Quantori (enterprise client under NDA)
- **Year / Duration:** 2025–2026 (ongoing)
- **Stack:** AWS (Aurora PostgreSQL Serverless v2, S3, SQS, ECR, Secrets Manager, KMS, IRSA), EKS (shared multi-tenant), Argo Workflows + Argo Events, ArgoCD, GitLab CI/CD, Terraform, Kustomize, Helm, Python 3.12 / FastAPI, OpenSearch, Trivy, SonarCloud, Claude Code
- **Role:** Lead DevOps on the primary R&D data platform; Architect on a parallel greenfield project that reused the same operating framework

## Problem

A large enterprise R&D organization commissioned a greenfield data platform — ingestion pipelines, domain-specific search, and application APIs — under tight constraints:

- Private subnets only; ingress via Site-to-Site VPN
- Shared corporate VPC — contractors cannot create their own VPC
- Shared multi-tenant EKS cluster — we get a namespace, not a cluster
- Multiple contractor organizations on the same AWS account with no pre-existing conventions for naming, IAM, secrets, or CI patterns

Standing up a custom platform from scratch would have burned sprints on provisioning before a single domain feature shipped. In parallel, a second greenfield project with a different product scope kicked off in a separate AWS account with near-identical documentation, operations, and onboarding needs — risking every team reinventing the same foundation.

## What I Did

**Fast prototyping on shared infrastructure**

- Split the application into six focused repositories so product teams could move in parallel from day one
- Shipped Phase 1 on the shared corporate EKS cluster and VPC — no waiting on infrastructure provisioning. The platform carries a serverless Postgres cluster, workflow orchestration (Argo Workflows + Argo Events), FastAPI services, a full-text search engine, and a domain-specific search service
- Accepted a pragmatic CD pivot mid-flight and captured it as an ADR: started with GitLab CI + `kubectl`/`kustomize` because GitOps tooling wasn't available on the shared cluster yet; switched to ArgoCD on the corporate platform once the upstream EKS module shipped. The ADR chain records the supersede without rewriting working code

**Reuse of the corporate platform**

- Forked and adapted the client's central DevOps platform repositories (EKS Terraform module, IAM framework, Helm chart, GitLab pipeline templates, manifests) into a local workspace. Kept project-specific adaptations visible on top of upstream instead of building a parallel platform
- Adopted the central GitLab pipeline templates for Terraform repositories rather than writing from scratch — inherited DB bootstrap, stage determination, and security scanning for free
- Managed IAM for the application services through the existing corporate IAM framework via IRSA — the same role model every other tenant on the platform already uses
- Clean separation: app-level Terraform creates only app-level resources; base infra stays in the corporate platform repos and syncs via ArgoCD on a cluster the platform team provisions

**Developer experience**

- Established a 3+1 documentation framework (Orientation / Operations / Decisions / WIP) applied identically across all three workspaces (primary app, infra, sister project). One project card per workspace, one doc per topic, ADRs for decisions, WIP for time-bounded investigations that must graduate on close or be deleted
- Wrote a small Python CLI plus Makefile targets (`make docs-check`, `make docs-index`) to scaffold new docs with correct frontmatter, validate links, flag stale docs, and regenerate the project index
- Authored operational runbooks covering the non-obvious parts: contractor VPN access, a self-hosted GitLab Runner inside the VPC for DB bootstrap jobs, IAM role provisioning via the central framework, container hardening (non-root user), a two-job ECR auth pattern using official images instead of a custom CI image, container scanning, and static analysis onboarding
- Replicated the framework end-to-end on the sister project in a different AWS account with a different team — same Makefile, same docs CLI, same ADR cadence

## Outcome

- Primary platform reached a functional Phase 1 on shared corporate infrastructure without provisioning a custom VPC or cluster — foundational infra work avoided by reusing what the platform team already had
- 9 ADRs capture every architectural decision (including the mid-project CD pivot) so new contributors can read *why* instead of asking
- 19 operations documents cover the developer lifecycle end-to-end — network access, AWS cost reference, IAM, cluster reference, GitLab workflow, CI templates, self-hosted runner, K8s quotas, monitoring, naming/tagging, container hardening, scanning
- Two greenfield projects run on the same documentation, tooling, and Makefile framework across different AWS accounts and teams — the operating model is a reusable asset, not a one-off
- Contractors from multiple organizations onboard from documentation rather than from tribal knowledge
