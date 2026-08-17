"""Verification helper.
Use this after a research run: sample rows, re-check official sources, and
record correct/incorrect outcomes in data/verification.csv.
"""
import csv, random
from pathlib import Path

def sample(n=12, seed=42):
    with open("data/research_results.csv", encoding="utf-8") as f:
        rows=list(csv.DictReader(f))
    random.seed(seed)
    return random.sample(rows, min(n,len(rows)))

if __name__ == "__main__":
    for row in sample():
        print(row["app_name"], "->", row["buildability"], "|", row["evidence_url"])
