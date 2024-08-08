import numpy as np
import scipy.sparse as sp

# test is sensitive to formatting so let's disable black
# pylint: disable=line-too-long
# fmt: off

# test inits
x0 = sp.csr_matrix([[0, 0]], dtype=np.float32)
reveal_type(x0)  # E: scipy.sparse._csr.csr_matrix[Any, numpy.dtype[numpy.floating[numpy._typing._32Bit]]]

x1 = sp.csc_matrix((3, 4))
reveal_type(x1)  # E: scipy.sparse._csc.csc_matrix[Any, numpy.dtype[Any]]

x2 = sp.csc_array((3, 4), dtype=np.dtype(np.float64))
reveal_type(x2)  # E: scipy.sparse._csc.csc_array[Any, numpy.dtype[numpy.floating[numpy._typing._64Bit]]]

x3 = sp.csr_array([[0, 1], [2, 0]], dtype=np.dtype(np.int32))
reveal_type(x3)  # E: scipy.sparse._csr.csr_array[Any, numpy.dtype[numpy.signedinteger[numpy._typing._32Bit]]]

x4 = sp.csc_array(x3)
reveal_type(x4)  # E: scipy.sparse._csc.csc_array[Any, numpy.dtype[numpy.signedinteger[numpy._typing._32Bit]]]

x5 = sp.csc_array(x3, dtype=np.uint32)
reveal_type(x5)  # E: scipy.sparse._csc.csc_array[Any, numpy.dtype[numpy.unsignedinteger[numpy._typing._32Bit]]]

x6 = sp.csr_array(([1.0, 3.0, 2.0], [0, 2, 1], [0, 2, 3]), dtype=np.float32)
reveal_type(x6)  # E: scipy.sparse._csr.csr_array[Any, numpy.dtype[numpy.floating[numpy._typing._32Bit]]]

x7 = sp.csr_matrix(([1.0, 3.0, 2.0], ([0, 0, 1], [0, 2, 1])), dtype="f")
reveal_type(x7)  # E: scipy.sparse._csr.csr_matrix[Any, numpy.dtype[Any]]

x8 = sp.csc_array((3, 4), dtype=float)
reveal_type(x8)  # E: scipy.sparse._csc.csc_array[Any, numpy.dtype[Any]]

# test properties / attributes
reveal_type(x0.data)  # E: numpy.ndarray[Any, numpy.dtype[numpy.floating[numpy._typing._32Bit]]]
reveal_type(x7.data)  # E: numpy.ndarray[Any, numpy.dtype[Any]]
reveal_type(x0.indices)  # E: numpy.ndarray[Any, numpy.dtype[numpy.signedinteger[Any]]]
reveal_type(x0.indptr)  # E: numpy.ndarray[Any, numpy.dtype[numpy.signedinteger[Any]]]
reveal_type(x0.dtype)  # E: numpy.dtype[numpy.floating[numpy._typing._32Bit]]
reveal_type(x0.shape)  # E: builtins.tuple[builtins.int, ...]
reveal_type(x0.nnz)  # E: builtins.int
reveal_type(x0.has_sorted_indices)  # E: builtins.bool
reveal_type(x0.has_canonical_format)  # E: builtins.bool
reveal_type(x0.maxprint)  # E: builtins.int
reveal_type(x0.format)  # E: Literal['csr']

# test asformat methods
reveal_type(x3.tocsr(copy=True))  # E: scipy.sparse._csr.csr_array[Any, numpy.dtype[numpy.signedinteger[numpy._typing._32Bit]]]
reveal_type(x3.asformat("csr", copy=True))  # E: scipy.sparse._csr.csr_array[Any, numpy.dtype[numpy.signedinteger[numpy._typing._32Bit]]]

# other methods
reveal_type(x0.sum_duplicates())  # E: None
reveal_type(x0.sort_indices())  # E: None
reveal_type(x4.mean())  # E: numpy.floating[Any]
reveal_type(x4.sum())  # E: numpy.signedinteger[Any]
