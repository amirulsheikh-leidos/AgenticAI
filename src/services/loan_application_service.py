"""
Loan application lookup service.

TODO: Participants will implement the lookup logic (Activity 1.1 exploration
uses this; it is exercised for real starting Activity 1.2/1.3).
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


def get_loan_application(application_id: str) -> Dict[str, Any]:
    """
    Look up a loan application (applicant, requested amount, tenure, income,
    employment status, etc.) by its application_id.

    TODO: Load data/business_data/loan_applications.json via
    load_business_data(), search its "applications" list for a matching
    application_id, and return that application's full dict. If no
    application matches, return
    {"error": "Application not found", "application_id": application_id}
    instead of raising.
    """
    data = load_business_data("loan_applications.json")

    # TODO: search data["applications"] for application_id and return the
    # match, or the not-found dict shape described above.
    raise NotImplementedError("Loan application lookup not implemented - see src/services/loan_application_service.py")
