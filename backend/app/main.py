from fastapi import FastAPI
from app.api import auth

app = FastAPI(title="ECC AI Compliance Platform")

app.include_router(auth.router)

