# Candidate Feedback Tool — Post-Interview Automation

- **Company:** Quantori
- **Year / Duration:** 2025
- **Stack:** Claude Code (LLM), internal corporate tooling
- **Role:** Designer and implementer

## Problem

Writing thorough, structured interview feedback took interviewers 60–90 minutes per candidate. This slowed hiring cycles, created a backlog after interview-heavy weeks, and produced variable-quality feedback — making calibration between interviewers difficult and limiting the team's ability to build a consistent hiring bar.

## What I Did

Built a tool that takes raw interviewer notes (bullet points, shorthand, impressions) and 1–2 corporate-style exemplar feedback reports, then feeds them to an LLM with stylistic constraints. The model generates a structured draft covering:

- Candidate strengths with concrete behavioral evidence
- Technical and soft-skill gaps
- Specific examples from the interview
- Recommended next steps in the company's house tone

The interviewer reviews the draft, makes targeted edits, and posts. The format is enforced by the exemplars, so calibration between interviewers becomes easier over time.

## Outcome

- Time per candidate feedback: 60–90 minutes reduced to 5–10 minutes
- Feedback quality became more consistent and actionable across interviewers
- The team built a reusable archive of structured feedback for calibration and future hiring decisions
