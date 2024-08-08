__all__ = [
    "bsr_matmat",
    "bsr_matrix",
    "bsr_matvec",
    "bsr_matvecs",
    "bsr_sort_indices",
    "bsr_tocsr",
    "bsr_transpose",
    "check_shape",
    "csr_matmat_maxnnz",
    "getdata",
    "getdtype",
    "isshape",
    "isspmatrix_bsr",
    "spmatrix",
    "to_native",
    "upcast",
    "warn",
]

from warnings import warn as warn

from ._bsr import bsr_matrix as bsr_matrix
from ._bsr import isspmatrix_bsr as isspmatrix_bsr
from ._matrix import spmatrix as spmatrix
from ._sparsetools import bsr_matmat as bsr_matmat
from ._sparsetools import bsr_matvec as bsr_matvec
from ._sparsetools import bsr_matvecs as bsr_matvecs
from ._sparsetools import bsr_sort_indices as bsr_sort_indices
from ._sparsetools import bsr_tocsr as bsr_tocsr
from ._sparsetools import bsr_transpose as bsr_transpose
from ._sparsetools import csr_matmat_maxnnz as csr_matmat_maxnnz
from ._sputils import check_shape as check_shape
from ._sputils import getdata as getdata
from ._sputils import getdtype as getdtype
from ._sputils import isshape as isshape
from ._sputils import to_native as to_native
from ._sputils import upcast as upcast
