# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
from db.base import Base
from db.session import engine
from routes.user import router as user_router
from routes.produce import router as produce_router
from routes.forum import router as forum_router
from routes.equipment import router as equipment_router

# Function to create database tables
def create_tables():
    Base.metadata.create_all(bind=engine)

# Function to start the FastAPI application
def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    
    # Enable CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000"],  # Allow frontend origin
        allow_credentials=True, 
        allow_methods=["*"],  # Allow all methods
        allow_headers=["*"],  # Allow all headers
    ) 
    
    create_tables()  # Ensure tables are created when the app starts
    return app

# Create the FastAPI app
app = start_application()

# Include routers with appropriate prefixes
app.include_router(user_router)  # No need for prefix here since it's already defined in the router
app.include_router(produce_router, prefix="/api/produce")
app.include_router(forum_router, prefix="/api/forum")
app.include_router(equipment_router, prefix="/api/equipment")

# Route for the home page
@app.get("/")
def home():
    return {"msg": "Hello FastAPI🚀"}
