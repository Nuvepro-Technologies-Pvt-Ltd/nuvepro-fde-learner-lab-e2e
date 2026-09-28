# FDE learner implementation package

This synthetic lab package is bound to the approved problem statement in
FDE API run `3eaa90a8-7cd6-45b0-9e84-13e5049d95c2`, candidate hash
`3bb68eb25db0f1909d5914d77b4dfceb923d64e47383cd1881726a29c83110f9`.

The `dataset/` directory contains the complete learner-facing corpus: 30
fictional applications with salary slips, bank statements, PAN cards,
Aadhaar cards, passport photos, workflow events, keyed values, and evaluation
metadata. No real applicant or production data is included.

Run the starter locally with:

```bash
./.nuvepro/bootstrap.sh
./.venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8091
```
