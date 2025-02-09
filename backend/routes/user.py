# routes/user.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.session import SessionLocal
from db.models.user import User
from schemas.user import UserCreate, UserOut, UserLogin
from core.security import get_password_hash, verify_password, create_access_token

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route for user registration
@router.post("/users/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Hash the password
    hashed_password = get_password_hash(user.password)
    # Create a new user instance
    db_user = User(username=user.username, email=user.email, password_hash=hashed_password)
    # Add the user to the database
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Route for user login
@router.post("/login/")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}