from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import auth, audit, ai

app = FastAPI(
    title="ECC AI Compliance Platform",
    version="1.0.0",
    description="AI-powered platform for ECC compliance assessment and guidance"
)

# ==================================================
# CORS 
# ==================================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # لاحقًا نخليها محددة
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==================================================
# Register API Routers
# ==================================================
app.include_router(auth.router)
app.include_router(audit.router)
app.include_router(ai.router)


# ==================================================
# Health Check
# ==================================================
@app.get("/")
def root():
    return {
        "status": "running",
        "service": "ECC AI Compliance Platform"
    }
