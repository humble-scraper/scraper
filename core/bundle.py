

from typing import Dict, List, Optional, Union
import json


class Book:
    def __init__(self, name: str, url: str) -> None:
        super().__init__()
        self.__name = name
        self.__url = url

    @property
    def name(self):
        return self.__name

    @property
    def url(self):
        return self.__url

    @classmethod
    def from_dict(cls, my_dict: Dict[str, str]) -> "Book":
        return cls(
            name=my_dict["name"],
            url=my_dict["url"]
        )

    def json(self) -> Dict[str, str]:
        return {
            "name": self.name,
            "url": self.url
        }

    def __str__(self) -> str:
        return self.name


class BookBundle:
    def __init__(self, name: str, url: str, booklist: Optional[List[Book]]) -> None:
        super().__init__()
        self.__name = name
        self.__url = url
        self.__booklist = booklist

    @property
    def name(self) -> str:
        return self.__name

    @property
    def url(self) -> str:
        return self.__url

    @property
    def booklist(self) -> List[Book]:
        return self.__booklist

    @property
    def number_of_books(self) -> int:
        return len(self.booklist)

    @classmethod
    def from_json(cls, my_json: str) -> "BookBundle":
        return BookBundle.from_dict(json.loads(my_json))

    @classmethod
    def from_dict(cls, my_dict: Dict[str, Union[str, List[dict]]]) -> "BookBundle":
        return cls(
            name=my_dict["name"],
            url=my_dict["url"],
            booklist=[Book.from_dict(book_dict) for book_dict in my_dict["books"]]
        )

    def json(self) -> Dict[str, Union[str, List[Book]]]:
        return {
            "name": self.name,
            "url": self.url,
            "books": [book.json() for book in self.booklist]
        }

    def __str__(self) -> str:
        return self.name
