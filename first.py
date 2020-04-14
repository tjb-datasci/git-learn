import numpy as np
import pandas as pd

x = np.linspace(-10, 10)
print(x)

x_log = np.log(x).dropna()
print(x_log)
