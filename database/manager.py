

import atexit
from datetime import datetime
from typing import Optional, Union

import pymongo
from core.bundle import BookBundle
from pymongo import MongoClient


class Manager:
    def __init__(self,
                 db_url: Optional[str] = "mongodb://localhost:27017/",
                 db_name: Optional[str] = "humblebundle",
                 collection_name: Optional[str] = "bookbundles") -> None:
        super().__init__()
        self.__url = db_url
        self.__client = MongoClient(db_url)
        self.__db = self.__client[db_name]
        self.__collection = self.__db.get_collection(collection_name)
        atexit.register(self.close)

    @property
    def url(self) -> str:
        """The database URL to which this manager is connected

        Returns:
            str: The database url
        """
        return self.__url

    def get_bundle(self, bundle_name: str) -> BookBundle:
        """Find a Bundle in the database, by name

        Args:
            bundle_name (str): The Bundle to search for

        Returns:
            Bundle: A Bundle with the given name
        """
        bundle_dict = self.__collection.find_one({"name": bundle_name})
        if bundle_dict is None:
            return None
        else:
            return BookBundle.from_dict(bundle_dict)

    def save_bundle(self, bundle: BookBundle) -> bool:
        """Saves the given Bundle in the database

        Args:
            bundle (Bundle): The Bundle to be saved

        Returns:
            bool: Whether or not the bundle was successfully saved
        """
        if self.has_bundle(bundle):
            return True
        bundle_json = {"last_modified": datetime.utcnow()}
        bundle_json.update(bundle.json())
        self.__collection.insert_one(bundle_json)

    def get_most_recent_bundle(self) -> BookBundle:
        """Queries the database to find the most recent bundle

        Returns:
            Bundle: A Bundle if found, else None
        """
        got = self.__collection.find_one({}, sort=[("_id", pymongo.DESCENDING)])
        return BookBundle.from_dict(got) if got is not None else None

    def has_bundle(self, bundle: Union[BookBundle, str]) -> bool:
        """Check whether or not the database contains the given Bundle or name of Bundle

        Args:
            bundle (Union[Bundle, str]): A Bundle object or the name of a Bundle

        Returns:
            bool: True if the database contains the given Bundle, False otherwise
        """
        name = bundle.name if isinstance(bundle, BookBundle) else bundle
        return self.get_bundle(name) is not None

    def close(self) -> None:
        print("Closing database...")
        self.__client.close()


SCRANAGER = Manager()
