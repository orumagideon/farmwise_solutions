from pydantic import BaseModel
from typing import Optional

# Schema for posting equipment
class EquipmentCreate(BaseModel):
    equipment_name: str
    description: Optional[str] = None
    lease_price: float

# Schema for returning equipment details
class EquipmentOut(BaseModel):
    id: int
    equipment_name: str
    description: Optional[str] = None
    lease_price: float
    available: str
    user_id: int

    class Config:
        from_attributes = True  # Enables ORM mode