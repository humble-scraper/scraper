#!/usr/bin/env python3.8

from typing import List
from bs4 import element
import requests
from bs4 import BeautifulSoup
from bs4.element import ResultSet
from requests.api import options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement

from core.scraper import BUNDLE_URL, TEST_URL, Scraper


def main():
    scraper = Scraper(TEST_URL, search_element=Scraper._BOOK_TITLE_SEARCH)
    for line in scraper.scrape_book():
        print(line)

    print("============================")

    props = {
        "name": "div",
        "attrs": {
                # "class": "bundle-dropdown-content-wrapper"
                "class": "js-bundle-dropdown"
        }
    }

    req = requests.get(BUNDLE_URL)
    element: ResultSet = BeautifulSoup(req.text, "html.parser").find_all(**props)

    got = element[0]

    print(element)
    print("============================")

    scraper = Scraper(
        BUNDLE_URL,
        props
    )

    for line in scraper.scrape_book():
        print(line)


def main2():
    # chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--window-size=1920,1080")
    # chrome_options.binary_location = "/usr/bin/google-chrome"
    # URL = "https://www.humblebundle.com/"
    # driver = webdriver.Chrome(executable_path="lib/chromedriver",
    #                           options=chrome_options)
    # driver.get(URL)
    # driver.find_element_by_class_name("js-bundle-dropdown").click()
    # div: WebElement = driver.find_element_by_class_name("bundle-dropdown-content-wrapper")
    # elements: List[WebElement] = div.find_elements_by_css_selector("span.name")
    elements = Scraper().scrape_bundles()
    print([ele.text for ele in elements])


if __name__ == "__main__":
    main2()
