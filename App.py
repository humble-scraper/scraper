#!/usr/bin/env python3.8

from core.scraper import TEST_URL, Scraper, BUNDLE_URL


def main():
    scraper = Scraper(TEST_URL, search_element=Scraper.BOOK_TITLE_SEARCH)
    for line in scraper.scrape():
        print(line)

    # print("============================")

    scraper = Scraper(BUNDLE_URL, {"name": "div", "attrs": {
                      "class": "bundle-dropdown-content-wrapper"}})
    for line in scraper.scrape():
        print(line)


if __name__ == "__main__":
    main()
