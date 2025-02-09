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

# Route to post produce
@router.post("/produce/", response_model=ProduceOut, status_code=status.HTTP_201_CREATED)
def create_produce(produce: ProduceCreate, db: Session = Depends(get_db)):
    db_produce = Produce(**produce.dict())
    db.add(db_produce)
    db.commit()
    db.refresh(db_produce)
    return db_produce

# Route to get all produce
@router.get("/produce/", response_model=list[ProduceOut])
def get_all_produce(db: Session = Depends(get_db)):
    produce = db.query(Produce).all()
    return produce

# Route to get a single produce by ID
@router.get("/produce/{produce_id}", response_model=ProduceOut)
def get_produce(produce_id: int, db: Session = Depends(get_db)):
    produce = db.query(Produce).filter(Produce.id == produce_id).first()
    if not produce:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produce not found")
    return produce