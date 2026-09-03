"""
LEARNER IMPLEMENTATION — Assignment DEV2

Implement the Pydantic model and helpers below. The auto-grader imports:
  import src.learner_ticket
"""
from __future__ import annotations

from typing import Any

# HINT: from pydantic import BaseModel, Field, ValidationError
# HINT: from typing import Literal
from pydantic import BaseModel, Field, ValidationError
from typing import Literal
import json

class SupportTicket(BaseModel):
    """
    Replace this stub with a real pydantic.BaseModel subclass.

    Required fields:
      - ticket_id: int
      - customer_name: str
      - issue: str   (Field min_length=10, max_length=500)
      - priority: Literal["low", "medium", "high"]
      - resolved: bool = False
    """

    ticket_id: int
    customer_name: str
    issue: str = Field(min_length=10, max_length=500)
    priority: Literal["low", "medium", "high"]
    resolved: bool = False 


def validate_ticket(payload: dict[str, Any]) -> SupportTicket:
    """
    Validate ``payload`` with SupportTicket.model_validate(...).
    Return the validated model instance.
    Let ValidationError propagate on bad data.
    """

    return SupportTicket.model_validate(payload)


def ticket_to_json(ticket: SupportTicket) -> str:
    """Return indented JSON (indent=2) via model_dump_json."""
    return ticket.model_dump_json(indent=2)


def load_and_validate(path: str) -> dict[str, Any]:
    """
    Load a JSON file from ``path``, validate with validate_ticket,
    and return a plain dict via model_dump().

    Useful for the entrypoint; grader may also call this.
    """
    with open(path, "r") as file:
        data = json.load(file)
    return validate_ticket(data)
