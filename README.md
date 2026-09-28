# FDE learner implementation package

This synthetic lab package is bound to the approved problem statement in
FDE run `d0435e00-7582-4aa2-b318-ae50fa18e7ab`.

The `dataset/` directory contains the complete learner-facing corpus: 30
fictional applications with salary slips, bank statements, PAN cards,
Aadhaar cards, passport photos, workflow events, keyed values, and evaluation
metadata. No real applicant or production data is included.

Run the starter locally with:

```bash
./.nuvepro/bootstrap.sh
./.venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8091
```
