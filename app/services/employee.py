from sqlalchemy.orm import Session

from ..ai import ask_ai
from .knowledge import get_company_knowledge


def process_employee_request(
    db: Session,
    company_id: int,
    message: str,
) -> str:

    company_context = get_company_knowledge(
        db,
        company_id,
        message,
    )

    return ask_ai(
        message,
        company_context,
    )
