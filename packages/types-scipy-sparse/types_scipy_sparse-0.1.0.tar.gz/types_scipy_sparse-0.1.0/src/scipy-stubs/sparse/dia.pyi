__all__ = [
    "check_shape",
    "dia_matrix",
    "dia_matvec",
    "get_sum_dtype",
    "getdtype",
    "isshape",
    "isspmatrix_dia",
    "spmatrix",
    "upcast_char",
    "validateaxis",
]

from ._dia import dia_matrix as dia_matrix
from ._dia import isspmatrix_dia as isspmatrix_dia
from ._matrix import spmatrix as spmatrix
from ._sparsetools import dia_matvec as dia_matvec
from ._sputils import check_shape as check_shape
from ._sputils import get_sum_dtype as get_sum_dtype
from ._sputils import getdtype as getdtype
from ._sputils import isshape as isshape
from ._sputils import upcast_char as upcast_char
from ._sputils import validateaxis as validateaxis
