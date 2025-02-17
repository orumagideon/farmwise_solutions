# schemas/equipment.py
from pydantic import BaseModel
from typing import Optional

# Schema for creating equipment
class EquipmentCreate(BaseModel):
    equipment_name: str
    description: Optional[str] = None
    lease_price: float
    user_id: int

# Schema for updating equipment
class EquipmentUpdate(BaseModel):
    description: Optional[str] = None

# Schema for returning equipment details
class EquipmentOut(BaseModel):
    id: int
    equipment_name: str
    description: Optional[str] = None
    lease_price: float
    available: str
    user_id: int
    image: Optional[bytes] = None  # Store image data as bytes

    class Config:
        from_attributes = True  # Enables ORM mode
