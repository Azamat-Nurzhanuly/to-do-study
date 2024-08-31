from fastapi import FastAPI
from router import router as items_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.include_router(items_router)

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)