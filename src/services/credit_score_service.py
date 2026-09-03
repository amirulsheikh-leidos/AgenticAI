"""
Credit bureau lookup service.

Participants will implement the lookup logic. This is the enterprise
capability wrapped as an MCP tool in Activity 2.1 (src/mcp/mcp_server.py
calls get_credit_score() directly, in-process - MCP wraps this function's
capability for cross-process/cross-tool access, it does not replace it).
"""
import json
from pathlib import Path
from typing import Any, Dict


def load_business_data(filename: str) -> Dict[str, Any]:
    """Load a business data JSON file from data/business_data/. Prefilled -
    identical pattern to Bootcamp 1/2."""
    path = Path("data/business_data") / filename
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_credit_score(customer_id: str) -> Dict[str, Any]:
    """
    Look up a customer's credit bureau record (score, delinquencies, credit
    utilization) by customer_id.

    Load data/business_data/credit_scores.json via
    load_business_data(), search its "credit_scores" list for a matching
    customer_id, and return that record's full dict. If no record matches,
    return {"error": "Credit record not found", "customer_id": customer_id}
    instead of raising.
    """
    data = load_business_data("credit_scores.json")
    for record in data.get("credit_scores", []):
        if record.get("customer_id") == customer_id:
            return record
    return {"error": "Credit record not found", "customer_id": customer_id}
