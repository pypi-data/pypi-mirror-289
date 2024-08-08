__all__ = [
    "block_diag",
    "bmat",
    "bsr_matrix",
    "check_random_state",
    "coo_matrix",
    "csc_matrix",
    "csr_hstack",
    "csr_matrix",
    "dia_matrix",
    "diags",
    "eye",
    "get_index_dtype",
    "hstack",
    "identity",
    "isscalarlike",
    "issparse",
    "kron",
    "kronsum",
    "numbers",
    "rand",
    "random",
    "rng_integers",
    "spdiags",
    "upcast",
    "vstack",
]

import numbers as numbers

from ._base import issparse as issparse
from ._bsr import bsr_matrix as bsr_matrix
from ._construct import block_diag as block_diag
from ._construct import bmat as bmat
from ._construct import diags as diags
from ._construct import eye as eye
from ._construct import hstack as hstack
from ._construct import identity as identity
from ._construct import kron as kron
from ._construct import kronsum as kronsum
from ._construct import rand as rand
from ._construct import random as random
from ._construct import spdiags as spdiags
from ._construct import vstack as vstack
from ._coo import coo_matrix as coo_matrix
from ._csc import csc_matrix as csc_matrix
from ._csr import csr_matrix as csr_matrix
from ._dia import dia_matrix as dia_matrix
from ._sparsetools import csr_hstack as csr_hstack
from ._sputils import get_index_dtype as get_index_dtype
from ._sputils import isscalarlike as isscalarlike
from ._sputils import upcast as upcast

from scipy._lib._util import (  # type: ignore[import-untyped] # isort: skip
    check_random_state as check_random_state,
    rng_integers as rng_integers,
)
