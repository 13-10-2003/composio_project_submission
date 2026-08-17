"""
Composio AI Product Ops research agent
--------------------------------------
This is a reproducible scaffold. It reads data/apps.csv, asks an LLM to produce
structured research, and requires evidence URLs for every material claim.

Set OPENAI_API_KEY and plug in your preferred web-search implementation.
The included seed dataset is the submission snapshot; this agent is the
reproducible research path for refreshing it.
"""

import csv, json, os
from pathlib import Path

SCHEMA = {
  "app_name": "string",
  "category": "string",
  "one_line_description": "string",
  "auth_methods": ["OAuth2", "API key", "Bearer/token", "Basic", "Other", "Unknown"],
  "credential_access": ["Self-serve", "Self-serve with restrictions", "Self-serve trial", "Paid", "Paid/admin approval", "Admin approval", "Contact sales", "Unknown"],
  "api_protocols": "REST | GraphQL | REST + GraphQL | REST/limited | None | Unknown",
  "api_breadth": "Broad | Moderate | Narrow | Unknown",
  "mcp_available": "Official | Third-party ecosystem | None found | Unknown",
  "buildability": "High | Medium | Low | Unknown",
  "main_blocker": "string",
  "evidence_urls": ["official URLs"],
  "confidence": "High | Medium | Low",
  "notes": "string"
}

SYSTEM = """You are an evidence-first product research agent.
Research only from sources you can cite. Prefer official developer/API/auth/pricing
documentation. Never invent URLs or facts. If a claim cannot be established,
return Unknown. Separate facts from inference. Return JSON matching the schema.
"""

def build_prompt(app, category, seed_url):
    return f"""{SYSTEM}

Research this application:
App: {app}
Category: {category}
Seed URL: {seed_url}

Answer the fields in this schema:
{json.dumps(SCHEMA, indent=2)}

For each major conclusion provide a source URL. Search specifically for:
1) authentication
2) developer credential creation/access
3) API protocol and breadth
4) MCP support
5) restrictions/approval/pricing
6) buildability implications.
"""

def main():
    path = Path("data/apps.csv")
    if not path.exists():
        raise SystemExit("Create data/apps.csv first.")
    with path.open(encoding="utf-8") as f:
        apps = list(csv.DictReader(f))
    print(f"Loaded {len(apps)} applications.")
    print("Next step: connect your web-search + LLM tool implementation and emit research_results.json.")
    print("The final pipeline should run: discovery -> extraction -> evidence validation -> confidence -> human-review queue.")

if __name__ == "__main__":
    main()
