from importlib.metadata import version
from .bode_logger import _update_root_logger
from .bode_logger import info, debug, warning, error, critical

__version__ = version("bode_logger")
_update_root_logger()

del bode_logger
del version