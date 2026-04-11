# Yuri Timerkhanov — Professional Index

> **Senior DevOps & Cloud Platform Engineer | AI-Driven Automation on AWS, K8s, Terraform**
> Malaysia · yutimer@gmail.com · [linkedin.com/in/ytimerkhanov](https://linkedin.com/in/ytimerkhanov) · [github.com/yurictl](https://github.com/yurictl)
>
> This file is the single navigable entry point to the portfolio. Everything links to a source file.

---

## Who I Am

Senior System Engineer specializing in **R&D and Advanced Automation**. I bridge complex infrastructure and developer productivity by building self-service tools and AI-driven workflows — replacing routine maintenance with autonomous systems.

What drives me is not the technology itself. What I care about is the problem behind it: can this tool actually help the team, and how much time does it save?

**Experience:** 15 yrs in tech · 8 yrs DevOps · 7 yrs AWS · Former Oracle DBA (deep SQL tuning background)
**Certifications (active):** CKA (until Mar 2027) · AWS SysOps Administrator Associate (until Dec 2025) · AWS AI Practitioner (until Oct 2027)
**Education:** Master's in Mathematics, Ural State University (2000–2006)

---

## Skills Snapshot

| Domain | Tools & Technologies |
|--------|----------------------|
| AI & Automation | OpenAI API, Claude Code, RAG, Prompt Engineering, AI Agents |
| Cloud | AWS (expert), Azure (novice) |
| Containers | Docker, Kubernetes, Helm, Kustomize, ArgoCD, EKS, AKS |
| CI/CD | GitHub Actions, GitLab CI/CD, Jenkins, Bitbucket, Roadie (Backstage) |
| IaC & Scripting | Terraform, CloudFormation, Ansible, Python, Bash |
| IaC Quality | Terratest, Checkov, CIS Benchmarks, HashiCorp Vault |
| Observability | Prometheus, Grafana, OpenTelemetry, CloudWatch, AppDynamics |
| SRE | SLIs/SLOs, incident response, zero-downtime releases, FinOps |
| MLOps | Kubeflow, MLflow, SageMaker |
| Databases | Oracle (OCP certified), Postgres, AuroraDB, DynamoDB, MongoDB, Snowflake |

---

## Projects

Projects are ordered by strategic impact. AI-in-DevOps projects come first — they represent Yuri's clearest differentiator.

---

### AI & Automation Projects

---

#### TerraGuide AI — Terraform Plan Risk Analysis

- **Company:** EPAM
- **Year / Duration:** 2024
- **Stack:** Python, OpenAI GPT-4o / GPT-4o-mini, Docker, Terraform
- **Role:** Solo builder — designed, implemented, and shipped
- **Problem:** Terraform plan outputs can be 50KB+ of dense HCL. Reviewers would skim or miss destructive changes. Risk assessment was gated on senior engineers, creating a bottleneck — junior engineers couldn't safely approve production changes.
- **What Yuri did:** Built a CLI tool that ingests a Terraform plan, summarizes it by resource type and change category (Add / Modify in-place / Replace / Destroy), assigns a risk level (LOW / MEDIUM / HIGH / CRITICAL), and writes the output as a PR comment and into ChatOps. Used GPT-4o-mini as the default (128k context, 15x cheaper than GPT-4) with temperature 0.2 for deterministic, safe output. ~240 lines of Python, containerized, non-root Docker execution.
- **Outcome:** Plan review time down 87% (15 min → 2 min). Junior engineers could conduct reviews independently. 40% fewer senior escalations. Error diagnosis time cut by 60%.
- **Source:** [`projects/terraGuide-ai.md`](projects/terraGuide-ai.md)

---

#### AI Release Notes Generator — Terraform Module Deployment Guides

- **Company:** EPAM
- **Year / Duration:** 2024
- **Stack:** Python, Azure OpenAI GPT-4o, Docker, BitBucket, Confluence API, HashiCorp Vault
- **Role:** Solo builder — designed, implemented, and shipped
- **Problem:** Operations teams needed a deployment guide for every Terraform module release — comparing the previous and current version, documenting variable changes, breaking changes, and step-by-step upgrade instructions. Writing one guide manually took 2–4 hours. With 20–40 releases per month, this was a constant ops bottleneck, and guides were inconsistent.
- **What Yuri did:** Built a Dockerized tool that clones two repo versions (current and previous tags), computes diffs of README.md and CHANGELOG.md, constructs a domain-specific few-shot prompt, sends it to GPT-4o (temperature 0.2, 128k context), and publishes the result directly to Confluence. Authors review instead of writing from scratch. Secrets managed via Vault with temporary SSH key rotation.
- **Outcome:** Documentation time reduced 95% (2–4 hours → 5–10 minutes). Consistency reached 100% (template-enforced). Error rate fell from ~10–15% to <2%. Cost per guide: $0.50–2 vs. $80–160 of manual labor. Break-even: under 1 month.
- **Source:** [`projects/ai-release-notes.md`](projects/ai-release-notes.md)

---

#### CV-as-a-Code with Claude Code — Hiring Pipeline Automation

- **Company:** Quantori
- **Year / Duration:** 2025
- **Stack:** Claude Code, Python, RenderCV (Typst), YAML, Git
- **Role:** Designer and implementer
- **Problem:** Heads of competence were spending 60–90 minutes per CV manually reformatting, tailoring, and quality-checking resumes for specific client roles. With multiple engineers in the pipeline, this was burning reviewers and producing inconsistent output.
- **What Yuri did:** Standardized CV data into YAML (single source of truth) and built Claude Code slash commands ("Improve CV," "Tailor to Role," "Extract Skills/Gaps"). Batches of CVs run through automated workflows, producing a cleaned document plus a JSON summary (skills, seniority signals, risk flags). Reviewers make light edits and approve. Multi-format export (PDF, HTML, PNG, Markdown) in one command.
- **Outcome:** Processing time cut 90% (60 min → 5 min per resume). Quality became consistent across roles. Throughput scaled without burning reviewers.
- **Source:** [`projects/cv-as-a-code.md`](projects/cv-as-a-code.md)

---

#### Candidate Feedback Tool — Post-Interview Automation

- **Company:** Quantori
- **Year / Duration:** 2025
- **Stack:** Claude Code (LLM), internal corporate tooling
- **Role:** Designer and implementer
- **Problem:** Writing thorough, structured interview feedback took interviewers 60–90 minutes per candidate. This slowed hiring cycles and produced variable-quality feedback, making calibration between interviewers difficult.
- **What Yuri did:** Built a tool that takes raw interviewer notes and 1–2 corporate-style exemplar feedback reports, feeds them to an LLM with stylistic constraints, and generates a structured draft — covering strengths, gaps, concrete behavioral examples, and next steps in the company's house tone. Interviewer reviews, tweaks, and posts.
- **Outcome:** Time per candidate down from 60–90 min to 5–10 min. Feedback quality became more consistent and actionable. Team built a reusable archive for calibration and future hiring.
- **Source:** [`projects/candidate-feedback-tool.md`](projects/candidate-feedback-tool.md)

---

### Infrastructure & Platform Projects

---

#### Quantori IaC Platform — Multi-Database Provisioning & CI/CD Standardization

- **Company:** Quantori
- **Year / Duration:** 2024–2025 (ongoing)
- **Stack:** Terraform, Terratest, GitHub Actions, Roadie (Backstage), Aurora, PostgreSQL, Oracle
- **Role:** Senior System Engineer; owned IaC quality and database provisioning automation
- **Problem:** 30+ Terraform modules had no unified testing framework — each team applied different patterns, making cross-team reuse brittle and review slow. Database provisioning (Aurora, PostgreSQL, Oracle) was manual across environments, generating operational overhead and human error. Junior DevOps hiring was ad hoc, with no structured onboarding pipeline.
- **What Yuri did:** Built a unified CI/CD and end-to-end testing framework for all 30+ Terraform modules using standardized Terratest patterns. Standardized multi-database provisioning and configuration across environments. Automated Day-0 database setup via GitHub Actions and Roadie templates — developers get ready-to-use databases instantly without manual steps. Streamlined the technical interview process (unified questions, evaluation forms, feedback templates). Co-developed Cloud/DevOps School materials and practical labs to create a repeatable source of junior DevOps talent.
- **Outcome:** Development time reduced 2–3×. Operational overhead for database provisioning cut ~40%. Interview throughput and TA pipeline efficiency improved ~30%.
- **Source:** [`projects/quantori-iac-platform.md`](projects/quantori-iac-platform.md)

---

#### IAD Framework / IDP Platform — FinOps & Monitoring Migration

- **Company:** EPAM
- **Year / Duration:** 2023–2024, ~1 year
- **Stack:** Terraform, Terragrunt, EKS, AKS, Vault, Consul, Jenkins, Prometheus, Grafana, AppDynamics, Azure OpenAI
- **Role:** Senior System Engineer; led multiple workstreams on a large internal developer platform (57 base modules, 293 component modules, 51 AWS accounts, 194 environments)
- **Problem:** Three monitoring subscriptions (AppDynamics, Splunk) were costing $150,000/month and the company had set a hard end-of-year deadline to exit them. No migration plan existed, no one on the team had done this transition, and the architecture was undefined at the start.
- **What Yuri did:** Led the POC for transitioning from AppDynamics to Prometheus + Grafana. Started by mapping actual requirements, then reached out to a neighboring team who had a relevant setup and adapted their approach rather than starting from scratch. While running the cost analysis for monitoring, noticed broader cloud spend anomalies — ran a full audit of backup policies, idle resources, and usage patterns (outside of original task scope).
- **Outcome:** POC completed and became the migration plan's foundation. Annual cloud costs reduced by $100,000+, reversing a growing cost trend. Contributed to 25+ major Terraform module releases. Conducted 15+ technical interviews in 2024.
- **Source:** [`projects/iad-framework.md`](projects/iad-framework.md)

---

#### SAP HANA → AWS / Snowflake Migration

- **Company:** EPAM
- **Year / Duration:** 2023, 8 months
- **Stack:** Terraform, CloudFormation, GitHub Actions, GitLab CI/CD, ECS, Aurora DB, DynamoDB, VPC, IAM, Snowflake
- **Role:** DevOps lead for a team of 10; owned all AWS infrastructure work
- **Problem:** A large pharmaceutical company needed to migrate its Marketing Analytics Reporting System from SAP HANA to a cloud-native AWS + Snowflake stack. Simultaneously, GitLab support was ending — forcing a pipeline migration to GitHub. Infrastructure code coverage was at 70%, with 200+ AWS resources partly described in nested CloudFormation stacks and partly managed manually.
- **What Yuri did:** Rewrote 3,500 lines of CloudFormation into reusable Terraform modules, importing all 200+ AWS resources without drift and without disrupting the team's ongoing work. Migrated CI/CD pipelines from GitLab to GitHub. Centralized all environment-specific configuration into GitHub configs and secrets (previously scattered in application code).
- **Outcome:** Project delivered on schedule. Infrastructure code coverage: 70% → 95%. Infrastructure costs reduced by 3x+. Deployments 4x faster. Knowledge transfer completed for the operations team.
- **Source:** [`projects/sap-hana-snowflake-migration.md`](projects/sap-hana-snowflake-migration.md)

---

#### Booking System for Demo Environments

- **Company:** EPAM (internal product)
- **Year / Duration:** 2021, 6 months
- **Stack:** GitLab CI/CD, AWS SDK, API Gateway, CloudFront, Lambda, ECS (Fargate), SQS, DynamoDB, EC2, S3, IAM, Prometheus, Grafana
- **Role:** Solo DevOps engineer — built everything from scratch
- **Problem:** Business Analysts, Presales, and Architects had to request demo environments through the DevOps team — a slow, manual, blocking process. The goal: self-service provisioning in under 15 minutes, available company-wide.
- **What Yuri did:** Engineered the full serverless architecture using AWS and GitLab CI/CD. Built CI/CD pipelines and AWS infrastructure from scratch. Designed and automated the provisioning process for two demo environment types: WordPress (3–5 min deploy via Fargate from custom image) and SAP Commerce 2105 / Hybris with Spartacus (<15 min deploy from pre-built AMI). Set up CloudWatch dashboards and a dedicated Grafana service with Prometheus for monitoring; integrated GitLab pipeline metrics with Teams alerts.
- **Outcome:** Active development phase completed in 6 months. Tool shipped company-wide. Employees independently deploy temporary stands for presentations, theory checks, and functionality tests — no DevOps involvement required.
- **Source:** [`projects/demo-booking-system.md`](projects/demo-booking-system.md)

---

#### Chatbot Systems — Internal Employee Chatbot

- **Company:** EPAM
- **Year / Duration:** 2022, 6 months
- **Stack:** Jenkins, Terraform, AWS (SageMaker, Cognito, ECS, ELB, EBS, Route53, Aurora DB), Python
- **Role:** DevOps lead; joined an in-flight project 4 months in
- **Problem:** A large pharmaceutical company was building an internal chatbot backed by an ML model (SageMaker) and a search engine (Coveo). When Yuri joined, the last release had taken a full month to prepare. Three environments (dev, staging, prod) had been set up manually by different people — configurations were inconsistent, and there was no automated deployment.
- **What Yuri did:** Standardized IAM roles across all environments. Rewrote Terraform code from scratch, recreating some resources and importing others. Resolved the hardest blocker — Cognito configuration that required cross-team manual coordination — by systematically working through request processes. Built Jenkins CI/CD pipelines from scratch for all environments, including automated tests and static code analysis.
- **Outcome:** Release frequency: monthly → weekly. Releases became stable and predictable. The team could ship new features without DevOps becoming a bottleneck.
- **Source:** [`projects/chatbot-systems.md`](projects/chatbot-systems.md)

---

#### ETL & Report Generator — Clinical Data Tooling

- **Company:** EPAM
- **Year / Duration:** 2022, 9 months
- **Stack:** Jenkins, Terraform, AWS (ECS, ELB, Route53, Glue, Lambda, DynamoDB), Python, Node.js
- **Role:** DevOps lead from project inception; also mentored a junior DevOps engineer (client-side)
- **Problem:** A tool to accelerate updates to CDISC (Clinical Data Interchange Standards Consortium) controlled terminologies — a process that previously took over a year to implement per cycle. The application was built from scratch; Yuri joined at the start.
- **What Yuri did:** Established AWS infrastructure using Terraform from day zero, enabling the development team to work in parallel from the beginning. Built and fully automated CI/CD pipelines with Jenkins, replacing manual deployment. Mentored a junior DevOps engineer on the client side — setting tasks, reviewing work, and ensuring a clean project handover.
- **Outcome:** Deployment time cut by 4x. Project handed over successfully with the junior engineer able to continue independently. Infrastructure remained stable after handover.
- **Source:** [`projects/etl-report-generator.md`](projects/etl-report-generator.md)

---

#### Price Elasticity Dashboard — MLOps for Pricing Analytics

- **Company:** EPAM
- **Year / Duration:** 2023, 3 months
- **Stack:** Terraform, EKS, GitHub Actions, GitLab CI/CD, ECS, ECR, Kubeflow, Aurora DB, MongoDB, Glue, IAM
- **Role:** Solo DevOps engineer; de facto Solution Architect (no architect on the team)
- **Problem:** EPAM had an internal ML product sold as a client pilot. The client's tech stack was significantly different from the internal demo. No Solution Architect. Small team: 1 PM, 1 analyst, 1 full-stack developer, 2 data scientists. Hard demo deadline in two months.
- **What Yuri did:** Took ownership of the target architecture from scratch — wrote all Terraform code for AWS resources including an EKS cluster. Migrated CI/CD pipelines from GitLab to GitHub. Created separate environments for development, testing, and client presentation. Shifted approach mid-project after PM feedback: stopped optimizing for "correct" architecture and prioritized demo readiness. Conducted knowledge transfer to a successor in one week.
- **Outcome:** Demo delivered on time. Client approved the project for further development. Lesson internalized: always anchor implementation to the current phase's definition of success.
- **Source:** [`projects/price-elasticity-dashboard.md`](projects/price-elasticity-dashboard.md)

---

#### Day-0 Self-Service Platform — Database Automation at Scale

- **Company:** Sber (European bank, 109M clients, 300K employees)
- **Year / Duration:** 2015–2021, 2.5 years core project
- **Stack:** Ansible, Jenkins, Python, Bitbucket, Linux, Oracle, Postgres
- **Role:** Infrastructure automation engineer
- **Problem:** Database administrators had to request new Oracle or Postgres environments through a manual process that took two weeks end-to-end — across more than 3,000 databases in the bank's landscape.
- **What Yuri did:** Built full automation for the bank's database provisioning pipeline using Ansible and Jenkins, integrating with monitoring and backup systems. Separately managed 5,000+ Oracle DB environments, improving automation via SQL procedures and reducing manual request volume by 20%.
- **Outcome:** Deployment time per database: 2 weeks → 2 hours. Scale: 3,000+ databases. Manual ticket volume down 20%.

---

## Career Timeline

| Period | Role | Company |
|--------|------|---------|
| 11/2024 – present | Senior System Engineer | Quantori |
| 06/2021 – 11/2024 | Senior System Engineer | EPAM |
| 01/2015 – 06/2021 | Senior DevOps / Automation Engineer | Sber |
| 02/2009 – 01/2015 | System Engineer | MegaFon |
| 01/2005 – 12/2008 | System Administrator | Rostelecom |

---

## Recommendations

Three LinkedIn recommendations from direct collaborators.

**Pavel Konan — CTO, Enginerasoft**
> "I've had the pleasure of working with Yura Timerkhanov, and I can confidently say he's one of the most talented and dedicated engineers I've come across. With over 15 years of experience, Yura has a unique ability to tackle complex challenges, especially in cloud infrastructure and automation. His work on AWS migrations and DevOps pipelines consistently resulted in cost savings and improved efficiency. Beyond his technical expertise, Yura is a natural leader, always willing to mentor others and share his knowledge."

**Dana Forberger MBA — Associate Director, Global Clinical Data Integration Operations, Merck**
> "I worked with Yurii on developing a tool to help my users automate a major manual task. The tool developed reduces work time from approximately six months to about one week. Yurii was instrumental in developing the tool and understanding what my users wanted... Yurii was always on top of finding and resolving any challenges that developed and was proactive, honest, and vocal when communicating with me and the end users."

**Sergey Samoylov — DevOps Engineer, former Sberbank-Technology**
> "The main area of his tasks were resolving critical problems with over 2000 databases supported by our team. Especially great skills he showed during support of Oracle Databases Clusters and support of Machine Learning environment. Automation was another area where he demonstrated his high expert level. Yuriy always supported state of the art knowledge and shared it along colleagues helping them to achieve higher qualification level."
