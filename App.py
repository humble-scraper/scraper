#!/usr/bin/env python3


from core.scraper import Scraper
from time import sleep
from fastapi import FastAPI


app = FastAPI()


def print_bundles(scraper: Scraper) -> None:
    elements = scraper.scrape_bundles()
    print(elements)
    for ele in elements:
        print(ele[0])


def main() -> None:
    scraper = Scraper()
    while True:
        print_bundles(scraper)
        print("-----------------------------------------------------------------")
        sleep(1)


if __name__ == "__main__":
    app.run()
    main()
