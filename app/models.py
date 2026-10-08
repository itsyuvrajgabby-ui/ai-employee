from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)

    users = relationship(
        "User",
        back_populates="company",
        cascade="all, delete"
    )

    documents = relationship(
        "KnowledgeDocument",
        back_populates="company",
        cascade="all, delete"
    )


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    company_id = Column(
        Integer,
        ForeignKey("companies.id"),
        nullable=False,
        index=True
    )

    name = Column(String(200), nullable=False)
    email = Column(String(320), nullable=False)

    company = relationship(
        "Company",
        back_populates="users"
    )


class KnowledgeDocument(Base):
    __tablename__ = "knowledge_documents"

    id = Column(Integer, primary_key=True, index=True)

    company_id = Column(
        Integer,
        ForeignKey("companies.id"),
        nullable=False,
        index=True
    )

    filename = Column(String(500), nullable=False)
    content = Column(Text, nullable=False)

    company = relationship(
        "Company",
        back_populates="documents"
    )
