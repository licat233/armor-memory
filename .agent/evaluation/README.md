# Evaluation

This directory supports manual cross-Agent evaluation for Hermes Agent, Claude Code, and Codex.

Files:

- `classification-cases.yaml`: natural-language cases and expected structured classifications
- `expected-results.yaml`: normalized expected outputs for comparison

## Manual Evaluation Workflow

1. Give the same case to Hermes, Claude Code, and Codex.
2. Ask each Agent to output only the structured classification.
3. Compare each output against `expected-results.yaml`.
4. Pass valid classifications through the Router.
5. Measure:

- exact classification match
- valid enum rate
- Router path match
- unresolved rate

Targets:

- standard cases: `100%` exact match
- boundary cases: `>=95%`
- invalid enum rate: `0`
- Router path consistency: `100%`
- implicit Inbox routing: `0`

Do not add an LLM API evaluation runner in this task.

