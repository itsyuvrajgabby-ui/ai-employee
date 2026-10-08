from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    company_id: int
    message: str = Field(
        min_length=1,
        max_length=10000,
    )


class ChatResponse(BaseModel):
    answer: str


class CompanyCreate(BaseModel):
    name: str = Field(
        min_length=1,
        max_length=200,
    )


class UserCreate(BaseModel):
    company_id: int
    name: str
    email: str


class DocumentResponse(BaseModel):
    id: int
    filename: str
