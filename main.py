from fastapi import FastAPI
from app.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware
from app.routers import history
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI(title="FastAPI + SQL Server Demo")

app.include_router(history.router)

# ============================
# Correct upload directory
# ============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))     # DOAN2_BE/
UPLOAD_DIR = os.path.join(BASE_DIR, "app", "uploads")     # DOAN2_BE/app/uploads

# Ensure folder exists
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Serve static files
app.mount("/uploads", StaticFiles(directory=UPLOAD_DIR), name="uploads")

# ==== Add CORS middleware ====
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI + SQL Server!"}
