# Group 3 — When It Went Wrong

Questions: Project that didn't go as planned / Greatest weakness / Handling criticism or feedback

> One core story. The lesson from it becomes the weakness answer — specific and real, not generic.

---

## Core Story

**Project**: Price Elasticity Dashboard — EPAM, 2023

**Situation**: EPAM had an internal ML product that was sold as a pilot to a client. My job was to adapt the infrastructure to the client's tech stack and get it ready for a demo. The team was small: one PM, one analyst, one fullstack developer, two data scientists, and me as the only DevOps engineer. There was no Solution Architect.

**What happened**: The PM needed a working demo within two months. But since there was no Solution Architect, I felt responsible for getting the architecture right. I got absorbed in doing things properly — proper environment separation, clean Terraform code, no shortcuts. I kept pushing back when the team wanted to move faster.

The PM gave me direct feedback: the pace was too slow. My first reaction was to explain why the architecture mattered. But then I stepped back and looked at the bigger picture.

**What I realized**: At this stage, the project's survival depended on the demo. If the demo didn't land, there would be no project — and no infrastructure to improve later. I was solving the wrong problem. I was optimizing for a future that might never happen.

**What I changed**: I shifted my focus to what the demo actually needed. We delivered it on time. The client approved the project for further development.

**The lesson**: In early-stage projects, I now explicitly ask: "What does success look like for this phase?" before diving into the implementation. That question stops me from confusing technical correctness with business value.

---

## Weakness Version

> "What is your greatest weakness?"

My weakness is that I sometimes get too invested in the technical solution before checking if it's actually the right priority.

I learned this on a client project where I was building infrastructure for a demo. I kept focusing on doing it cleanly instead of quickly — because I didn't want technical debt. But the PM's priority was the demo, not the architecture. The project's future depended on that demo.

Once I got that feedback, I changed my approach. Now I start every project phase by asking: "What does success look like right now?" That question keeps me focused on what actually matters — not what's technically ideal.

It's still something I have to watch myself on. But being aware of it makes a real difference.

---

## Handling Criticism Version

> "How do you handle feedback and criticism?"

My honest answer: I don't always enjoy hearing it in the moment. But I've learned to pause before reacting.

The clearest example is from a dashboard project. My PM told me the pace was too slow. My first instinct was to defend my work — I had real reasons for the decisions I made. But I gave it a day and asked myself: is he right?

And he was — just not about the code quality. He was right that the demo was the priority, and I was treating it as secondary.

That feedback changed how I approach new projects. Now when I get pushback, I try to ask: what's the business reason behind this? Usually there's something real there, even if the delivery isn't perfect.
