# routes/equipment.py
from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from sqlalchemy.orm import Session
from db.session import get_db
from db.models.equipment import Equipment
from schemas.equipment import EquipmentCreate, EquipmentOut, EquipmentUpdate
from typing import List

# Create the router instance
router = APIRouter(prefix="/equipment", tags=["Equipment"])

# ──────────────────────────────────────────────────────────────
# 🔹 Route: Post Equipment (with optional image upload)
# ──────────────────────────────────────────────────────────────
@router.post("/", response_model=EquipmentOut, status_code=status.HTTP_201_CREATED)
def create_equipment(
    equipment: EquipmentCreate, 
    image: UploadFile = File(None), 
    db: Session = Depends(get_db)
):
    """
    Adds a new equipment listing with an optional image upload.
    """
    image_data = image.file.read() if image else None

    db_equipment = Equipment(
        equipment_name=equipment.equipment_name,
        description=equipment.description,
        lease_price=equipment.lease_price,
        user_id=equipment.user_id,
        image=image_data
    )
    db.add(db_equipment)
    db.commit()
    db.refresh(db_equipment)
    return db_equipment

# ──────────────────────────────────────────────────────────────
# 🔹 Route: Get All Equipment Listings
# ──────────────────────────────────────────────────────────────
@router.get("/", response_model=List[EquipmentOut])
def get_all_equipment(db: Session = Depends(get_db)):
    """
    Retrieves all equipment available for lease.
    """
    return db.query(Equipment).all()

# ──────────────────────────────────────────────────────────────
# 🔹 Route: Get Equipment by ID
# ──────────────────────────────────────────────────────────────
@router.get("/{equipment_id}", response_model=EquipmentOut)
def get_equipment(equipment_id: int, db: Session = Depends(get_db)):
    """
    Retrieves a single equipment item based on its ID.
    """
    equipment = db.query(Equipment).filter(Equipment.id == equipment_id).first()
    if not equipment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Equipment not found")
    return equipment

# ──────────────────────────────────────────────────────────────
# 🔹 Route: Update Equipment Description
# ──────────────────────────────────────────────────────────────
@router.put("/{equipment_id}", response_model=EquipmentOut)
def update_equipment(
    equipment_id: int, 
    equipment_update: EquipmentUpdate, 
    db: Session = Depends(get_db)
):
    """
    Updates the description of an existing equipment listing.
    """
    equipment = db.query(Equipment).filter(Equipment.id == equipment_id).first()
    if not equipment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Equipment not found")

    if equipment_update.description is not None:
        equipment.description = equipment_update.description

    db.commit()
    db.refresh(equipment)
    return equipment

# ──────────────────────────────────────────────────────────────
# 🔹 Route: Delete Equipment Listing
# ──────────────────────────────────────────────────────────────
@router.delete("/{equipment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_equipment(equipment_id: int, db: Session = Depends(get_db)):
    """
    Deletes an equipment listing based on its ID.
    """
    equipment = db.query(Equipment).filter(Equipment.id == equipment_id).first()
    if not equipment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Equipment not found")

    db.delete(equipment)
    db.commit()
    return {"message": "Equipment deleted successfully"}