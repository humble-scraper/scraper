from core.Scraper import TEST_URL, Scraper


def main():
    scraper: Scraper = Scraper(TEST_URL)
    for line in scraper.get_books():
        print(line)


if __name__ == "__main__":
    main()
