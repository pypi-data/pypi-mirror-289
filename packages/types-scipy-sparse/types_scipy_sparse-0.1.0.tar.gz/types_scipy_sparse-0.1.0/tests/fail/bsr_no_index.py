import numpy as np
from scipy.sparse import bsr_array

sparr = bsr_array([[0, 1], [1, 0]], dtype=np.int32)

sparr[0, 1]  # E: Invalid index type

sparr[0, 1] = 2  # E: Invalid index type
