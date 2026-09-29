# FDE learner implementation package

This synthetic lab package is bound to the approved problem statement in
FDE API run `882d451d-4393-4d7f-9c99-d548b9b5948d`, candidate hash
`9e21aaf1012cda1d7966b320a2ff7b8e4c551265d02f085e074a6614ebb490fa`.

The `dataset/` directory contains the complete learner-facing corpus: 30
fictional applications with salary slips, bank statements, PAN cards,
Aadhaar cards, passport photos, workflow events, keyed values, and evaluation
metadata. No real applicant or production data is included.

Run the starter locally with:

```bash
./.nuvepro/bootstrap.sh
./.venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8091
```
