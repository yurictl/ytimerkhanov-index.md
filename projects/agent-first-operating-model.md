# Agent-First Operating Model — Restructuring Platform Work Around AI Collaborators

- **Company:** Quantori (enterprise client under NDA)
- **Year / Duration:** 2025–2026 (ongoing)
- **Stack:** Claude Code, Markdown + YAML frontmatter, Python, Make, Git; CLIs wired as skills: Confluence CLI, glab, jira-cli, AWS CLI
- **Role:** Designed and rolled out the agent-centric operating model across two greenfield project workspaces (primary platform + sister project) and the shared infra workspace

## Problem

AI coding assistants moved from autocomplete to something that reads the repository, plans the change, and ships it. On greenfield projects that shift surfaced a concrete problem: existing DevOps knowledge is optimized for *human* onboarding — long Confluence tutorials, screenshots, tribal Slack context, stale pages nobody deletes. When an agent is dropped into that environment:

- It reinvents conventions because nothing tells it which standards this project uses
- It proposes decisions that were already made and rejected — ADRs live in someone's head, not in the repo
- It hits permission prompts and config gaps because tooling isn't described in a place it can read
- It produces plausible-but-wrong output because documentation is narrative, not structured

The question stopped being "do we use AI tools" and became "what does our knowledge and tooling have to look like for an agent to be a productive contributor — not just an autocomplete engine."

## What I Did

**Agent-first entry points at every level**

- One `CLAUDE.md` at the workspace root plus one per project (primary app, infra, sister project) — every path an agent can be spawned from has an entry-point brief: role, constraints, doc framework, tool registry, git conventions
- Each repository inside a workspace keeps its own `CLAUDE.md` with repo-local context (project IDs, branch conventions, CI quirks) — agents pick up repo-specific rules without reloading the whole workspace

**Structured, machine-readable documentation**

- Mandatory YAML frontmatter on every doc: `title`, `summary`, `status`, `updated`. The `summary` field is specifically written as a one-line hook so an agent can skim an index and load only the relevant document instead of burning context on unrelated pages
- Status vocabulary fixed per category: `active` for operations, `accepted` / `superseded` / `draft` for ADRs, `open` / `in-progress` for WIP. Agents filter on status rather than re-reading content to find what's current
- 3+1 framework (Orientation / Operations / Decisions / WIP): three persistent categories for long-lived knowledge, one transient category for in-flight investigations. Clear retrieval paths for "what is this project," "how do I do X," "why was this decided," "what are we still figuring out"

**Knowledge lifecycle that prevents agent drift**

- WIP entries have a hard rule: graduate on close into Operations or Decisions, or be deleted. No half-finished files sitting around with stale hypotheses that an agent might treat as ground truth
- ADRs chain via `supersedes` — when a decision changes, the new ADR explicitly points at the old one and marks it `superseded`. Agents can trace the reasoning without being misled by outdated docs

**Mechanical validation loop**

- Python CLI (`<project>_docs.py`) scaffolds new WIP / ADR / Operations docs with correct frontmatter — no copy-paste errors
- `make docs-check` validates frontmatter, link integrity, and stale-doc freshness — the loop the agent runs before committing doc changes
- `make docs-index` rebuilds the document index inside `PROJECT_CARD.md` — the index stays in sync with the filesystem, so an agent's retrieval is never based on a dangling reference

**Tool registry as a skill catalogue**

- Each external tool (Confluence, GitLab, Jira, AWS CLI) is documented with: CLI version, auth config path, a verify command, and the matching Claude Code skill name. Agents self-check tool availability and know which skill to invoke, instead of me pasting the same usage block into every prompt
- Custom skills for recurring workflows (`/graduate`, `/start-wip`, `/audit-docs`, `/review`, `/security-review`, `/md-to-confluence`) — shared vocabulary so any session in any workspace triggers the same workflow instead of reconstructing it from prose

**Governance for AI use**

- Wrote an approved-AI-tools reference document that maps the client's corporate policy hierarchy onto a concrete list of permitted tools for contractors, with a governance framework and explicit constraints. Turned "should we use this" ambiguity into a repo-readable policy

**Persistent memory across sessions**

- Structured memory file (`MEMORY.md` + typed memory entries: user, feedback, project, reference) at the workspace level. Cross-session context — user profile, workflow preferences, project state — survives conversations instead of being re-explained every morning

## Outcome

- Three workspaces (primary platform, infra, sister project) run on the same agent-first operating model. Dropping an agent into any one of them produces consistent behaviour on conventions, tool use, and git hygiene
- 28 structured documents across the primary platform alone (9 ADRs + 19 operations runbooks), all machine-readable, indexed, and validated by a mechanical check — the kind of substrate that makes agents useful instead of risky
- Recurring chores (docs scaffolding, validation, index rebuild, WIP graduation, doc audits) moved from "human remembers" to "agent runs the command" — knowledge hygiene became a pipeline job, not a discipline problem
- The same pattern — CLAUDE.md entry points, frontmatter + 3+1, docs CLI, tool registry, custom skills, memory — carried over to personal work (career portfolio, drafts, posts), so what I learned on the enterprise platform compounds instead of being project-local
- Shift in how I price my contribution: I'm no longer the person who writes Terraform faster with AI; I'm the person who sets up the operating model so other contributors (human and AI) can work without me being the bottleneck
