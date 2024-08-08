from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

import numpy as np
import scipy.sparse as sp

if TYPE_CHECKING:
    from scipy.sparse.typing import SparseArray

# test generic types of classes
x1: SparseArray[Any] = sp.csc_matrix((3, 4))
x2: SparseArray[np.float64] = sp.csc_array((3, 4), dtype=np.dtype(np.float64))
x3: sp.sparray[Any, np.dtype[np.int_]] = sp.csr_array((3, 4), dtype=np.dtype(np.int32))
x4: sp.spmatrix[Any, np.dtype[np.complex_]] = sp.csr_matrix(
    (3, 4), dtype=np.dtype(np.complex128)
)
x5: sp.csr_matrix[Any, np.dtype[np.bool_]] = sp.csr_matrix(
    (3, 4), dtype=np.dtype(np.bool_)
)

# test different inits
y1: sp.csr_array[Any, np.dtype[np.float32]] = sp.csr_array(
    [[1, 0, 3], [0, 2, 0]],
    dtype=np.dtype(np.float32),
)
y2: sp.csr_array[Any, np.dtype[np.float32]] = sp.csr_array(
    ([1.0, 3.0, 2.0], [0, 2, 1], [0, 2, 3]),
    dtype=np.float32,
)
y3: sp.csr_matrix[Any, Any] = sp.csr_matrix(
    ([1.0, 3.0, 2.0], ([0, 0, 1], [0, 2, 1])), dtype="f"
)
y4: sp.csc_array[Any, Any] = sp.csc_array((3, 4), dtype=float)
y5: sp.csr_matrix[Any, np.dtype[np.int_]] = sp.csr_matrix(y4, dtype=np.int32)

# test dtype
y3_dtype: np.dtype[Any] = y3.dtype
y5_dtype: np.dtype[np.int_] = y5.dtype

# test asformat
f_csr: Literal["csr"] = y5.format
f_csr2: Literal["csr"] = y5.asformat("csr", copy=True).format
f_csc: Literal["csc"] = y5.asformat("csc", copy=True).format

# test sum and mean
y3_mean: np.float_ = y3.astype(np.int_).mean()
y3_sum: np.int_ = y3.astype(np.int_).sum()
y1_mean: np.float32 = y1.mean()
y1_sum: np.float32 = y1.sum()

z1: sp.dok_array[Any, np.dtype[np.int8]] = sp.dok_array(
    np.array([[1, 0, 3], [0, 2, 0]], dtype=np.int8)
)
