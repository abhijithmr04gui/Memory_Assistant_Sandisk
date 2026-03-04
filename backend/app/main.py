from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.memory_routes import router as memory_router
from app.api.chat_routes import router as chat_router


app = FastAPI(title="Memory OS")


# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # during development allow all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include API routes
app.include_router(memory_router)
app.include_router(chat_router)


@app.get("/")
def root():
    return {"message": "Memory OS Backend Running"}