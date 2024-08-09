import os
import os.path as osp
import logging
import logging.config
from logging.handlers import RotatingFileHandler
import platform
from tqdm import tqdm as tqdm_original
import threading

# PyTorch Multi-GPU DDP Constants
RANK = int(os.getenv("RANK", -1))
LOCAL_RANK = int(os.getenv("LOCAL_RANK", -1))  # https://pytorch.org/docs/stable/elastic/run.html

# Other Contants
PYTHON_VERSION = platform.python_version()
NUM_THREADS = min(8, max(1, os.cpu_count() - 1))  # number of YOLO multiprocessing threads
VERBOSE = str(os.getenv("YCSAI_VERBOSE", True)).lower() == "true"  # global verbose mode
TQDM_BAR_FORMAT = "{l_bar}{bar:10}{r_bar}" if VERBOSE else None  # tqdm bar format
FONT = 'Arial.ttf'  # https://ultralytics.com/assets/Arial.ttf
GIT_INFO = None

# Logging
LOGGING_NAME = "YCSAI"
def set_logger():
    logger = logging.getLogger(LOGGING_NAME)
    logger.setLevel(logging.INFO)

    # if not osp.exists('logs'):
    #     os.makedirs('logs', exist_ok=True)
    # file_logger = RotatingFileHandler('logs/' + LOGGING_NAME + '.log', maxBytes=10240, backupCount=10)
    # file_logger.setFormatter(logging.Formatter(fmt='%(asctime)s %(levelname)s: %(message)s'))
    # file_logger.setLevel(logging.INFO)
    # logger.addHandler(file_logger)

    return logger
LOGGER = set_logger()

class TQDM(tqdm_original):
    """
    Custom Ultralytics tqdm class with different default arguments.

    Args:
        *args (list): Positional arguments passed to original tqdm.
        **kwargs (any): Keyword arguments, with custom defaults applied.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize custom Ultralytics tqdm class with different default arguments.

        Note these can still be overridden when calling TQDM.
        """
        kwargs["disable"] = not VERBOSE or kwargs.get("disable", False)  # logical 'and' with default value if passed
        kwargs.setdefault("bar_format", TQDM_BAR_FORMAT)  # override default value if passed
        super().__init__(*args, **kwargs)

def threaded(func):
    # Multi-threads a target function and returns thread. Usage: @threaded decorator
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs, daemon=True)
        thread.start()
        return thread

    return wrapper





