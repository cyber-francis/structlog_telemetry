from .banner import print_banner
from .version import __version__


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs) -> dict:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print_banner(cls.__name__, __version__)

        return cls._instance
