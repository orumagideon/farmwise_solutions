from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
from core.config import settings

# Configure the database engine
engine = create_engine(settings.DATABASE_URL)

# Configure the session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
