from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "dataset"
app = FastAPI(title="FDE Document Verification Lab")


def summary() -> dict[str, object]:
    applications = sorted((DATASET / "applications").glob("app-*"))
    documents = [path for path in (DATASET / "applications").rglob("*.pdf")]
    types = Counter()
    for path in documents:
        for name in ("salary_slip", "bank_statement", "pan_card", "aadhaar_card", "passport_photo"):
            if name in path.name:
                types[name] += 1
    return {
        "applications": len(applications),
        "documents": len(documents),
        "documentTypes": dict(sorted(types.items())),
        "indexRows": sum(1 for _ in csv.DictReader((DATASET / "application-index.csv").open())),
    }


@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "healthy"}


@app.get("/api/dataset")
def dataset_summary() -> dict[str, object]:
    return summary()


@app.get("/", response_class=HTMLResponse)
def home() -> str:
    details = summary()
    rows = "".join(f"<li><strong>{key}</strong>: {value}</li>" for key, value in details.items())
    return f"""<!doctype html><html><head><title>FDE Learner Lab</title>
    <style>body{{font:16px system-ui;max-width:900px;margin:48px auto;padding:0 24px}}code{{background:#eee;padding:2px 6px}}</style>
    </head><body><h1>Document Verification Salary-Slip Defect Identification</h1>
    <p>This sandbox is bound to the learner-approved problem statement. The complete synthetic learner corpus is under <code>dataset/</code>.</p>
    <ul>{rows}</ul><p>Implement the prototype in <code>app/</code>. Start the supplied API with <code>~/Desktop/start-fde-lab.sh</code>.</p>
    </body></html>"""
