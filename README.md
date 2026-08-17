# Composio AI Product Ops — 100-App Research

## What this is

An evidence-first research pipeline for the Composio AI Product Ops take-home.
The project studies 100 applications across 10 categories and structures:
authentication, credential access, API surface, MCP availability, buildability,
blockers, confidence and evidence.

## Important honesty note

The included HTML is a **research snapshot**. A subset of 12 applications was
independently checked against current official documentation during preparation.
The remaining rows use the assignment's official seed URLs plus structured
research classifications and should be re-checked before claiming a fully
audited production dataset. This distinction is intentional: the assignment
explicitly asks candidates to report misses honestly rather than fabricate
accuracy.

## Architecture

Input apps -> research agent -> official-source discovery -> structured extraction
-> evidence validation -> confidence -> human review -> analysis -> HTML case study.

## Files

- `data/research_results.csv` — 100-app structured dataset
- `data/research_results.json` — same dataset in JSON
- `data/verification.csv` — independently checked sample
- `agent/researcher.py` — reproducible research-agent scaffold
- `agent/verifier.py` — sampling helper
- `output/index.html` — self-contained case study

## Run

```bash
python agent/researcher.py
python agent/verifier.py
```

To refresh the dataset, connect `researcher.py` to a web-search provider and an
LLM with structured-output support. The research prompt should require official
evidence URLs and an explicit Unknown state.

## Verification

The audited sample contains 12 applications spanning CRM, support, ecommerce,
developer, finance and AI categories. The sample was checked against official
documentation. The page intentionally separates this audited sample from the
full 100-row research snapshot.

## Buildability rubric

High = practical public API + workable credentials/access.
Medium = API is viable but access, approval, pricing or restrictions add friction.
Low = public integration path is severely restricted or not practically available.
Unknown = insufficient evidence.

## Submission

Deploy `output/index.html` as the case study and publish this repository as the
source. Before final submission, replace the repository URL and live URL
placeholders in the HTML.
