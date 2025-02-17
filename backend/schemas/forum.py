# schemas/forum.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

# Schema for creating a forum post
class ForumPostCreate(BaseModel):
    content: str
    user_id: int

    class Config:
        from_attributes = True  # Updated to comply with Pydantic V2

# Schema for updating a forum post
class ForumPostUpdate(BaseModel):
    content: Optional[str] = None

    class Config:
        from_attributes = True  # Updated to comply with Pydantic V2

# Schema for creating a forum reply
class ForumReplyCreate(BaseModel):
    post_id: int
    user_id: int
    content: str

    class Config:
        from_attributes = True  # Updated to comply with Pydantic V2

# Schema for returning a forum reply
class ForumReplyOut(BaseModel):
    id: int
    post_id: int
    user_id: int
    content: str
    created_at: datetime

    class Config:
        from_attributes = True  # Updated to comply with Pydantic V2

# Schema for returning a forum post
class ForumPostOut(BaseModel):
    id: int
    content: str
    upvotes: int
    downvotes: int
    created_at: datetime
    user_id: int
    replies: List[ForumReplyOut] = []

    class Config:
        from_attributes = True  # Updated to comply with Pydantic V2
