import platform
from types import enum
from managers.mac_manager import MacManager

PlatformEnum = enum(
    'Windows',
    'Macintosh',
    'Linux',
)

platforms = []


class PlatformMeta(type):

    def __init__(cls, *args):
        super(PlatformMeta, cls).__init__(args)

        if cls.platform is None:
            return

        platforms.setdefault(cls.platform, []).append(cls)


class Platform(object):
    __metaclass__ = PlatformMeta
    platform = None

    @staticmethod
    def is_current_platform(os_string):
        return False

    @staticmethod
    def get_manager():
        return None


class Windows(Platform):
    platform = PlatformEnum.Windows

    @staticmethod
    def is_current_platform(os_string):
        return "Windows" in platform.system()


class Macintosh(Platform):
    platform = platform.Macintosh

    @staticmethod
    def is_current_platform(os_string):
        return "Darwin" in platform.system()

    @staticmethod
    def get_manager():
        return MacManager
    

class Linux(Platform):
    platform = PlatformEnum.Linux

    @staticmethod
    def is_current_platform(os_string):
        return "Linux" in platform.system()
