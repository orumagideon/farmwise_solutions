# main.py
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.session import SessionLocal
from db.models.user import User
from schemas.user import UserCreate, UserOut
from core.security import get_password_hash
from core.config import settings
from db.base import Base  # Import Base here
from db.session import engine  # Import engine here

# Function to create database tables
def create_tables():
    Base.metadata.create_all(bind=engine)

# Function to start the FastAPI application
def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    create_tables()
    return app

# Create the FastAPI app
app = start_application()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route for user registration
@app.post("/users/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
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

# Route for the home page
@app.get("/")
def home():
    return {"msg": "Hello FastAPI🚀"}