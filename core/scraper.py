from typing import Any, Dict, Generator, List, Optional, Tuple, Union

import requests
import json
from bs4 import BeautifulSoup


_HOME_PAGE = "https://www.humblebundle.com/"


class Scraper:
    _BOOK_TITLE_SEARCH: Dict[str, Any] = {
        "name": "span",
        "attrs": {
            "class": "front-page-art-image-text"
        }
    }

    def __init__(self, base_url: Optional[str] = _HOME_PAGE) -> None:
        super().__init__()
        self._base_url = base_url

    @property
    def url(self) -> str:
        return self._base_url

    @url.setter
    def url(self, new_url) -> None:
        self._base_url = new_url

    def scrape_bundles(self, with_books: Optional[bool] = False):
        return Scraper.scrape_bundles_from(base_url=self._base_url, with_books=with_books)

    @staticmethod
    def scrape_book(url: str) -> Generator[str, None, List[str]]:
        ls: List = list()
        for span in BeautifulSoup(
                    Scraper.__get_book_html(url), "html.parser"
                ).find_all(**Scraper._BOOK_TITLE_SEARCH):
            txt: str = span.get_text()
            ls.append(txt)
            yield txt
        return ls

    @staticmethod
    def __get_book_html(url: str) -> str:
        return requests.get(url).text

    @staticmethod
    def scrape_bundles_from(
            base_url: Optional[str] = _HOME_PAGE,
            with_books: Optional[bool] = False
            ) -> List[Tuple[str, str]]:
        got = requests.get(base_url)
        souped = BeautifulSoup(got.text, "html.parser")
        found: dict = json.loads(souped.find("script", {"id": "base-webpack-json-data"}).string)
        return list(
            Scraper.__to_name_url_dicts(
                Scraper.__to_full_urls(base_url, Scraper.__get_urls(found)),
                with_books)
        )

    @staticmethod
    def __get_urls(found: dict) -> Generator[str, None, None]:
        return (
            f["product_url"]
            for f in found["navbar"]["productTiles"]
            if "/books/" in f["product_url"]
        )

    @staticmethod
    def __to_full_urls(
            prefix: str,
            urls: Generator[str, None, None]
            ) -> Generator[str, None, None]:
        return (prefix + url for url in urls)

    @staticmethod
    def __to_name_url_dicts(
            full_urls: Generator[str, None, None],
            with_books: Optional[bool] = False
            ) -> Generator[Dict[str, Union[str, dict]], None, None]:
        return (
            {
                "name": url.split("/")[-1],
                "url": url,
                "books": list(Scraper.scrape_book(url))
            } if with_books else {
                "name": url.split("/")[-1],
                "url": url
            }
            for url in full_urls
        )


SCRAPER: Scraper = Scraper()
