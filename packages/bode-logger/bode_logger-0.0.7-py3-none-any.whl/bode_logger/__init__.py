from importlib.metadata import version
from .bode_logger import update_root_logger
from .bode_logger import info, debug, warning, error, critical

__version__ = version("bode_logger")
update_root_logger()
