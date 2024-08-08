from typing import Any
from pykit.err import ValueErr
from pykit.query import Query
from pymongo import MongoClient
from codo.engine import Engine

class MongoEngine(Engine):
    _META_OBJ_KEY = "codo"

    def __init__(self, url: str, *args):
        super().__init__(url)
        self._client  = MongoClient(self._url)
        dbname = args[0]
        if not isinstance(dbname, str):
            raise ValueErr(f"dbname should be str, got {dbname}")
        self._db = self._client[dbname]

    def get_version(self) -> str:
        obj: Any | None = self._db[self._META_OBJ_KEY].find_one()
        if obj is None:
            raise ValueErr("db is not initialized")
        assert isinstance(obj, dict)

        version = obj.get("version", None)
        if version is None:
            raise ValueErr(
                "db is not correctly initialize,"
                f" meta obj {self._META_OBJ_KEY} does not contain valid"
                " schema")

        return version

    def execute(self, q: Query):
        !!
        return self._db[self._META_OBJ_KEY].update_one

