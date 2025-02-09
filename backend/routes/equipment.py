# routes/equipment.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.session import SessionLocal
from db.models.equipment import Equipment
from schemas.equipment import EquipmentCreate, EquipmentOut

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route to post equipment
@router.post("/equipment/", response_model=EquipmentOut, status_code=status.HTTP_201_CREATED)
def create_equipment(equipment: EquipmentCreate, db: Session = Depends(get_db)):
    db_equipment = Equipment(**equipment.dict())
    db.add(db_equipment)
    db.commit()
    db.refresh(db_equipment)
    return db_equipment

# Route to get all equipment
@router.get("/equipment/", response_model=list[EquipmentOut])
def get_all_equipment(db: Session = Depends(get_db)):
    equipment = db.query(Equipment).all()
    return equipment

# Route to get a single equipment by ID
@router.get("/equipment/{equipment_id}", response_model=EquipmentOut)
def get_equipment(equipment_id: int, db: Session = Depends(get_db)):
    equipment = db.query(Equipment).filter(Equipment.id == equipment_id).first()
    if not equipment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Equipment not found")
    return equipment