from core.scraper import SCRAPER
from fastapi import APIRouter


scrouter = APIRouter()


@scrouter.get("/")
async def scrape():
    return SCRAPER.scrape_bundles()
