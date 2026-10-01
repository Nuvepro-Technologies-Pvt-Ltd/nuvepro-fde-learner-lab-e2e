# FDE learner implementation package

This synthetic lab package is bound to the approved problem statement in
FDE API run `c7df7564-124b-4f45-b969-e5ee3a8acc46`, candidate hash
`e57763a1452e5ce5eae489572f513072f1fd28290ebacf7ac54e634d0ce46f61`.

The complete evidence-backed brief is in `problem-statement.json`.

The `dataset/` directory contains the complete learner-facing corpus: 30
fictional applications with salary slips, bank statements, PAN cards,
Aadhaar cards, passport photos, workflow events, keyed values, and evaluation
metadata. No real applicant or production data is included.

Run the starter locally with:

```bash
./.nuvepro/bootstrap.sh
./.venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8091
```
