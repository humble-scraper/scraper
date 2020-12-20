from typing import List, Optional, Tuple

from core.scraper import SCRAPER
from fastapi import APIRouter

scrouter = APIRouter()


@scrouter.get("/")
async def scrape(scrape_books: Optional[bool] = False) -> List[Tuple[str, str]]:
    return SCRAPER.scrape_bundles_from(with_books=scrape_books)
