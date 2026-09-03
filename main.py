"""Thin entrypoint for Assignment DEV2 — Pydantic Support Ticket Pipeline."""
from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

from src.learner_ticket import load_and_validate, ticket_to_json, validate_ticket

ROOT = Path(__file__).resolve().parent
RAW_PATH = ROOT / "data" / "raw_ticket.json"


def main() -> int:
    load_dotenv()
    app_name = os.getenv("APP_NAME", "dev2")

    try:
        data = load_and_validate(str(RAW_PATH))
        ticket = validate_ticket(data)
        print(f"APP_NAME={app_name}")
        print("=== VALIDATED TICKET JSON ===")
        print(ticket_to_json(ticket))
    except Exception as error:  # noqa: BLE001 — learner-facing CLI
        print(f"Validation/pipeline error: {error}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
