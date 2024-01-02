from .banner import print_banner
from .version import __version__


class Singleton(object):
    _instances = {}  # dict([cls, instance])

    def __new__(cls, *args, **kwargs) -> dict:
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
            print_banner(cls.__name__, __version__)

        return cls._instances[cls]
