__all__ = [
    "IndexMixin",
    "check_shape",
    "dok_matrix",
    "getdtype",
    "isdense",
    "isintlike",
    "isscalarlike",
    "isshape",
    "isspmatrix_dok",
    "itertools",
    "spmatrix",
    "upcast",
    "upcast_scalar",
]

import itertools as itertools

from ._dok import dok_matrix as dok_matrix
from ._dok import isspmatrix_dok as isspmatrix_dok
from ._index import IndexMixin as IndexMixin
from ._matrix import spmatrix as spmatrix
from ._sputils import check_shape as check_shape
from ._sputils import getdtype as getdtype
from ._sputils import isdense as isdense
from ._sputils import isintlike as isintlike
from ._sputils import isscalarlike as isscalarlike
from ._sputils import isshape as isshape
from ._sputils import upcast as upcast
from ._sputils import upcast_scalar as upcast_scalar
