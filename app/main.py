from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import os

from app.core.config import settings
from app.api.endpoints import auth, users, swipe, chat

app = FastAPI(title=settings.PROJECT_NAME)

# CORS
origins = [
    settings.FRONTEND_URL,
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Routers
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(users.router, prefix="/api/users", tags=["users"])
app.include_router(swipe.router, prefix="/api/swipe", tags=["swipe"])
app.include_router(chat.router, prefix="/api/ws/chat", tags=["chat"])

# Static Files
if os.path.isdir("app/static"):
    app.mount("/assets", StaticFiles(directory="app/static/assets"), name="assets")
    # We don't mount "/" directly to avoid conflict with API, but we serve index.html for root and others

@app.get("/{full_path:path}")
async def serve_spa(full_path: str):
    # If API request, return 404 (handled by API router if matched, but here if not)
    if full_path.startswith("api"):
        return {"error": "Not found"}

    # Serve index.html for SPA routing
    if os.path.exists("app/static/index.html"):
        with open("app/static/index.html", "r") as f:
            return HTMLResponse(content=f.read(), status_code=200)
    return {"message": "Frontend not built yet. Run npm run build in frontend directory."}
