# Booking System for Demo Environments

- **Company:** EPAM (internal product)
- **Year / Duration:** 2021, 6 months
- **Stack:** GitLab CI/CD, AWS SDK, API Gateway, CloudFront, Lambda, ECS (Fargate), SQS, DynamoDB, EC2, S3, IAM, Prometheus, Grafana
- **Role:** Solo DevOps engineer — built everything from scratch

## Problem

Business Analysts, Presales, and Architects had to request demo environments through the DevOps team — a slow, manual, blocking process. The business goal was to give employees self-service access to fully deployed demo environments within 15 minutes, available company-wide without DevOps involvement.

## What I Did

Engineered the full serverless architecture and built the platform from scratch over 6 months:

- Designed and built CI/CD pipelines for the full-stack serverless application (frontend on S3 + CloudFront, backend on API Gateway + Lambda)
- Automated provisioning for two demo environment types:
  - **WordPress (POC):** 3–5 minute deploy as a Fargate node from a custom Docker image
  - **SAP Commerce 2105 (Hybris) with Spartacus:** under 15 minutes deploy from a pre-built AMI — required a different provisioning approach since Hybris cannot be containerized the same way as a standard web app
- Set up CloudWatch dashboards and a dedicated Grafana + Prometheus service for monitoring
- Integrated GitLab pipeline metrics (via an open-source OpenMetrics extractor) with Microsoft Teams alerts — failed pipeline deployments trigger an automatic notification to the project channel

Each demo environment type required a different infrastructure approach, which made the provisioning design non-trivial despite the self-service surface being simple.

## Outcome

- Active development phase completed in 6 months
- Tool shipped company-wide
- Business Analysts, Presales, and Architects independently deploy temporary environments for presentations, feasibility checks, and demos — no DevOps team involvement required
