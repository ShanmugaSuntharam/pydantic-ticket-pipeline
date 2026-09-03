# Assignment DEV2 — Pydantic Support Ticket Pipeline

Starter for **Agentic AI Developer Bootcamp** Sessions 3–4 (dotenv + Pydantic contracts).

## Implement

Edit **`src/learner_ticket.py`**:

- `SupportTicket` (Pydantic `BaseModel`)
- `validate_ticket`
- `ticket_to_json`
- `load_and_validate`

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
PYTHONPATH=. python main.py
```

No OpenAI key is required for auto-grading.

## Reflection

1. Why validate external / LLM JSON with Pydantic before using it in code?
a) Since they are untrusted, it should be validated before using it
b) Pydantic gives the flexibility to manage the validation efficiently
2. What happened when you fed an invalid `priority`?
It throws an error, for e.g. priority
  Input should be 'low', 'medium' or 'high' [type=literal_error, input_value='medium-high', input_type=str]

## Repo root warning

Push the **contents** of `pydantic-ticket-pipeline/` as the GitHub repo root.
