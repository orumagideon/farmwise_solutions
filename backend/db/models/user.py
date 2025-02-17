# db/models/user.py
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from db.base import Base

class User(Base):
    __tablename__ = "users"  # Explicitly define the table name

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    produce = relationship("Produce", back_populates="user")
    forum_posts = relationship("ForumPost", back_populates="user")
    equipment = relationship("Equipment", back_populates="user")
