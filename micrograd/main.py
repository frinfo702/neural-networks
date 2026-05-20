import math

import matplotlib.pyplot as plt
import numpy as np
import test
from engine import Value

# %%
a = Value(2.0)
b = Value(-3.0)
c = Value(10.0)
d = a * b + c
print(d)
print(d._prev)

if __name__ == "__main__":
    test.test()
