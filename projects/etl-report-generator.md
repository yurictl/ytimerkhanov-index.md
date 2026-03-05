# ETL & Report Generator — Clinical Data Tooling

- **Company:** EPAM
- **Year / Duration:** 2022, 9 months
- **Stack:** Jenkins, Terraform, AWS (ECS, ELB, Route53, Glue, Lambda, DynamoDB), Python, Node.js
- **Role:** DevOps lead from project inception; mentored a junior DevOps engineer on the client side

## Problem

A pharmaceutical company needed to accelerate the adoption of updates to CDISC (Clinical Data Interchange Standards Consortium) controlled terminologies — a process that previously took over a year to implement per cycle. The ETL and reporting tool was being built from scratch. At the start: no infrastructure, no pipelines, all deployments were manual.

## What I Did

Joined at project inception alongside the development team, which meant I could establish good practices from day one rather than retrofitting them:

- Built AWS infrastructure from scratch using Terraform, establishing environments for all stages (dev, staging, prod) in parallel with active development
- Built and fully automated CI/CD pipelines with Jenkins, replacing manual deployment entirely
- Mentored a junior DevOps engineer on the client side — set tasks, reviewed work, explained decisions, and ensured a clean handover. At the start she struggled with basic git workflows; by handover she was independently managing daily tasks and contributing to the project

## Outcome

- Deployment time cut by 4x (manual → fully automated CI/CD)
- Clean project handover: the junior engineer was able to continue independently after the EPAM team's participation ended
- Infrastructure remained stable after handover
