_locals_pre_startup = [x for x in locals()]

import random
import datetime
import json
import math
import time
import timeit
from pathlib import Path

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

try:
    import untappd
except ImportError:
    pass

_new_locals = [
    x
    for x in locals()
    if x not in _locals_pre_startup and x[0] != "_"
]
print(
    "imported a bunch of things:\n"
    + ", ".join(_new_locals)
)
