from typing import Any, Dict, Generator, List, Tuple

import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


TEST_URL: str = "https://www.humblebundle.com/books/hacking-101-no-starch-press-books?hmb_source=humble_home&hmb_medium=product_tile&hmb_campaign=mosaic_section_2_layout_index_2_layout_type_twos_tile_index_1_c_hacking101nostarchpress_bookbundle"
BUNDLE_URL: str = "https://www.humblebundle.com/store"


class Scraper:
    _BOOK_TITLE_SEARCH: Dict[str, Any] = {
        "name": "span",
        "attrs": {
            "class": "front-page-art-image-text"
        }
    }

    # Initialize the selenium stuff
    _CHROME_OPTIONS = Options()
    _CHROME_OPTIONS.add_argument("--headless")
    _CHROME_OPTIONS.add_argument("--window-size=1920,1080")
    _CHROME_OPTIONS.binary_location = "/usr/bin/google-chrome"
    _EXECUTABLE_PATH = "lib/chromedriver"
    _HOME_PAGE = "https://www.humblebundle.com/"
    _DROP_DOWN_BUTTON_SELECTOR = ".js-bundle-dropdown"
    _BUNDLE_TITLE_SELECTOR = "a.bundle"

    def __init__(self, books_only: bool = True) -> None:
        super().__init__()
        self.books_only = books_only
        self.driver = Scraper.__init_web_driver()

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

    def scrape_bundles(self) -> List[Tuple[str, WebElement]]:
        self.driver.get(Scraper._HOME_PAGE)
        self.driver.find_element_by_css_selector(Scraper._DROP_DOWN_BUTTON_SELECTOR).click()
        elements = self.driver.find_elements_by_css_selector(Scraper._BUNDLE_TITLE_SELECTOR)
        elements = Scraper.__to_title_and_link_tuples(elements)
        if self.books_only:
            elements = Scraper.__filter_books_only(elements)
        elements = Scraper.__add_booklists(elements)
        return elements

    @staticmethod
    def __filter_books_only(elements: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
        return [
            ele for ele in elements
            if Scraper.__is_book_bundle(ele[0])
        ]

    @staticmethod
    def __is_book_bundle(title: str) -> bool:
        return re.match(r'humble book bundle', title, re.IGNORECASE) is not None

    @staticmethod
    def __to_title_and_link_tuples(elements: List[WebElement]) -> List[Tuple[str, str]]:
        return [
            e for e in [
                (
                    ele.find_element_by_css_selector("span.name").text,
                    ele.get_attribute("href")
                )
                for ele in elements
            ]
            if e[0] != ''
        ]

    @staticmethod
    def __add_booklists(elements: List[Tuple[str, str]]) -> List[Tuple[str, str, List[str]]]:
        return [
            (ele[0], ele[1], list(Scraper.scrape_book(ele[1])))
            for ele in elements
        ]

    @staticmethod
    def __init_web_driver() -> WebDriver:
        return webdriver.Chrome(
                executable_path=Scraper._EXECUTABLE_PATH,
                options=Scraper._CHROME_OPTIONS)

    @staticmethod
    def __get_book_html(url: str) -> str:
        return requests.get(url).text
