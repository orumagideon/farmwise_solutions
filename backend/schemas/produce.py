from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class ProduceCreate(BaseModel):
    product_name: str
    description: Optional[str] = None
    price: float
    quantity: int = Field(..., gt=0, description="Quantity should be greater than zero")
    phone_number: str
    location: str
    image_url: Optional[str] = None
    user_id: int

class ProduceUpdate(BaseModel):
    product_name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None
    phone_number: Optional[str] = None
    location: Optional[str] = None
    image_url: Optional[str] = None

class ProduceOut(BaseModel):
    id: int
    product_name: str
    description: Optional[str] = None
    price: float
    quantity: int
    phone_number: str
    location: str
    image_url: Optional[str] = None
    posted_at: datetime
    user_id: int

    class Config:
        from_attributes = True
