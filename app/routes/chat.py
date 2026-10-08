from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Company
from ..schemas import ChatRequest, ChatResponse
from ..services.employee import process_employee_request


router = APIRouter(
    prefix="/api/chat",
    tags=["chat"],
)


@router.post("", response_model=ChatResponse)
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db),
):
    company = (
        db.query(Company)
        .filter(Company.id == request.company_id)
        .first()
    )

    if not company:
        raise HTTPException(
            status_code=404,
            detail="Company not found",
        )

    answer = process_employee_request(
        db,
        request.company_id,
        request.message,
    )

    return ChatResponse(answer=answer)
