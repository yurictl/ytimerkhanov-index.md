# Day-0 Self-Service Platform

- **Company:** Sber (European bank, 109M clients, 300K employees)
- **Year / Duration:** 2018–2021 / 2.5 years
- **Stack:** Ansible, Jenkins, Python, Bitbucket, Linux, Oracle, PostgreSQL
- **Role:** Senior DevOps Engineer

## Problem

App administrators needed database environments (stands) for testing and development but had no self-service option. Every request went through manual processing — the queue was long, the process was error-prone, and deployment took up to two weeks. With over 3,000 databases across Oracle and PostgreSQL, the scale made manual work unsustainable.

## What I Did

Built a self-service portal that let app administrators order environments directly without submitting tickets. Automated the full provisioning lifecycle using Ansible and Jenkins — from environment creation to integration with monitoring and backup systems.

Separately managed and improved automation for over 5,000 Oracle DB environments across the bank's testing landscape, using SQL procedures and Ansible to reduce the volume of manually processed requests by 20%.

## Outcome

- Deployment time for database environments dropped from **two weeks to 2 hours** across 3,000+ databases
- Manual request handling reduced by **20%** for the broader Oracle DB estate
- Eliminated a major bottleneck for development teams bank-wide
