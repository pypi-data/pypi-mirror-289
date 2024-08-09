
__version__ = "1.0.5"

import os

# Set ENV Variables (place before imports)
os.environ["OMP_NUM_THREADS"] = "1"  # reduce CPU utilization during training

from ycsai.models import Engine

__all__ = (
    "__version__",
    "Engine",
)
