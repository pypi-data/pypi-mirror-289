from importlib.metadata import version
from ._bode_logger import _update_root_logger
from ._bode_logger import info, debug, warning, error, critical

__version__ = version("bode_logger")
del version

_update_root_logger()
