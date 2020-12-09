#!/usr/bin/env python3.8


from typing import List

from selenium.webdriver.remote.webelement import WebElement
from core.scraper import Scraper


def print_bundles(scraper: Scraper) -> None:
    elements = scraper.scrape_bundles()
    print(elements)


def main() -> None:
    scraper = Scraper()
    # bundles: List[WebElement] = scraper.scrape_bundles()
    print_bundles(scraper)


if __name__ == "__main__":
    main()
