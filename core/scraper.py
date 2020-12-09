from typing import Any, Dict, Generator, List

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
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

    _BUNDLE_TITLE_SEARCH: Dict[str, Any] = {
        "name": "span",
        "attrs": {"class": "name"}
    }

    # Initialize the selenium stuff
    _CHROME_OPTIONS = Options()
    _CHROME_OPTIONS.add_argument("--headless")
    _CHROME_OPTIONS.add_argument("--window-size=1920,1080")
    _CHROME_OPTIONS.binary_location = "/usr/bin/google-chrome"
    _EXECUTABLE_PATH = "lib/chromedriver"
    _HOME_PAGE = "https://www.humblebundle.com/"
    _DROP_DOWN_BUTTON_SELECTOR = ".js-bundle-dropdown"
    _BUNDLE_TITLE_SELECTOR = "span.name"

    def __init__(self) -> None:
        super().__init__()
        self.driver = Scraper.__init_web_driver()

    def scrape_book(self, url: str) -> Generator[str, None, List[str]]:
        ls: List = list()
        for span in BeautifulSoup(self.__get_book_html(),
                                  "html.parser").find_all(**self.search_element):
            txt: str = span.get_text()
            ls.append(txt)
            yield txt
        return ls

    def scrape_bundles(self) -> List[WebElement]:
        self.driver.get(Scraper._HOME_PAGE)
        self.driver.find_element_by_css_selector(Scraper._DROP_DOWN_BUTTON_SELECTOR).click()
        # div: WebElement = self.driver.find_element_by_class_name("bundle-dropdown-content-wrapper")
        elements: List[WebElement] = self.driver.find_elements_by_css_selector(
                Scraper._BUNDLE_TITLE_SELECTOR)
        return elements

    @staticmethod
    def __init_web_driver() -> WebDriver:
        return webdriver.Chrome(
                executable_path=Scraper._EXECUTABLE_PATH,
                options=Scraper._CHROME_OPTIONS)

    def __get_book_html(self) -> str:
        return requests.get(self.url).text

    def __repr__(self) -> Dict[str, Any]:
        return {"url": self.url, "search_element": self.search_element}

    def __str__(self) -> str:
        return self.url
