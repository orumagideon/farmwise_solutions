# db/models/equipment.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship
from db.base import Base

class Equipment(Base):
    __tablename__ = "equipment"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    equipment_name = Column(String, nullable=False)
    description = Column(String)
    lease_price = Column(Float, nullable=False)
    available = Column(String, default="yes")  # "yes" or "no"
    image = Column(LargeBinary, nullable=True)  # Store image as binary data

    # Relationship with User
    user = relationship("User", back_populates="equipment")
