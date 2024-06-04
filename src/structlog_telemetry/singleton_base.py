
class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs) -> dict:
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance
