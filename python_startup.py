_locals_pre_startup = [x for x in locals()]

import random
import datetime
import time
import timeit

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

_new_locals = [
    x
    for x in locals()
    if x not in _locals_pre_startup and x[0] != "_"
]
print(
    "imported a bunch of things:\n"
    + ", ".join(_new_locals)
)
