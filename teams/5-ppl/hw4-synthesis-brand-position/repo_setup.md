# UnlockDrill repo setup

**Team:** 5 PPL

**Framework selected for the proposed setup:** [OpenSpec](https://github.com/Fission-AI/OpenSpec), because explicit behavior scenarios help resolve prompt timing, skip, pause, and repeat-trigger behavior before implementation.

## Status

This homework includes the proposed framework and a copy of the product AGENTS.md below. No product repository, framework installation, or runnable application is claimed. The [draft product documents](product-docs/) are ready to copy into the future product repo's `docs/` folder. This class-submission folder is not that product repository.

## Proposed layout

```text
AGENTS.md
docs/brand_position.md
docs/style_guide.md
.claude/agents/persona-maya.md
.claude/agents/persona-jordan.md
.claude/agents/persona-casey.md
assets/logo/
openspec/
src/
tests/
```

## Feature acceptance scenarios

- An eligible app opening offers one reviewed question for a selected topic.
- Skip and pause remain visible; returning to the chosen app does not trigger a loop.
- A wrong answer receives a brief explanation without requiring correctness to exit.
- Frequency settings and offline/error exits behave consistently.
- Platform integration is verified on the actual target device before compatibility is advertised.

## Copy of AGENTS.md

````markdown
# UnlockDrill

## Product
UnlockDrill is an opt-in SAT practice shortcut. Offer one reviewed question at a student-selected app-opening moment. Prioritize a small start, useful feedback, and user control.

## Read first
Read docs/brand_position.md, docs/style_guide.md, relevant research, and the current feature specification. These describe proposed behavior; distinguish implemented features from plans.

## Evidence
Preserve interview IDs and exact quotations. Do not invent testimonials, score gains, persona facts, supported devices, or customer validation. Keep ErrorJournal and tutoring evidence separate from evidence for app-triggered practice.

## Feature workflow
Use OpenSpec after installation. Write the proposal, behavior scenarios, design, and task list; resolve platform uncertainty; implement a small change; verify the scenarios; document what changed and what remains uncertain.

## Product rules
Users choose the apps and timing. Keep skip and pause visible. Respect frequency limits. Avoid repeated-trigger loops. Never require a correct answer in the proposed default flow. Provide a safe exit on errors.

## Learning content
Use original or appropriately licensed questions. Check each answer and explanation. Do not imply official SAT endorsement. Do not equate attempts or streaks with score improvement.

## Design
Use the agreed tokens and logo assets. Maintain readable text, keyboard access, visible focus, labeled controls, and reduced-motion support. Do not add guilt-based copy or compulsory celebration.

## Data
Collect only data needed for the agreed feature and explain collection. Keep raw interview notes and participant identities out of public builds. Do not commit secrets.

## Run and verify
No application stack or run commands are configured yet. After setup, document exact install, development, build, and test commands here. Do not invent commands or report unrun checks as passing.

## Review and handoff
Test prompt eligibility, skip, pause, repeated opening, answer feedback, and error exit. Summarize behavior changes, checks actually run, and remaining limits in the pull request. Team members own final product and release decisions.
````

## Remaining setup

Create the product repository, install the selected workflow, copy the documents and persona files, and document the actual install/run/test commands after the platform is selected. No commands have been invented to suggest that a scaffold already runs.
