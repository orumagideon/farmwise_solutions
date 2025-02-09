# schemas/produce.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Schema for creating produce
class ProduceCreate(BaseModel):
    product_name: str
    description: Optional[str] = None
    price: float
    user_id: int

# Schema for returning produce details
class ProduceOut(BaseModel):
    id: int
    product_name: str
    description: Optional[str] = None
    price: float
    posted_at: datetime
    user_id: int

    class Config:
        from_attributes = True  # Enables ORM mode (previously `orm_mode = True`)