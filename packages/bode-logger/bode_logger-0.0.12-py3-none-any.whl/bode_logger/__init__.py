from importlib.metadata import version
from bode_logger.bode_logger import _update_root_logger
from bode_logger.bode_logger import info, debug, warning, error, critical

__version__ = version("bode_logger")
del version

_update_root_logger()
del bode_logger
