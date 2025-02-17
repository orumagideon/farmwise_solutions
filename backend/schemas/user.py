# schemas/user.py
from pydantic import BaseModel
from typing import Optional

# Schema for creating a user
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        from_attributes = True  # Updated to comply with Pydantic V2

# Schema for returning user information
class UserOut(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True  # Updated to comply with Pydantic V2

# Schema for user login (authentication)
class UserLogin(BaseModel):
    username: str
    password: str

    class Config:
        from_attributes = True  # Updated to comply with Pydantic V2
