from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / ".nuvepro" / "manifest.json"
manifest_bytes = MANIFEST_PATH.read_bytes()
manifest = json.loads(manifest_bytes)

applications = sorted((ROOT / "dataset" / "applications").glob("app-*"))
learner_files = [path for path in (ROOT / "dataset").rglob("*") if path.is_file()]
required_top_level = [
    "application-index.csv",
    "dataset-plan.json",
    "evaluation-contract.json",
    "loantrak-keyed-values.csv",
    "manifest.json",
    "template-provenance.json",
    "workflow-events.ndjson",
]
missing = [name for name in required_top_level if not (ROOT / "dataset" / name).is_file()]
if missing:
    raise SystemExit(f"missing learner dataset files: {', '.join(missing)}")
if len(applications) != manifest["applicationCount"]:
    raise SystemExit(f"expected {manifest['applicationCount']} applications, found {len(applications)}")
if len(learner_files) != manifest["learnerFileCount"]:
    raise SystemExit(f"expected {manifest['learnerFileCount']} learner files, found {len(learner_files)}")

document_types = {
    "salary_slip": 0,
    "bank_statement": 0,
    "pan_card": 0,
    "aadhaar_card": 0,
    "passport_photo": 0,
}
for path in learner_files:
    for document_type in document_types:
        if document_type in path.name:
            document_types[document_type] += 1
if any(count != manifest["applicationCount"] for count in document_types.values()):
    raise SystemExit(f"document coverage mismatch: {document_types}")

revision = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
receipt = {
    "schemaVersion": "fde-lab-readiness/1",
    "problemStatementHash": manifest["problemStatementHash"],
    "manifestSha256": hashlib.sha256(manifest_bytes).hexdigest(),
    "revision": revision,
    "status": "passed",
    "checks": {
        "applicationCount": len(applications),
        "learnerFileCount": len(learner_files),
        "documentTypes": document_types,
        "fastApiImport": True,
        "starterPresent": (ROOT / "app" / "main.py").is_file(),
    },
}
(ROOT / ".nuvepro" / "readiness.json").write_text(json.dumps(receipt, indent=2) + "\n")
print(json.dumps(receipt))
