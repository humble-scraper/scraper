from fastapi import FastAPI

from .routers.scraping_router import scrouter


scrapp = FastAPI()
scrapp.include_router(scrouter)
