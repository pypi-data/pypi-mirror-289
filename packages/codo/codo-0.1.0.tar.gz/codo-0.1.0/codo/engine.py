from pykit.query import Query

class Engine:
    MetaObjKey: str = ""

    def __init__(self, url: str, *args):
        self._url = url

    def get_version(self) -> str:
        raise NotImplementedError

    def execute(self, q: Query):
        raise NotImplementedError

