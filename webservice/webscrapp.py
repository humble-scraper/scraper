from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers.scraping_router import scrouter


scrapp = FastAPI()
scrapp.include_router(scrouter)
scrapp.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_origins=[
        "http://localhost",
        "http://localhost:3000"
    ]
)
