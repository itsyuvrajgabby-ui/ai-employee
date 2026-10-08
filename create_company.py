from app.database import Base, engine, SessionLocal
from app.models import Company

Base.metadata.create_all(bind=engine)

db = SessionLocal()

company = Company(
    name="Demo Business"
)

db.add(company)
db.commit()
db.refresh(company)

print("Company created!")
print("Company ID:", company.id)

db.close()
