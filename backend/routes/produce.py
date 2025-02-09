# routes/produce.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.session import SessionLocal
from db.models.produce import Produce
from schemas.produce import ProduceCreate, ProduceOut

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route to delete produce
@router.delete("/produce/{produce_id}")
def delete_produce(produce_id: int, db: Session = Depends(get_db)):
    db_produce = db.query(Produce).filter(Produce.id == produce_id).first()
    if not db_produce:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produce not found")
    db.delete(db_produce)
    db.commit()
    return {"message": "Produce deleted successfully"}