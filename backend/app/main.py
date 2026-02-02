from fastapi import FastAPI
from app.api import auth, audit

app = FastAPI(title="ECC AI Compliance Platform")

app.include_router(auth.router)
app.include_router(audit.router)
