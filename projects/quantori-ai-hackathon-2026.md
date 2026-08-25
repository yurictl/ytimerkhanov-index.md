# AI Hackathon Governance — Task Design & Agent-Assisted Judging

- **Company:** Quantori
- **Year / Duration:** June–July 2026 (~7 weeks of preparation and judging; 48-hour remote build window)
- **Stack:** LiteLLM, Claude and Gemini models, open-weight models via Ollama, LLM coding agents, Python, git, GitHub / GitLab, Teams
- **Role:** Organizing committee member — challenge design, evaluation rubric, participant policy, repository-level judging, live-final judging, and retrospective

## Problem

Quantori wanted an internal AI hackathon that produced useful agent applications, not polished wrappers. Three constraints shaped the event:

- Tasks could not depend on client or internal data. Data approval would have blocked the schedule.
- “Multi-agent” was easy to claim and hard to compare. A fixed A→B→C pipeline can look agentic in a short demo.
- Demo-only judging could not verify when code was built, which models actually ran, or whether an evaluation claim had a real harness behind it.

The event needed task design, scoring, and technical verification that worked together.

## What I Did

**Removed the data dependency from task design**

- Designed six challenge cards across single-agent and multi-agent tracks
- Used public or committee-fabricated substrates: OSS contributor data, EU AI Act and NIST AI RMF texts, LKML streams, public documentation drift, and simulated grant-review and scheduling scenarios
- Added one local-model constraint with `gpt-oss-20b` to force architecture work around a smaller model rather than prompt-tuning a frontier model

**Made agent sophistication testable**

- Split practical Impact from Innovation in the scoring rubric
- Defined a 0–5 anchored scale and final weights: Functionality 35%, Innovation 10%, Impact 15%, Agent Sophistication 20%, Presentation & Docs 20%
- Wrote the Track B anti-pattern into participant guidance: a fixed orchestration sequence is not a multi-agent system; the design must show dynamic routing, negotiation, or disagreement resolution
- Replaced a proposed one-hour pre-approval step for custom ideas with a light Open Proposal Lane and one shared rubric for every submission

**Built repository-level judging support**

- Reviewed all seven submitted repositories against the rubric before the live final
- Ran an independent second-model verification pass across all seven projects
- Checked git history, delivery-window compliance, actual model use, declared track versus implemented architecture, eval substance, and application-security gaps
- Kept repository evidence separate from demo evidence and wrote a scorecard rationale for every project

**Converted the event into reusable controls**

- Wrote the retrospective across fair play, tracks, bonuses, infrastructure, judging, demo reliability, and code-release policy
- Proposed a managed repository hub with an infrastructural code freeze, bonuses based on demonstrated rather than declared model use, and a hosted open-weight endpoint for reliable demos
- Recommended repository-level agent-assisted review as standard judging support for the next edition

## Outcome

- 7 submitted projects progressed to 4 live finalists
- Repository review surfaced delivery-window, model-claim, track-fit, and evaluation discrepancies that recorded demos did not expose
- Two of four finalists were solo engineers, showing that one engineer working with agents could reach the final alongside multi-person teams
- Public-data task design removed the internal-data approval dependency and preserved a path to later open-sourcing, subject to IP, licensing, data, and secret review
- The judging workflow produced written, comparable evidence for every submission instead of relying on presentation alone

This project is the governance side of AI engineering: define the constraints, make claims testable, and build verification into the workflow.
