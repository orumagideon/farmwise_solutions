# schemas/forum.py
from pydantic import BaseModel
from datetime import datetime

# Schema for creating a forum post
class ForumPostCreate(BaseModel):
    content: str
    user_id: int

# Schema for returning a forum post
class ForumPostOut(BaseModel):
    id: int
    content: str
    upvotes: int
    created_at: datetime
    user_id: int

    class Config:
        from_attributes = True  # Enables ORM mode