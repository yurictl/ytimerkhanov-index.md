# Group 4 — Working With People

Questions: Teamwork / Conflicts / Explaining technical concepts to a non-technical audience

---

## Teamwork Story

> "Describe a time when you had to work as part of a team to achieve a goal."

**Project**: Booking System for Demo Environments — EPAM internal project, 6 months

**Situation**: EPAM needed a self-service tool that would let employees deploy temporary demo environments on their own — in under 15 minutes. The team was small, and what made it unusual: everyone was working in a role that was new to them. The PM was managing a technical project for the first time. I was working with a serverless AWS architecture — Lambda, API Gateway, SQS — in a way I hadn't before. The developer was learning new patterns too.

**What made it work**: We had to trust each other. Nobody was the expert who had all the answers. So we communicated constantly — short syncs, honest updates when something wasn't working, early escalation when we got blocked.

My job was to build the AWS infrastructure and CI/CD pipelines from scratch. But I also had to explain to the rest of the team how things connected — why a deployment sequence mattered, what would break if we changed the environment setup. I made it a habit to over-communicate: write things down, share diagrams, make sure people understood what was happening in the infrastructure.

**Result**: The project finished in six months. The tool went into company-wide use. Employees now use it to deploy demo environments for client presentations, theory checks, and functionality tests — without touching the DevOps team at all.

---

## Explaining Technical Concepts

> "Describe a time when you had to explain a complex technical concept to a non-technical audience."

One ongoing example from my current project.

Terraform plan reviews are a real problem. When engineers run `terraform plan`, they get hundreds or thousands of lines of technical output. It's hard to read even for experienced engineers — and for a PM or a client, it's completely opaque. But they still need to approve deployments.

I built a tool that takes that output and uses an LLM to translate it: what's being added, what's being replaced, what could cause downtime, and what the overall risk level is — LOW, MEDIUM, HIGH, or CRITICAL.

Now, instead of showing someone a wall of Terraform code before a deployment, I can send them a two-paragraph summary. They can ask informed questions. They can say "wait, why is this HIGH risk?" — and that's a much better conversation than "just trust us, it'll be fine."

The principle I use: don't simplify the topic — translate it. Find what the other person already cares about — uptime, cost, timeline — and connect the technical concept to that.

---

## Handling Conflicts

> "How do you handle conflicts with colleagues or clients?"

My approach is to separate the technical disagreement from the personal dynamic.

Most conflicts I've had at work were actually alignment issues — two people optimizing for different things without realizing it.

On the Price Elasticity project, there was real tension between me and the PM. I wanted clean architecture. He wanted a fast demo. We were both right for our own reasons.

What resolved it was getting explicit: what are we actually optimizing for right now? When we agreed that the demo was the immediate priority, the conflict disappeared. We weren't arguing about the code anymore — we were aligned on the goal.

I've found that most conflicts dissolve when you move from "you're wrong" to "let's agree on what success looks like here."
