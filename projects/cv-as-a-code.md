# CV-as-a-Code — Hiring Pipeline Automation with Claude Code

- **Company:** Quantori
- **Year / Duration:** 2025
- **Stack:** Claude Code, Python, RenderCV (Typst), YAML, Git
- **Role:** Designer and implementer

## Problem

Heads of competence were spending 60–90 minutes per CV manually reformatting, tailoring to specific client roles, and quality-checking resumes. With multiple engineers in the pipeline simultaneously, this was burning senior reviewers and producing inconsistent output — different versions of the same person's CV told different stories depending on who had touched it last.

## What I Did

Shifted the CV workflow from document-centric to data-centric:

- Standardized all CV content into YAML (single source of truth, version-controlled in Git)
- Built Claude Code slash commands for the recurring tasks: "Improve CV," "Tailor to Role," "Extract Skills/Gaps"
- Batches of CVs run through these automated workflows, producing a cleaned document plus a JSON summary with skills inventory, seniority signals, and risk flags
- Reviewers make light edits and approve — they no longer write from scratch
- RenderCV (Typst-based engine) generates multi-format export (PDF, HTML, PNG, Markdown) in a single command

The validation layer catches schema errors, missing fields, and date inconsistencies before rendering — zero invalid CVs reach review.

## Outcome

- Processing time cut 90%: from 60 minutes to 5 minutes per resume
- Quality became consistent across roles and reviewers
- Throughput scaled without adding reviewer workload
- Multiple CV variations per engineer (DevOps-focused, Architecture-focused, FinOps-focused) maintained from one YAML source
