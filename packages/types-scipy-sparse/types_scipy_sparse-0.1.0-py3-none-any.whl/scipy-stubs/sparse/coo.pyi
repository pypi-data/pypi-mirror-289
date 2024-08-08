__all__ = [
    "SparseEfficiencyWarning",
    "check_reshape_kwargs",
    "check_shape",
    "coo_matrix",
    "coo_matvec",
    "coo_tocsr",
    "coo_todense",
    "downcast_intp_index",
    "getdata",
    "getdtype",
    "isshape",
    "isspmatrix_coo",
    "operator",
    "spmatrix",
    "to_native",
    "upcast",
    "upcast_char",
    "warn",
]
import operator as operator
from warnings import warn as warn

from ._base import SparseEfficiencyWarning as SparseEfficiencyWarning
from ._coo import coo_matrix as coo_matrix
from ._coo import isspmatrix_coo as isspmatrix_coo
from ._matrix import spmatrix as spmatrix
from ._sparsetools import coo_matvec as coo_matvec
from ._sparsetools import coo_tocsr as coo_tocsr
from ._sparsetools import coo_todense as coo_todense
from ._sputils import check_reshape_kwargs as check_reshape_kwargs
from ._sputils import check_shape as check_shape
from ._sputils import downcast_intp_index as downcast_intp_index
from ._sputils import getdata as getdata
from ._sputils import getdtype as getdtype
from ._sputils import isshape as isshape
from ._sputils import to_native as to_native
from ._sputils import upcast_char as upcast_char

upcast: None = None

# Names in __all__ with no definition:
#   upcast
