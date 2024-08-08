from collections.abc import Sequence
from typing import (
    Any,
    Literal,
    SupportsFloat,
    SupportsIndex,
    SupportsInt,
    overload,
)

import numpy as np
import numpy.typing as npt

from ._base import sparray
from ._bsr import bsr_array, bsr_matrix
from ._coo import coo_array, coo_matrix
from ._csc import csc_array, csc_matrix
from ._csr import csr_array, csr_matrix
from ._dia import dia_array, dia_matrix
from ._dok import dok_array, dok_matrix
from ._lil import lil_array, lil_matrix
from ._matrix import spmatrix
from .typing import (
    DataRVsType,
    DataSamplerType,
    SparseArray,
    _ArrayLike1DIndex,
    _DTypeLike,
    _SCT_co,
)

__all__ = [
    "spdiags",
    "eye",
    "identity",
    "kron",
    "kronsum",
    "hstack",
    "vstack",
    "bmat",
    "rand",
    "random",
    "diags",
    "block_diag",
    "diags_array",
    "block_array",
    "eye_array",
    "random_array",
]

@overload
def spdiags(
    data: npt.NDArray[_SCT_co],
    diags: _ArrayLike1DIndex | SupportsIndex,
    m: None | tuple[SupportsIndex, SupportsIndex] = ...,
    n: None = ...,
    format: None = ...,
) -> dia_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def spdiags(
    data: npt.ArrayLike,
    diags: _ArrayLike1DIndex | SupportsIndex,
    m: SupportsIndex = ...,
    n: SupportsIndex = ...,
    format: None = ...,
) -> dia_matrix[Any, Any]: ...
@overload
def spdiags(
    data: npt.NDArray[_SCT_co],
    diags: _ArrayLike1DIndex | SupportsIndex,
    m: None | tuple[SupportsIndex, SupportsIndex],
    n: None,
    format: Literal["csc"],
) -> csc_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def spdiags(
    data: npt.NDArray[_SCT_co],
    diags: _ArrayLike1DIndex | SupportsIndex,
    m: None | tuple[SupportsIndex, SupportsIndex] = ...,
    n: None = ...,
    *,
    format: Literal["csc"],
) -> csc_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def spdiags(
    data: npt.ArrayLike,
    diags: _ArrayLike1DIndex | SupportsIndex,
    m: SupportsIndex,
    n: SupportsIndex,
    format: Literal["csc"],
) -> csc_matrix[Any, Any]: ...
@overload
def spdiags(
    data: npt.NDArray[_SCT_co],
    diags: _ArrayLike1DIndex | SupportsIndex,
    m: None | tuple[SupportsIndex, SupportsIndex],
    n: None,
    format: Literal["csr"],
) -> csr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def spdiags(
    data: npt.NDArray[_SCT_co],
    diags: _ArrayLike1DIndex | SupportsIndex,
    m: None | tuple[SupportsIndex, SupportsIndex] = ...,
    n: None = ...,
    *,
    format: Literal["csr"],
) -> csr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def spdiags(
    data: npt.ArrayLike,
    diags: _ArrayLike1DIndex | SupportsIndex,
    m: SupportsIndex,
    n: SupportsIndex,
    format: Literal["csr"],
) -> csr_matrix[Any, Any]: ...
@overload
def spdiags(
    data: npt.NDArray[_SCT_co],
    diags: _ArrayLike1DIndex | SupportsIndex,
    m: None | tuple[SupportsIndex, SupportsIndex],
    n: None,
    format: Literal["coo"],
) -> coo_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def spdiags(
    data: npt.NDArray[_SCT_co],
    diags: _ArrayLike1DIndex | SupportsIndex,
    m: None | tuple[SupportsIndex, SupportsIndex] = ...,
    n: None = ...,
    *,
    format: Literal["coo"],
) -> coo_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def spdiags(
    data: npt.ArrayLike,
    diags: _ArrayLike1DIndex | SupportsIndex,
    m: SupportsIndex,
    n: SupportsIndex,
    format: Literal["coo"],
) -> coo_matrix[Any, Any]: ...
@overload
def spdiags(
    data: npt.NDArray[_SCT_co],
    diags: _ArrayLike1DIndex | SupportsIndex,
    m: None | tuple[SupportsIndex, SupportsIndex],
    n: None,
    format: Literal["bsr"],
) -> bsr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def spdiags(
    data: npt.NDArray[_SCT_co],
    diags: _ArrayLike1DIndex | SupportsIndex,
    m: None | tuple[SupportsIndex, SupportsIndex] = ...,
    n: None = ...,
    *,
    format: Literal["bsr"],
) -> bsr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def spdiags(
    data: npt.ArrayLike,
    diags: _ArrayLike1DIndex | SupportsIndex,
    m: SupportsIndex,
    n: SupportsIndex,
    format: Literal["bsr"],
) -> bsr_matrix[Any, Any]: ...
@overload
def spdiags(
    data: npt.NDArray[_SCT_co],
    diags: _ArrayLike1DIndex | SupportsIndex,
    m: None | tuple[SupportsIndex, SupportsIndex],
    n: None,
    format: Literal["dia"],
) -> dia_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def spdiags(
    data: npt.NDArray[_SCT_co],
    diags: _ArrayLike1DIndex | SupportsIndex,
    m: None | tuple[SupportsIndex, SupportsIndex] = ...,
    n: None = ...,
    *,
    format: Literal["dia"],
) -> dia_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def spdiags(
    data: npt.ArrayLike,
    diags: _ArrayLike1DIndex | SupportsIndex,
    m: SupportsIndex,
    n: SupportsIndex,
    format: Literal["dia"],
) -> dia_matrix[Any, Any]: ...
@overload
def spdiags(
    data: npt.NDArray[_SCT_co],
    diags: _ArrayLike1DIndex | SupportsIndex,
    m: None | tuple[SupportsIndex, SupportsIndex],
    n: None,
    format: Literal["dok"],
) -> dok_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def spdiags(
    data: npt.NDArray[_SCT_co],
    diags: _ArrayLike1DIndex | SupportsIndex,
    m: None | tuple[SupportsIndex, SupportsIndex] = ...,
    n: None = ...,
    *,
    format: Literal["dok"],
) -> dok_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def spdiags(
    data: npt.ArrayLike,
    diags: _ArrayLike1DIndex | SupportsIndex,
    m: SupportsIndex,
    n: SupportsIndex,
    format: Literal["dok"],
) -> dok_matrix[Any, Any]: ...
@overload
def spdiags(
    data: npt.NDArray[_SCT_co],
    diags: _ArrayLike1DIndex | SupportsIndex,
    m: None | tuple[SupportsIndex, SupportsIndex],
    n: None,
    format: Literal["lil"],
) -> lil_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def spdiags(
    data: npt.NDArray[_SCT_co],
    diags: _ArrayLike1DIndex | SupportsIndex,
    m: None | tuple[SupportsIndex, SupportsIndex] = ...,
    n: None = ...,
    *,
    format: Literal["lil"],
) -> lil_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def spdiags(
    data: npt.ArrayLike,
    diags: _ArrayLike1DIndex | SupportsIndex,
    m: SupportsIndex,
    n: SupportsIndex,
    format: Literal["lil"],
) -> lil_matrix[Any, Any]: ...
@overload
def diags_array(
    diagonals: npt.NDArray[_SCT_co],
    /,
    *,
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    format: Literal["csc"],
    dtype: None = ...,
) -> csc_array[Any, np.dtype[_SCT_co]]: ...
@overload
def diags_array(
    diagonals: npt.ArrayLike,
    /,
    *,
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    format: Literal["csc"],
    dtype: _DTypeLike[_SCT_co] = ...,
) -> csc_array[Any, np.dtype[_SCT_co]]: ...
@overload
def diags_array(
    diagonals: npt.ArrayLike,
    /,
    *,
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    format: Literal["csc"],
    dtype: npt.DTypeLike | None = ...,
) -> csc_array[Any, Any]: ...
@overload
def diags_array(
    diagonals: npt.NDArray[_SCT_co],
    /,
    *,
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    format: Literal["csr"],
    dtype: None = ...,
) -> csr_array[Any, np.dtype[_SCT_co]]: ...
@overload
def diags_array(
    diagonals: npt.ArrayLike,
    /,
    *,
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    format: Literal["csr"],
    dtype: _DTypeLike[_SCT_co] = ...,
) -> csr_array[Any, np.dtype[_SCT_co]]: ...
@overload
def diags_array(
    diagonals: npt.ArrayLike,
    /,
    *,
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    format: Literal["csr"],
    dtype: npt.DTypeLike | None = ...,
) -> csr_array[Any, Any]: ...
@overload
def diags_array(
    diagonals: npt.NDArray[_SCT_co],
    /,
    *,
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    format: Literal["coo"],
    dtype: None = ...,
) -> coo_array[Any, np.dtype[_SCT_co]]: ...
@overload
def diags_array(
    diagonals: npt.ArrayLike,
    /,
    *,
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    format: Literal["coo"],
    dtype: _DTypeLike[_SCT_co] = ...,
) -> coo_array[Any, np.dtype[_SCT_co]]: ...
@overload
def diags_array(
    diagonals: npt.ArrayLike,
    /,
    *,
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    format: Literal["coo"],
    dtype: npt.DTypeLike | None = ...,
) -> coo_array[Any, Any]: ...
@overload
def diags_array(
    diagonals: npt.NDArray[_SCT_co],
    /,
    *,
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    format: Literal["bsr"],
    dtype: None = ...,
) -> bsr_array[Any, np.dtype[_SCT_co]]: ...
@overload
def diags_array(
    diagonals: npt.ArrayLike,
    /,
    *,
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    format: Literal["bsr"],
    dtype: _DTypeLike[_SCT_co] = ...,
) -> bsr_array[Any, np.dtype[_SCT_co]]: ...
@overload
def diags_array(
    diagonals: npt.ArrayLike,
    /,
    *,
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    format: Literal["bsr"],
    dtype: npt.DTypeLike | None = ...,
) -> bsr_array[Any, Any]: ...
@overload
def diags_array(
    diagonals: npt.NDArray[_SCT_co],
    /,
    *,
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    format: Literal["dia"] | None = ...,
    dtype: None = ...,
) -> dia_array[Any, np.dtype[_SCT_co]]: ...
@overload
def diags_array(
    diagonals: npt.ArrayLike,
    /,
    *,
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    format: Literal["dia"] | None = ...,
    dtype: _DTypeLike[_SCT_co] = ...,
) -> dia_array[Any, np.dtype[_SCT_co]]: ...
@overload
def diags_array(
    diagonals: npt.ArrayLike,
    /,
    *,
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    format: Literal["dia"] | None = ...,
    dtype: npt.DTypeLike | None = ...,
) -> dia_array[Any, Any]: ...
@overload
def diags_array(
    diagonals: npt.NDArray[_SCT_co],
    /,
    *,
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    format: Literal["dok"],
    dtype: None = ...,
) -> dok_array[Any, np.dtype[_SCT_co]]: ...
@overload
def diags_array(
    diagonals: npt.ArrayLike,
    /,
    *,
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    format: Literal["dok"],
    dtype: _DTypeLike[_SCT_co] = ...,
) -> dok_array[Any, np.dtype[_SCT_co]]: ...
@overload
def diags_array(
    diagonals: npt.ArrayLike,
    /,
    *,
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    format: Literal["dok"],
    dtype: npt.DTypeLike | None = ...,
) -> dok_array[Any, Any]: ...
@overload
def diags_array(
    diagonals: npt.NDArray[_SCT_co],
    /,
    *,
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    format: Literal["lil"],
    dtype: None = ...,
) -> lil_array[Any, np.dtype[_SCT_co]]: ...
@overload
def diags_array(
    diagonals: npt.ArrayLike,
    /,
    *,
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    format: Literal["lil"],
    dtype: _DTypeLike[_SCT_co] = ...,
) -> lil_array[Any, np.dtype[_SCT_co]]: ...
@overload
def diags_array(
    diagonals: npt.ArrayLike,
    /,
    *,
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    format: Literal["lil"],
    dtype: npt.DTypeLike | None = ...,
) -> lil_array[Any, Any]: ...
@overload
def diags(
    diagonals: npt.NDArray[_SCT_co],
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    format: None = ...,
    dtype: None = ...,
) -> spmatrix[Any, np.dtype[_SCT_co]]: ...
@overload
def diags(
    diagonals: npt.ArrayLike,
    offsets: _ArrayLike1DIndex | SupportsIndex,
    shape: None | tuple[SupportsIndex, SupportsIndex],
    format: None,
    dtype: _DTypeLike[_SCT_co],
) -> spmatrix[Any, np.dtype[_SCT_co]]: ...
@overload
def diags(
    diagonals: npt.ArrayLike,
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    format: None = ...,
    *,
    dtype: _DTypeLike[_SCT_co],
) -> spmatrix[Any, np.dtype[_SCT_co]]: ...
@overload
def diags(
    diagonals: npt.ArrayLike,
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    format: None = ...,
    dtype: npt.DTypeLike | None = ...,
) -> spmatrix[Any, Any]: ...
@overload
def diags(
    diagonals: npt.NDArray[_SCT_co],
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    *,
    format: Literal["csc"],
    dtype: None = ...,
) -> csc_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def diags(
    diagonals: npt.NDArray[_SCT_co],
    offsets: _ArrayLike1DIndex | SupportsIndex,
    shape: None | tuple[SupportsIndex, SupportsIndex],
    format: Literal["csc"],
    dtype: None = ...,
) -> csc_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def diags(
    diagonals: npt.ArrayLike,
    offsets: _ArrayLike1DIndex | SupportsIndex,
    shape: None | tuple[SupportsIndex, SupportsIndex],
    format: Literal["csc"],
    dtype: _DTypeLike[_SCT_co] = ...,
) -> csc_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def diags(
    diagonals: npt.ArrayLike,
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    *,
    format: Literal["csc"],
    dtype: _DTypeLike[_SCT_co] = ...,
) -> csc_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def diags(
    diagonals: npt.ArrayLike,
    offsets: _ArrayLike1DIndex | SupportsIndex,
    shape: None | tuple[SupportsIndex, SupportsIndex],
    format: Literal["csc"],
    dtype: npt.DTypeLike | None = ...,
) -> csc_matrix[Any, Any]: ...
@overload
def diags(
    diagonals: npt.ArrayLike,
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    *,
    format: Literal["csc"],
    dtype: npt.DTypeLike | None = ...,
) -> csc_matrix[Any, Any]: ...
@overload
def diags(
    diagonals: npt.NDArray[_SCT_co],
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    *,
    format: Literal["csr"],
    dtype: None = ...,
) -> csr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def diags(
    diagonals: npt.NDArray[_SCT_co],
    offsets: _ArrayLike1DIndex | SupportsIndex,
    shape: None | tuple[SupportsIndex, SupportsIndex],
    format: Literal["csr"],
    dtype: None = ...,
) -> csr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def diags(
    diagonals: npt.ArrayLike,
    offsets: _ArrayLike1DIndex | SupportsIndex,
    shape: None | tuple[SupportsIndex, SupportsIndex],
    format: Literal["csr"],
    dtype: _DTypeLike[_SCT_co] = ...,
) -> csr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def diags(
    diagonals: npt.ArrayLike,
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    *,
    format: Literal["csr"],
    dtype: _DTypeLike[_SCT_co] = ...,
) -> csr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def diags(
    diagonals: npt.ArrayLike,
    offsets: _ArrayLike1DIndex | SupportsIndex,
    shape: None | tuple[SupportsIndex, SupportsIndex],
    format: Literal["csr"],
    dtype: npt.DTypeLike | None = ...,
) -> csr_matrix[Any, Any]: ...
@overload
def diags(
    diagonals: npt.ArrayLike,
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    *,
    format: Literal["csr"],
    dtype: npt.DTypeLike | None = ...,
) -> csr_matrix[Any, Any]: ...
@overload
def diags(
    diagonals: npt.NDArray[_SCT_co],
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    *,
    format: Literal["coo"],
    dtype: None = ...,
) -> coo_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def diags(
    diagonals: npt.NDArray[_SCT_co],
    offsets: _ArrayLike1DIndex | SupportsIndex,
    shape: None | tuple[SupportsIndex, SupportsIndex],
    format: Literal["coo"],
    dtype: None = ...,
) -> coo_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def diags(
    diagonals: npt.ArrayLike,
    offsets: _ArrayLike1DIndex | SupportsIndex,
    shape: None | tuple[SupportsIndex, SupportsIndex],
    format: Literal["coo"],
    dtype: _DTypeLike[_SCT_co] = ...,
) -> coo_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def diags(
    diagonals: npt.ArrayLike,
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    *,
    format: Literal["coo"],
    dtype: _DTypeLike[_SCT_co] = ...,
) -> coo_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def diags(
    diagonals: npt.ArrayLike,
    offsets: _ArrayLike1DIndex | SupportsIndex,
    shape: None | tuple[SupportsIndex, SupportsIndex],
    format: Literal["coo"],
    dtype: npt.DTypeLike | None = ...,
) -> coo_matrix[Any, Any]: ...
@overload
def diags(
    diagonals: npt.ArrayLike,
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    *,
    format: Literal["coo"],
    dtype: npt.DTypeLike | None = ...,
) -> coo_matrix[Any, Any]: ...
@overload
def diags(
    diagonals: npt.NDArray[_SCT_co],
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    *,
    format: Literal["bsr"],
    dtype: None = ...,
) -> bsr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def diags(
    diagonals: npt.NDArray[_SCT_co],
    offsets: _ArrayLike1DIndex | SupportsIndex,
    shape: None | tuple[SupportsIndex, SupportsIndex],
    format: Literal["bsr"],
    dtype: None = ...,
) -> bsr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def diags(
    diagonals: npt.ArrayLike,
    offsets: _ArrayLike1DIndex | SupportsIndex,
    shape: None | tuple[SupportsIndex, SupportsIndex],
    format: Literal["bsr"],
    dtype: _DTypeLike[_SCT_co] = ...,
) -> bsr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def diags(
    diagonals: npt.ArrayLike,
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    *,
    format: Literal["bsr"],
    dtype: _DTypeLike[_SCT_co] = ...,
) -> bsr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def diags(
    diagonals: npt.ArrayLike,
    offsets: _ArrayLike1DIndex | SupportsIndex,
    shape: None | tuple[SupportsIndex, SupportsIndex],
    format: Literal["bsr"],
    dtype: npt.DTypeLike | None = ...,
) -> bsr_matrix[Any, Any]: ...
@overload
def diags(
    diagonals: npt.ArrayLike,
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    *,
    format: Literal["bsr"],
    dtype: npt.DTypeLike | None = ...,
) -> bsr_matrix[Any, Any]: ...
@overload
def diags(
    diagonals: npt.NDArray[_SCT_co],
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    *,
    format: Literal["dia"],
    dtype: None = ...,
) -> dia_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def diags(
    diagonals: npt.NDArray[_SCT_co],
    offsets: _ArrayLike1DIndex | SupportsIndex,
    shape: None | tuple[SupportsIndex, SupportsIndex],
    format: Literal["dia"],
    dtype: None = ...,
) -> dia_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def diags(
    diagonals: npt.ArrayLike,
    offsets: _ArrayLike1DIndex | SupportsIndex,
    shape: None | tuple[SupportsIndex, SupportsIndex],
    format: Literal["dia"],
    dtype: _DTypeLike[_SCT_co] = ...,
) -> dia_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def diags(
    diagonals: npt.ArrayLike,
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    *,
    format: Literal["dia"],
    dtype: _DTypeLike[_SCT_co] = ...,
) -> dia_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def diags(
    diagonals: npt.ArrayLike,
    offsets: _ArrayLike1DIndex | SupportsIndex,
    shape: None | tuple[SupportsIndex, SupportsIndex],
    format: Literal["dia"],
    dtype: npt.DTypeLike | None = ...,
) -> dia_matrix[Any, Any]: ...
@overload
def diags(
    diagonals: npt.ArrayLike,
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    *,
    format: Literal["dia"],
    dtype: npt.DTypeLike | None = ...,
) -> dia_matrix[Any, Any]: ...
@overload
def diags(
    diagonals: npt.NDArray[_SCT_co],
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    *,
    format: Literal["dok"],
    dtype: None = ...,
) -> dok_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def diags(
    diagonals: npt.NDArray[_SCT_co],
    offsets: _ArrayLike1DIndex | SupportsIndex,
    shape: None | tuple[SupportsIndex, SupportsIndex],
    format: Literal["dok"],
    dtype: None = ...,
) -> dok_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def diags(
    diagonals: npt.ArrayLike,
    offsets: _ArrayLike1DIndex | SupportsIndex,
    shape: None | tuple[SupportsIndex, SupportsIndex],
    format: Literal["dok"],
    dtype: _DTypeLike[_SCT_co] = ...,
) -> dok_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def diags(
    diagonals: npt.ArrayLike,
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    *,
    format: Literal["dok"],
    dtype: _DTypeLike[_SCT_co] = ...,
) -> dok_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def diags(
    diagonals: npt.ArrayLike,
    offsets: _ArrayLike1DIndex | SupportsIndex,
    shape: None | tuple[SupportsIndex, SupportsIndex],
    format: Literal["dok"],
    dtype: npt.DTypeLike | None = ...,
) -> dok_matrix[Any, Any]: ...
@overload
def diags(
    diagonals: npt.ArrayLike,
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    *,
    format: Literal["dok"],
    dtype: npt.DTypeLike | None = ...,
) -> dok_matrix[Any, Any]: ...
@overload
def diags(
    diagonals: npt.NDArray[_SCT_co],
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    *,
    format: Literal["lil"],
    dtype: None = ...,
) -> lil_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def diags(
    diagonals: npt.NDArray[_SCT_co],
    offsets: _ArrayLike1DIndex | SupportsIndex,
    shape: None | tuple[SupportsIndex, SupportsIndex],
    format: Literal["lil"],
    dtype: None = ...,
) -> lil_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def diags(
    diagonals: npt.ArrayLike,
    offsets: _ArrayLike1DIndex | SupportsIndex,
    shape: None | tuple[SupportsIndex, SupportsIndex],
    format: Literal["lil"],
    dtype: _DTypeLike[_SCT_co] = ...,
) -> lil_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def diags(
    diagonals: npt.ArrayLike,
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    *,
    format: Literal["lil"],
    dtype: _DTypeLike[_SCT_co] = ...,
) -> lil_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def diags(
    diagonals: npt.ArrayLike,
    offsets: _ArrayLike1DIndex | SupportsIndex,
    shape: None | tuple[SupportsIndex, SupportsIndex],
    format: Literal["lil"],
    dtype: npt.DTypeLike | None = ...,
) -> lil_matrix[Any, Any]: ...
@overload
def diags(
    diagonals: npt.ArrayLike,
    offsets: _ArrayLike1DIndex | SupportsIndex = ...,
    shape: None | tuple[SupportsIndex, SupportsIndex] = ...,
    *,
    format: Literal["lil"],
    dtype: npt.DTypeLike | None = ...,
) -> lil_matrix[Any, Any]: ...
@overload
def identity(
    n: SupportsIndex,
    dtype: _DTypeLike[_SCT_co],
    format: None = ...,
) -> dia_array[Any, np.dtype[_SCT_co]]: ...
@overload
def identity(
    n: SupportsIndex,
    dtype: npt.DTypeLike = ...,
    format: None = ...,
) -> dia_array[Any, Any]: ...
@overload
def identity(
    n: SupportsIndex,
    dtype: _DTypeLike[_SCT_co],
    format: Literal["csc"],
) -> csc_array[Any, np.dtype[_SCT_co]]: ...
@overload
def identity(
    n: SupportsIndex,
    dtype: npt.DTypeLike,
    format: Literal["csc"],
) -> csc_array[Any, Any]: ...
@overload
def identity(
    n: SupportsIndex,
    dtype: npt.DTypeLike = ...,
    *,
    format: Literal["csc"],
) -> csc_array[Any, Any]: ...
@overload
def identity(
    n: SupportsIndex,
    dtype: _DTypeLike[_SCT_co],
    format: Literal["csr"],
) -> csr_array[Any, np.dtype[_SCT_co]]: ...
@overload
def identity(
    n: SupportsIndex,
    dtype: npt.DTypeLike,
    format: Literal["csr"],
) -> csr_array[Any, Any]: ...
@overload
def identity(
    n: SupportsIndex,
    dtype: npt.DTypeLike = ...,
    *,
    format: Literal["csr"],
) -> csr_array[Any, Any]: ...
@overload
def identity(
    n: SupportsIndex,
    dtype: _DTypeLike[_SCT_co],
    format: Literal["coo"],
) -> coo_array[Any, np.dtype[_SCT_co]]: ...
@overload
def identity(
    n: SupportsIndex,
    dtype: npt.DTypeLike,
    format: Literal["coo"],
) -> coo_array[Any, Any]: ...
@overload
def identity(
    n: SupportsIndex,
    dtype: npt.DTypeLike = ...,
    *,
    format: Literal["coo"],
) -> coo_array[Any, Any]: ...
@overload
def identity(
    n: SupportsIndex,
    dtype: _DTypeLike[_SCT_co],
    format: Literal["bsr"],
) -> bsr_array[Any, np.dtype[_SCT_co]]: ...
@overload
def identity(
    n: SupportsIndex,
    dtype: npt.DTypeLike,
    format: Literal["bsr"],
) -> bsr_array[Any, Any]: ...
@overload
def identity(
    n: SupportsIndex,
    dtype: npt.DTypeLike = ...,
    *,
    format: Literal["bsr"],
) -> bsr_array[Any, Any]: ...
@overload
def identity(
    n: SupportsIndex,
    dtype: _DTypeLike[_SCT_co],
    format: Literal["dia"],
) -> dia_array[Any, np.dtype[_SCT_co]]: ...
@overload
def identity(
    n: SupportsIndex,
    dtype: npt.DTypeLike,
    format: Literal["dia"],
) -> dia_array[Any, Any]: ...
@overload
def identity(
    n: SupportsIndex,
    dtype: npt.DTypeLike = ...,
    *,
    format: Literal["dia"],
) -> dia_array[Any, Any]: ...
@overload
def identity(
    n: SupportsIndex,
    dtype: _DTypeLike[_SCT_co],
    format: Literal["dok"],
) -> dok_array[Any, np.dtype[_SCT_co]]: ...
@overload
def identity(
    n: SupportsIndex,
    dtype: npt.DTypeLike,
    format: Literal["dok"],
) -> dok_array[Any, Any]: ...
@overload
def identity(
    n: SupportsIndex,
    dtype: npt.DTypeLike = ...,
    *,
    format: Literal["dok"],
) -> dok_array[Any, Any]: ...
@overload
def identity(
    n: SupportsIndex,
    dtype: _DTypeLike[_SCT_co],
    format: Literal["lil"],
) -> lil_array[Any, np.dtype[_SCT_co]]: ...
@overload
def identity(
    n: SupportsIndex,
    dtype: npt.DTypeLike,
    format: Literal["lil"],
) -> lil_array[Any, Any]: ...
@overload
def identity(
    n: SupportsIndex,
    dtype: npt.DTypeLike = ...,
    *,
    format: Literal["lil"],
) -> lil_array[Any, Any]: ...
@overload
def eye_array(
    m: SupportsIndex,
    n: SupportsIndex | None = ...,
    *,
    dtype: _DTypeLike[_SCT_co],
    k: SupportsIndex = ...,
    format: Literal["csc"],
) -> csc_array[Any, np.dtype[_SCT_co]]: ...
@overload
def eye_array(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None = ...,
    *,
    dtype: _DTypeLike[_SCT_co],
    k: SupportsIndex = ...,
    format: Literal["csc"],
) -> csc_array[Any, np.dtype[_SCT_co]]: ...
@overload
def eye_array(
    m: SupportsIndex,
    n: SupportsIndex | None = ...,
    *,
    k: SupportsIndex = ...,
    dtype: npt.DTypeLike = ...,
    format: Literal["csc"],
) -> csc_array[Any, Any]: ...
@overload
def eye_array(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None = ...,
    *,
    k: SupportsIndex = ...,
    dtype: npt.DTypeLike = ...,
    format: Literal["csc"],
) -> csc_array[Any, Any]: ...
@overload
def eye_array(
    m: SupportsIndex,
    n: SupportsIndex | None = ...,
    *,
    dtype: _DTypeLike[_SCT_co],
    k: SupportsIndex = ...,
    format: Literal["csr"],
) -> csr_array[Any, np.dtype[_SCT_co]]: ...
@overload
def eye_array(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None = ...,
    *,
    dtype: _DTypeLike[_SCT_co],
    k: SupportsIndex = ...,
    format: Literal["csr"],
) -> csr_array[Any, np.dtype[_SCT_co]]: ...
@overload
def eye_array(
    m: SupportsIndex,
    n: SupportsIndex | None = ...,
    *,
    k: SupportsIndex = ...,
    dtype: npt.DTypeLike = ...,
    format: Literal["csr"],
) -> csr_array[Any, Any]: ...
@overload
def eye_array(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None = ...,
    *,
    k: SupportsIndex = ...,
    dtype: npt.DTypeLike = ...,
    format: Literal["csr"],
) -> csr_array[Any, Any]: ...
@overload
def eye_array(
    m: SupportsIndex,
    n: SupportsIndex | None = ...,
    *,
    dtype: _DTypeLike[_SCT_co],
    k: SupportsIndex = ...,
    format: Literal["coo"],
) -> coo_array[Any, np.dtype[_SCT_co]]: ...
@overload
def eye_array(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None = ...,
    *,
    dtype: _DTypeLike[_SCT_co],
    k: SupportsIndex = ...,
    format: Literal["coo"],
) -> coo_array[Any, np.dtype[_SCT_co]]: ...
@overload
def eye_array(
    m: SupportsIndex,
    n: SupportsIndex | None = ...,
    *,
    k: SupportsIndex = ...,
    dtype: npt.DTypeLike = ...,
    format: Literal["coo"],
) -> coo_array[Any, Any]: ...
@overload
def eye_array(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None = ...,
    *,
    k: SupportsIndex = ...,
    dtype: npt.DTypeLike = ...,
    format: Literal["coo"],
) -> coo_array[Any, Any]: ...
@overload
def eye_array(
    m: SupportsIndex,
    n: SupportsIndex | None = ...,
    *,
    dtype: _DTypeLike[_SCT_co],
    k: SupportsIndex = ...,
    format: Literal["bsr"],
) -> bsr_array[Any, np.dtype[_SCT_co]]: ...
@overload
def eye_array(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None = ...,
    *,
    dtype: _DTypeLike[_SCT_co],
    k: SupportsIndex = ...,
    format: Literal["bsr"],
) -> bsr_array[Any, np.dtype[_SCT_co]]: ...
@overload
def eye_array(
    m: SupportsIndex,
    n: SupportsIndex | None = ...,
    *,
    k: SupportsIndex = ...,
    dtype: npt.DTypeLike = ...,
    format: Literal["bsr"],
) -> bsr_array[Any, Any]: ...
@overload
def eye_array(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None = ...,
    *,
    k: SupportsIndex = ...,
    dtype: npt.DTypeLike = ...,
    format: Literal["bsr"],
) -> bsr_array[Any, Any]: ...
@overload
def eye_array(
    m: SupportsIndex,
    n: SupportsIndex | None = ...,
    *,
    dtype: _DTypeLike[_SCT_co],
    k: SupportsIndex = ...,
    format: Literal["dia"] | None = ...,
) -> dia_array[Any, np.dtype[_SCT_co]]: ...
@overload
def eye_array(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None = ...,
    *,
    dtype: _DTypeLike[_SCT_co],
    k: SupportsIndex = ...,
    format: Literal["dia"] | None = ...,
) -> dia_array[Any, np.dtype[_SCT_co]]: ...
@overload
def eye_array(
    m: SupportsIndex,
    n: SupportsIndex | None = ...,
    *,
    k: SupportsIndex = ...,
    dtype: npt.DTypeLike = ...,
    format: Literal["dia"] | None = ...,
) -> dia_array[Any, Any]: ...
@overload
def eye_array(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None = ...,
    *,
    k: SupportsIndex = ...,
    dtype: npt.DTypeLike = ...,
    format: Literal["dia"] | None = ...,
) -> dia_array[Any, Any]: ...
@overload
def eye_array(
    m: SupportsIndex,
    n: SupportsIndex | None = ...,
    *,
    dtype: _DTypeLike[_SCT_co],
    k: SupportsIndex = ...,
    format: Literal["dok"],
) -> dok_array[Any, np.dtype[_SCT_co]]: ...
@overload
def eye_array(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None = ...,
    *,
    dtype: _DTypeLike[_SCT_co],
    k: SupportsIndex = ...,
    format: Literal["dok"],
) -> dok_array[Any, np.dtype[_SCT_co]]: ...
@overload
def eye_array(
    m: SupportsIndex,
    n: SupportsIndex | None = ...,
    *,
    k: SupportsIndex = ...,
    dtype: npt.DTypeLike = ...,
    format: Literal["dok"],
) -> dok_array[Any, Any]: ...
@overload
def eye_array(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None = ...,
    *,
    k: SupportsIndex = ...,
    dtype: npt.DTypeLike = ...,
    format: Literal["dok"],
) -> dok_array[Any, Any]: ...
@overload
def eye_array(
    m: SupportsIndex,
    n: SupportsIndex | None = ...,
    *,
    dtype: _DTypeLike[_SCT_co],
    k: SupportsIndex = ...,
    format: Literal["lil"],
) -> lil_array[Any, np.dtype[_SCT_co]]: ...
@overload
def eye_array(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None = ...,
    *,
    dtype: _DTypeLike[_SCT_co],
    k: SupportsIndex = ...,
    format: Literal["lil"],
) -> lil_array[Any, np.dtype[_SCT_co]]: ...
@overload
def eye_array(
    m: SupportsIndex,
    n: SupportsIndex | None = ...,
    *,
    k: SupportsIndex = ...,
    dtype: npt.DTypeLike = ...,
    format: Literal["lil"],
) -> lil_array[Any, Any]: ...
@overload
def eye_array(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None = ...,
    *,
    k: SupportsIndex = ...,
    dtype: npt.DTypeLike = ...,
    format: Literal["lil"],
) -> lil_array[Any, Any]: ...
@overload
def eye(
    m: SupportsIndex,
    n: SupportsIndex | None,
    k: SupportsIndex,
    dtype: _DTypeLike[_SCT_co],
    format: None = ...,
) -> spmatrix[Any, np.dtype[_SCT_co]]: ...
@overload
def eye(
    m: SupportsIndex,
    n: SupportsIndex | None = ...,
    k: SupportsIndex = ...,
    *,
    dtype: _DTypeLike[_SCT_co],
    format: None = ...,
) -> spmatrix[Any, np.dtype[_SCT_co]]: ...
@overload
def eye(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None,
    k: SupportsIndex,
    dtype: _DTypeLike[_SCT_co],
    format: None = ...,
) -> spmatrix[Any, np.dtype[_SCT_co]]: ...
@overload
def eye(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None = ...,
    k: SupportsIndex = ...,
    *,
    dtype: _DTypeLike[_SCT_co],
    format: None = ...,
) -> spmatrix[Any, np.dtype[_SCT_co]]: ...
@overload
def eye(
    m: SupportsIndex,
    n: SupportsIndex | None = ...,
    k: SupportsIndex = ...,
    dtype: npt.DTypeLike = ...,
    format: None = ...,
) -> spmatrix[Any, Any]: ...
@overload
def eye(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None = ...,
    k: SupportsIndex = ...,
    dtype: npt.DTypeLike = ...,
    format: None = ...,
) -> spmatrix[Any, Any]: ...
@overload
def eye(
    m: SupportsIndex,
    n: SupportsIndex | None,
    k: SupportsIndex,
    dtype: _DTypeLike[_SCT_co],
    format: Literal["csc"],
) -> csc_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def eye(
    m: SupportsIndex,
    n: SupportsIndex | None = ...,
    k: SupportsIndex = ...,
    *,
    dtype: _DTypeLike[_SCT_co],
    format: Literal["csc"],
) -> csc_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def eye(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None,
    k: SupportsIndex,
    dtype: _DTypeLike[_SCT_co],
    format: Literal["csc"],
) -> csc_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def eye(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None = ...,
    k: SupportsIndex = ...,
    *,
    dtype: _DTypeLike[_SCT_co],
    format: Literal["csc"],
) -> csc_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def eye(
    m: SupportsIndex,
    n: SupportsIndex | None,
    k: SupportsIndex,
    dtype: npt.DTypeLike,
    format: Literal["csc"],
) -> csc_matrix[Any, Any]: ...
@overload
def eye(
    m: SupportsIndex,
    n: SupportsIndex | None = ...,
    k: SupportsIndex = ...,
    dtype: npt.DTypeLike = ...,
    *,
    format: Literal["csc"],
) -> csc_matrix[Any, Any]: ...
@overload
def eye(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None,
    k: SupportsIndex,
    dtype: npt.DTypeLike,
    format: Literal["csc"],
) -> csc_matrix[Any, Any]: ...
@overload
def eye(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None = ...,
    k: SupportsIndex = ...,
    dtype: npt.DTypeLike = ...,
    *,
    format: Literal["csc"],
) -> csc_matrix[Any, Any]: ...
@overload
def eye(
    m: SupportsIndex,
    n: SupportsIndex | None,
    k: SupportsIndex,
    dtype: _DTypeLike[_SCT_co],
    format: Literal["csr"],
) -> csr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def eye(
    m: SupportsIndex,
    n: SupportsIndex | None = ...,
    k: SupportsIndex = ...,
    *,
    dtype: _DTypeLike[_SCT_co],
    format: Literal["csr"],
) -> csr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def eye(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None,
    k: SupportsIndex,
    dtype: _DTypeLike[_SCT_co],
    format: Literal["csr"],
) -> csr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def eye(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None = ...,
    k: SupportsIndex = ...,
    *,
    dtype: _DTypeLike[_SCT_co],
    format: Literal["csr"],
) -> csr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def eye(
    m: SupportsIndex,
    n: SupportsIndex | None,
    k: SupportsIndex,
    dtype: npt.DTypeLike,
    format: Literal["csr"],
) -> csr_matrix[Any, Any]: ...
@overload
def eye(
    m: SupportsIndex,
    n: SupportsIndex | None = ...,
    k: SupportsIndex = ...,
    dtype: npt.DTypeLike = ...,
    *,
    format: Literal["csr"],
) -> csr_matrix[Any, Any]: ...
@overload
def eye(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None,
    k: SupportsIndex,
    dtype: npt.DTypeLike,
    format: Literal["csr"],
) -> csr_matrix[Any, Any]: ...
@overload
def eye(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None = ...,
    k: SupportsIndex = ...,
    dtype: npt.DTypeLike = ...,
    *,
    format: Literal["csr"],
) -> csr_matrix[Any, Any]: ...
@overload
def eye(
    m: SupportsIndex,
    n: SupportsIndex | None,
    k: SupportsIndex,
    dtype: _DTypeLike[_SCT_co],
    format: Literal["coo"],
) -> coo_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def eye(
    m: SupportsIndex,
    n: SupportsIndex | None = ...,
    k: SupportsIndex = ...,
    *,
    dtype: _DTypeLike[_SCT_co],
    format: Literal["coo"],
) -> coo_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def eye(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None,
    k: SupportsIndex,
    dtype: _DTypeLike[_SCT_co],
    format: Literal["coo"],
) -> coo_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def eye(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None = ...,
    k: SupportsIndex = ...,
    *,
    dtype: _DTypeLike[_SCT_co],
    format: Literal["coo"],
) -> coo_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def eye(
    m: SupportsIndex,
    n: SupportsIndex | None,
    k: SupportsIndex,
    dtype: npt.DTypeLike,
    format: Literal["coo"],
) -> coo_matrix[Any, Any]: ...
@overload
def eye(
    m: SupportsIndex,
    n: SupportsIndex | None = ...,
    k: SupportsIndex = ...,
    dtype: npt.DTypeLike = ...,
    *,
    format: Literal["coo"],
) -> coo_matrix[Any, Any]: ...
@overload
def eye(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None,
    k: SupportsIndex,
    dtype: npt.DTypeLike,
    format: Literal["coo"],
) -> coo_matrix[Any, Any]: ...
@overload
def eye(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None = ...,
    k: SupportsIndex = ...,
    dtype: npt.DTypeLike = ...,
    *,
    format: Literal["coo"],
) -> coo_matrix[Any, Any]: ...
@overload
def eye(
    m: SupportsIndex,
    n: SupportsIndex | None,
    k: SupportsIndex,
    dtype: _DTypeLike[_SCT_co],
    format: Literal["bsr"],
) -> bsr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def eye(
    m: SupportsIndex,
    n: SupportsIndex | None = ...,
    k: SupportsIndex = ...,
    *,
    dtype: _DTypeLike[_SCT_co],
    format: Literal["bsr"],
) -> bsr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def eye(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None,
    k: SupportsIndex,
    dtype: _DTypeLike[_SCT_co],
    format: Literal["bsr"],
) -> bsr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def eye(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None = ...,
    k: SupportsIndex = ...,
    *,
    dtype: _DTypeLike[_SCT_co],
    format: Literal["bsr"],
) -> bsr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def eye(
    m: SupportsIndex,
    n: SupportsIndex | None,
    k: SupportsIndex,
    dtype: npt.DTypeLike,
    format: Literal["bsr"],
) -> bsr_matrix[Any, Any]: ...
@overload
def eye(
    m: SupportsIndex,
    n: SupportsIndex | None = ...,
    k: SupportsIndex = ...,
    dtype: npt.DTypeLike = ...,
    *,
    format: Literal["bsr"],
) -> bsr_matrix[Any, Any]: ...
@overload
def eye(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None,
    k: SupportsIndex,
    dtype: npt.DTypeLike,
    format: Literal["bsr"],
) -> bsr_matrix[Any, Any]: ...
@overload
def eye(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None = ...,
    k: SupportsIndex = ...,
    dtype: npt.DTypeLike = ...,
    *,
    format: Literal["bsr"],
) -> bsr_matrix[Any, Any]: ...
@overload
def eye(
    m: SupportsIndex,
    n: SupportsIndex | None,
    k: SupportsIndex,
    dtype: _DTypeLike[_SCT_co],
    format: Literal["dia"],
) -> dia_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def eye(
    m: SupportsIndex,
    n: SupportsIndex | None = ...,
    k: SupportsIndex = ...,
    *,
    dtype: _DTypeLike[_SCT_co],
    format: Literal["dia"],
) -> dia_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def eye(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None,
    k: SupportsIndex,
    dtype: _DTypeLike[_SCT_co],
    format: Literal["dia"],
) -> dia_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def eye(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None = ...,
    k: SupportsIndex = ...,
    *,
    dtype: _DTypeLike[_SCT_co],
    format: Literal["dia"],
) -> dia_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def eye(
    m: SupportsIndex,
    n: SupportsIndex | None,
    k: SupportsIndex,
    dtype: npt.DTypeLike,
    format: Literal["dia"],
) -> dia_matrix[Any, Any]: ...
@overload
def eye(
    m: SupportsIndex,
    n: SupportsIndex | None = ...,
    k: SupportsIndex = ...,
    dtype: npt.DTypeLike = ...,
    *,
    format: Literal["dia"],
) -> dia_matrix[Any, Any]: ...
@overload
def eye(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None,
    k: SupportsIndex,
    dtype: npt.DTypeLike,
    format: Literal["dia"],
) -> dia_matrix[Any, Any]: ...
@overload
def eye(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None = ...,
    k: SupportsIndex = ...,
    dtype: npt.DTypeLike = ...,
    *,
    format: Literal["dia"],
) -> dia_matrix[Any, Any]: ...
@overload
def eye(
    m: SupportsIndex,
    n: SupportsIndex | None,
    k: SupportsIndex,
    dtype: _DTypeLike[_SCT_co],
    format: Literal["dok"],
) -> dok_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def eye(
    m: SupportsIndex,
    n: SupportsIndex | None = ...,
    k: SupportsIndex = ...,
    *,
    dtype: _DTypeLike[_SCT_co],
    format: Literal["dok"],
) -> dok_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def eye(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None,
    k: SupportsIndex,
    dtype: _DTypeLike[_SCT_co],
    format: Literal["dok"],
) -> dok_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def eye(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None = ...,
    k: SupportsIndex = ...,
    *,
    dtype: _DTypeLike[_SCT_co],
    format: Literal["dok"],
) -> dok_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def eye(
    m: SupportsIndex,
    n: SupportsIndex | None,
    k: SupportsIndex,
    dtype: npt.DTypeLike,
    format: Literal["dok"],
) -> dok_matrix[Any, Any]: ...
@overload
def eye(
    m: SupportsIndex,
    n: SupportsIndex | None = ...,
    k: SupportsIndex = ...,
    dtype: npt.DTypeLike = ...,
    *,
    format: Literal["dok"],
) -> dok_matrix[Any, Any]: ...
@overload
def eye(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None,
    k: SupportsIndex,
    dtype: npt.DTypeLike,
    format: Literal["dok"],
) -> dok_matrix[Any, Any]: ...
@overload
def eye(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None = ...,
    k: SupportsIndex = ...,
    dtype: npt.DTypeLike = ...,
    *,
    format: Literal["dok"],
) -> dok_matrix[Any, Any]: ...
@overload
def eye(
    m: SupportsIndex,
    n: SupportsIndex | None,
    k: SupportsIndex,
    dtype: _DTypeLike[_SCT_co],
    format: Literal["lil"],
) -> lil_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def eye(
    m: SupportsIndex,
    n: SupportsIndex | None = ...,
    k: SupportsIndex = ...,
    *,
    dtype: _DTypeLike[_SCT_co],
    format: Literal["lil"],
) -> lil_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def eye(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None,
    k: SupportsIndex,
    dtype: _DTypeLike[_SCT_co],
    format: Literal["lil"],
) -> lil_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def eye(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None = ...,
    k: SupportsIndex = ...,
    *,
    dtype: _DTypeLike[_SCT_co],
    format: Literal["lil"],
) -> lil_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def eye(
    m: SupportsIndex,
    n: SupportsIndex | None,
    k: SupportsIndex,
    dtype: npt.DTypeLike,
    format: Literal["lil"],
) -> lil_matrix[Any, Any]: ...
@overload
def eye(
    m: SupportsIndex,
    n: SupportsIndex | None = ...,
    k: SupportsIndex = ...,
    dtype: npt.DTypeLike = ...,
    *,
    format: Literal["lil"],
) -> lil_matrix[Any, Any]: ...
@overload
def eye(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None,
    k: SupportsIndex,
    dtype: npt.DTypeLike,
    format: Literal["lil"],
) -> lil_matrix[Any, Any]: ...
@overload
def eye(
    m: tuple[SupportsIndex, SupportsIndex],
    n: None = ...,
    k: SupportsIndex = ...,
    dtype: npt.DTypeLike = ...,
    *,
    format: Literal["lil"],
) -> lil_matrix[Any, Any]: ...
@overload
def kron(
    A: sparray[Any, Any],
    B: SparseArray[Any] | npt.ArrayLike,
    format: None = ...,
) -> bsr_array[Any, Any] | coo_array[Any, Any]: ...
@overload
def kron(
    A: SparseArray[Any] | npt.ArrayLike,
    B: sparray[Any, Any],
    format: None = ...,
) -> bsr_array[Any, Any] | coo_array[Any, Any]: ...
@overload
def kron(
    A: sparray[Any, Any],
    B: SparseArray[Any] | npt.ArrayLike,
    format: Literal["csc"],
) -> csc_array[Any, Any]: ...
@overload
def kron(
    A: SparseArray[Any] | npt.ArrayLike,
    B: sparray[Any, Any],
    format: Literal["csc"],
) -> csc_array[Any, Any]: ...
@overload
def kron(
    A: sparray[Any, Any],
    B: SparseArray[Any] | npt.ArrayLike,
    format: Literal["csr"],
) -> csr_array[Any, Any]: ...
@overload
def kron(
    A: SparseArray[Any] | npt.ArrayLike,
    B: sparray[Any, Any],
    format: Literal["csr"],
) -> csr_array[Any, Any]: ...
@overload
def kron(
    A: sparray[Any, Any],
    B: SparseArray[Any] | npt.ArrayLike,
    format: Literal["coo"],
) -> coo_array[Any, Any]: ...
@overload
def kron(
    A: SparseArray[Any] | npt.ArrayLike,
    B: sparray[Any, Any],
    format: Literal["coo"],
) -> coo_array[Any, Any]: ...
@overload
def kron(
    A: sparray[Any, Any],
    B: SparseArray[Any] | npt.ArrayLike,
    format: Literal["bsr"],
) -> bsr_array[Any, Any]: ...
@overload
def kron(
    A: SparseArray[Any] | npt.ArrayLike,
    B: sparray[Any, Any],
    format: Literal["bsr"],
) -> bsr_array[Any, Any]: ...
@overload
def kron(
    A: sparray[Any, Any],
    B: SparseArray[Any] | npt.ArrayLike,
    format: Literal["dia"],
) -> dia_array[Any, Any]: ...
@overload
def kron(
    A: SparseArray[Any] | npt.ArrayLike,
    B: sparray[Any, Any],
    format: Literal["dia"],
) -> dia_array[Any, Any]: ...
@overload
def kron(
    A: sparray[Any, Any],
    B: SparseArray[Any] | npt.ArrayLike,
    format: Literal["dok"],
) -> dok_array[Any, Any]: ...
@overload
def kron(
    A: SparseArray[Any] | npt.ArrayLike,
    B: sparray[Any, Any],
    format: Literal["dok"],
) -> dok_array[Any, Any]: ...
@overload
def kron(
    A: sparray[Any, Any],
    B: SparseArray[Any] | npt.ArrayLike,
    format: Literal["lil"],
) -> lil_array[Any, Any]: ...
@overload
def kron(
    A: SparseArray[Any] | npt.ArrayLike,
    B: sparray[Any, Any],
    format: Literal["lil"],
) -> lil_array[Any, Any]: ...
@overload
def kron(
    A: spmatrix[Any, Any] | npt.ArrayLike,
    B: spmatrix[Any, Any] | npt.ArrayLike,
    format: None = ...,
) -> bsr_matrix[Any, Any] | coo_matrix[Any, Any]: ...
@overload
def kron(
    A: spmatrix[Any, Any] | npt.ArrayLike,
    B: spmatrix[Any, Any] | npt.ArrayLike,
    format: Literal["csc"],
) -> csc_matrix[Any, Any]: ...
@overload
def kron(
    A: spmatrix[Any, Any] | npt.ArrayLike,
    B: spmatrix[Any, Any] | npt.ArrayLike,
    format: Literal["csr"],
) -> csr_matrix[Any, Any]: ...
@overload
def kron(
    A: spmatrix[Any, Any] | npt.ArrayLike,
    B: spmatrix[Any, Any] | npt.ArrayLike,
    format: Literal["coo"],
) -> coo_matrix[Any, Any]: ...
@overload
def kron(
    A: spmatrix[Any, Any] | npt.ArrayLike,
    B: spmatrix[Any, Any] | npt.ArrayLike,
    format: Literal["bsr"],
) -> bsr_matrix[Any, Any]: ...
@overload
def kron(
    A: spmatrix[Any, Any] | npt.ArrayLike,
    B: spmatrix[Any, Any] | npt.ArrayLike,
    format: Literal["dia"],
) -> dia_matrix[Any, Any]: ...
@overload
def kron(
    A: spmatrix[Any, Any] | npt.ArrayLike,
    B: spmatrix[Any, Any] | npt.ArrayLike,
    format: Literal["dok"],
) -> dok_matrix[Any, Any]: ...
@overload
def kron(
    A: spmatrix[Any, Any] | npt.ArrayLike,
    B: spmatrix[Any, Any] | npt.ArrayLike,
    format: Literal["lil"],
) -> lil_matrix[Any, Any]: ...
@overload
def kronsum(
    A: sparray[Any, Any],
    B: SparseArray[Any] | npt.ArrayLike,
    format: None = ...,
) -> coo_array[Any, Any]: ...
@overload
def kronsum(
    A: SparseArray[Any] | npt.ArrayLike,
    B: sparray[Any, Any],
    format: None = ...,
) -> coo_array[Any, Any]: ...
@overload
def kronsum(
    A: sparray[Any, Any],
    B: SparseArray[Any] | npt.ArrayLike,
    format: Literal["csc"],
) -> csc_array[Any, Any]: ...
@overload
def kronsum(
    A: SparseArray[Any] | npt.ArrayLike,
    B: sparray[Any, Any],
    format: Literal["csc"],
) -> csc_array[Any, Any]: ...
@overload
def kronsum(
    A: sparray[Any, Any],
    B: SparseArray[Any] | npt.ArrayLike,
    format: Literal["csr"],
) -> csr_array[Any, Any]: ...
@overload
def kronsum(
    A: SparseArray[Any] | npt.ArrayLike,
    B: sparray[Any, Any],
    format: Literal["csr"],
) -> csr_array[Any, Any]: ...
@overload
def kronsum(
    A: sparray[Any, Any],
    B: SparseArray[Any] | npt.ArrayLike,
    format: Literal["coo"],
) -> coo_array[Any, Any]: ...
@overload
def kronsum(
    A: SparseArray[Any] | npt.ArrayLike,
    B: sparray[Any, Any],
    format: Literal["coo"],
) -> coo_array[Any, Any]: ...
@overload
def kronsum(
    A: sparray[Any, Any],
    B: SparseArray[Any] | npt.ArrayLike,
    format: Literal["bsr"],
) -> bsr_array[Any, Any]: ...
@overload
def kronsum(
    A: SparseArray[Any] | npt.ArrayLike,
    B: sparray[Any, Any],
    format: Literal["bsr"],
) -> bsr_array[Any, Any]: ...
@overload
def kronsum(
    A: sparray[Any, Any],
    B: SparseArray[Any] | npt.ArrayLike,
    format: Literal["dia"],
) -> dia_array[Any, Any]: ...
@overload
def kronsum(
    A: SparseArray[Any] | npt.ArrayLike,
    B: sparray[Any, Any],
    format: Literal["dia"],
) -> dia_array[Any, Any]: ...
@overload
def kronsum(
    A: sparray[Any, Any],
    B: SparseArray[Any] | npt.ArrayLike,
    format: Literal["dok"],
) -> dok_array[Any, Any]: ...
@overload
def kronsum(
    A: SparseArray[Any] | npt.ArrayLike,
    B: sparray[Any, Any],
    format: Literal["dok"],
) -> dok_array[Any, Any]: ...
@overload
def kronsum(
    A: sparray[Any, Any],
    B: SparseArray[Any] | npt.ArrayLike,
    format: Literal["lil"],
) -> lil_array[Any, Any]: ...
@overload
def kronsum(
    A: SparseArray[Any] | npt.ArrayLike,
    B: sparray[Any, Any],
    format: Literal["lil"],
) -> lil_array[Any, Any]: ...
@overload
def kronsum(
    A: spmatrix[Any, Any] | npt.ArrayLike,
    B: spmatrix[Any, Any] | npt.ArrayLike,
    format: None = ...,
) -> coo_matrix[Any, Any]: ...
@overload
def kronsum(
    A: spmatrix[Any, Any] | npt.ArrayLike,
    B: spmatrix[Any, Any] | npt.ArrayLike,
    format: Literal["csc"],
) -> csc_matrix[Any, Any]: ...
@overload
def kronsum(
    A: spmatrix[Any, Any] | npt.ArrayLike,
    B: spmatrix[Any, Any] | npt.ArrayLike,
    format: Literal["csr"],
) -> csr_matrix[Any, Any]: ...
@overload
def kronsum(
    A: spmatrix[Any, Any] | npt.ArrayLike,
    B: spmatrix[Any, Any] | npt.ArrayLike,
    format: Literal["coo"],
) -> coo_matrix[Any, Any]: ...
@overload
def kronsum(
    A: spmatrix[Any, Any] | npt.ArrayLike,
    B: spmatrix[Any, Any] | npt.ArrayLike,
    format: Literal["bsr"],
) -> bsr_matrix[Any, Any]: ...
@overload
def kronsum(
    A: spmatrix[Any, Any] | npt.ArrayLike,
    B: spmatrix[Any, Any] | npt.ArrayLike,
    format: Literal["dia"],
) -> dia_matrix[Any, Any]: ...
@overload
def kronsum(
    A: spmatrix[Any, Any] | npt.ArrayLike,
    B: spmatrix[Any, Any] | npt.ArrayLike,
    format: Literal["dok"],
) -> dok_matrix[Any, Any]: ...
@overload
def kronsum(
    A: spmatrix[Any, Any] | npt.ArrayLike,
    B: spmatrix[Any, Any] | npt.ArrayLike,
    format: Literal["lil"],
) -> lil_matrix[Any, Any]: ...
@overload
def hstack(
    blocks: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: None,
    dtype: _DTypeLike[_SCT_co],
) -> spmatrix[Any, np.dtype[_SCT_co]]: ...
@overload
def hstack(
    blocks: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: None = ...,
    *,
    dtype: _DTypeLike[_SCT_co],
) -> spmatrix[Any, np.dtype[_SCT_co]]: ...
@overload
def hstack(
    blocks: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: None = ...,
    dtype: npt.DTypeLike | None = ...,
) -> spmatrix[Any, Any]: ...
@overload
def hstack(
    blocks: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: None,
    dtype: _DTypeLike[_SCT_co],
) -> SparseArray[_SCT_co]: ...
@overload
def hstack(
    blocks: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: None = ...,
    *,
    dtype: np.dtype[_SCT_co],
) -> SparseArray[_SCT_co]: ...
@overload
def hstack(
    blocks: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: None = ...,
    dtype: npt.DTypeLike | None = ...,
) -> SparseArray[Any]: ...
@overload
def hstack(
    blocks: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: Literal["csc"],
    dtype: _DTypeLike[_SCT_co],
) -> csc_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def hstack(
    blocks: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: Literal["csc"],
    dtype: npt.DTypeLike | None = ...,
) -> csc_matrix[Any, Any]: ...
@overload
def hstack(
    blocks: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: Literal["csc"],
    dtype: _DTypeLike[_SCT_co],
) -> csc_array[Any, np.dtype[_SCT_co]] | csc_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def hstack(
    blocks: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: Literal["csc"],
    dtype: npt.DTypeLike | None = ...,
) -> csc_array[Any, np.dtype[_SCT_co]] | csc_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def hstack(
    blocks: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: Literal["csr"],
    dtype: _DTypeLike[_SCT_co],
) -> csr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def hstack(
    blocks: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: Literal["csr"],
    dtype: npt.DTypeLike | None = ...,
) -> csr_matrix[Any, Any]: ...
@overload
def hstack(
    blocks: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: Literal["csr"],
    dtype: _DTypeLike[_SCT_co],
) -> csr_array[Any, np.dtype[_SCT_co]] | csr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def hstack(
    blocks: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: Literal["csr"],
    dtype: npt.DTypeLike | None = ...,
) -> csr_array[Any, np.dtype[_SCT_co]] | csr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def hstack(
    blocks: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: Literal["coo"],
    dtype: _DTypeLike[_SCT_co],
) -> coo_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def hstack(
    blocks: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: Literal["coo"],
    dtype: npt.DTypeLike | None = ...,
) -> coo_matrix[Any, Any]: ...
@overload
def hstack(
    blocks: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: Literal["coo"],
    dtype: _DTypeLike[_SCT_co],
) -> coo_array[Any, np.dtype[_SCT_co]] | coo_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def hstack(
    blocks: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: Literal["coo"],
    dtype: npt.DTypeLike | None = ...,
) -> coo_array[Any, np.dtype[_SCT_co]] | coo_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def hstack(
    blocks: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: Literal["bsr"],
    dtype: _DTypeLike[_SCT_co],
) -> bsr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def hstack(
    blocks: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: Literal["bsr"],
    dtype: npt.DTypeLike | None = ...,
) -> bsr_matrix[Any, Any]: ...
@overload
def hstack(
    blocks: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: Literal["bsr"],
    dtype: _DTypeLike[_SCT_co],
) -> bsr_array[Any, np.dtype[_SCT_co]] | bsr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def hstack(
    blocks: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: Literal["bsr"],
    dtype: npt.DTypeLike | None = ...,
) -> bsr_array[Any, np.dtype[_SCT_co]] | bsr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def hstack(
    blocks: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: Literal["dia"],
    dtype: _DTypeLike[_SCT_co],
) -> dia_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def hstack(
    blocks: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: Literal["dia"],
    dtype: npt.DTypeLike | None = ...,
) -> dia_matrix[Any, Any]: ...
@overload
def hstack(
    blocks: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: Literal["dia"],
    dtype: _DTypeLike[_SCT_co],
) -> dia_array[Any, np.dtype[_SCT_co]] | dia_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def hstack(
    blocks: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: Literal["dia"],
    dtype: npt.DTypeLike | None = ...,
) -> dia_array[Any, np.dtype[_SCT_co]] | dia_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def hstack(
    blocks: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: Literal["dok"],
    dtype: _DTypeLike[_SCT_co],
) -> dok_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def hstack(
    blocks: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: Literal["dok"],
    dtype: npt.DTypeLike | None = ...,
) -> dok_matrix[Any, Any]: ...
@overload
def hstack(
    blocks: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: Literal["dok"],
    dtype: _DTypeLike[_SCT_co],
) -> dok_array[Any, np.dtype[_SCT_co]] | dok_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def hstack(
    blocks: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: Literal["dok"],
    dtype: npt.DTypeLike | None = ...,
) -> dok_array[Any, np.dtype[_SCT_co]] | dok_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def hstack(
    blocks: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: Literal["lil"],
    dtype: _DTypeLike[_SCT_co],
) -> lil_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def hstack(
    blocks: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: Literal["lil"],
    dtype: npt.DTypeLike | None = ...,
) -> lil_matrix[Any, Any]: ...
@overload
def hstack(
    blocks: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: Literal["lil"],
    dtype: _DTypeLike[_SCT_co],
) -> lil_array[Any, np.dtype[_SCT_co]] | lil_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def hstack(
    blocks: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: Literal["lil"],
    dtype: npt.DTypeLike | None = ...,
) -> lil_array[Any, np.dtype[_SCT_co]] | lil_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def vstack(
    blocks: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: None,
    dtype: _DTypeLike[_SCT_co],
) -> spmatrix[Any, np.dtype[_SCT_co]]: ...
@overload
def vstack(
    blocks: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: None = ...,
    *,
    dtype: _DTypeLike[_SCT_co],
) -> spmatrix[Any, np.dtype[_SCT_co]]: ...
@overload
def vstack(
    blocks: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: None = ...,
    dtype: npt.DTypeLike | None = ...,
) -> spmatrix[Any, Any]: ...
@overload
def vstack(
    blocks: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: None,
    dtype: _DTypeLike[_SCT_co],
) -> SparseArray[_SCT_co]: ...
@overload
def vstack(
    blocks: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: None = ...,
    *,
    dtype: np.dtype[_SCT_co],
) -> SparseArray[_SCT_co]: ...
@overload
def vstack(
    blocks: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: None = ...,
    dtype: npt.DTypeLike | None = ...,
) -> SparseArray[Any]: ...
@overload
def vstack(
    blocks: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: Literal["csc"],
    dtype: _DTypeLike[_SCT_co],
) -> csc_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def vstack(
    blocks: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: Literal["csc"],
    dtype: npt.DTypeLike | None = ...,
) -> csc_matrix[Any, Any]: ...
@overload
def vstack(
    blocks: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: Literal["csc"],
    dtype: _DTypeLike[_SCT_co],
) -> csc_array[Any, np.dtype[_SCT_co]] | csc_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def vstack(
    blocks: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: Literal["csc"],
    dtype: npt.DTypeLike | None = ...,
) -> csc_array[Any, np.dtype[_SCT_co]] | csc_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def vstack(
    blocks: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: Literal["csr"],
    dtype: _DTypeLike[_SCT_co],
) -> csr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def vstack(
    blocks: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: Literal["csr"],
    dtype: npt.DTypeLike | None = ...,
) -> csr_matrix[Any, Any]: ...
@overload
def vstack(
    blocks: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: Literal["csr"],
    dtype: _DTypeLike[_SCT_co],
) -> csr_array[Any, np.dtype[_SCT_co]] | csr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def vstack(
    blocks: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: Literal["csr"],
    dtype: npt.DTypeLike | None = ...,
) -> csr_array[Any, np.dtype[_SCT_co]] | csr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def vstack(
    blocks: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: Literal["coo"],
    dtype: _DTypeLike[_SCT_co],
) -> coo_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def vstack(
    blocks: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: Literal["coo"],
    dtype: npt.DTypeLike | None = ...,
) -> coo_matrix[Any, Any]: ...
@overload
def vstack(
    blocks: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: Literal["coo"],
    dtype: _DTypeLike[_SCT_co],
) -> coo_array[Any, np.dtype[_SCT_co]] | coo_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def vstack(
    blocks: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: Literal["coo"],
    dtype: npt.DTypeLike | None = ...,
) -> coo_array[Any, np.dtype[_SCT_co]] | coo_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def vstack(
    blocks: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: Literal["bsr"],
    dtype: _DTypeLike[_SCT_co],
) -> bsr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def vstack(
    blocks: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: Literal["bsr"],
    dtype: npt.DTypeLike | None = ...,
) -> bsr_matrix[Any, Any]: ...
@overload
def vstack(
    blocks: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: Literal["bsr"],
    dtype: _DTypeLike[_SCT_co],
) -> bsr_array[Any, np.dtype[_SCT_co]] | bsr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def vstack(
    blocks: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: Literal["bsr"],
    dtype: npt.DTypeLike | None = ...,
) -> bsr_array[Any, np.dtype[_SCT_co]] | bsr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def vstack(
    blocks: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: Literal["dia"],
    dtype: _DTypeLike[_SCT_co],
) -> dia_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def vstack(
    blocks: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: Literal["dia"],
    dtype: npt.DTypeLike | None = ...,
) -> dia_matrix[Any, Any]: ...
@overload
def vstack(
    blocks: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: Literal["dia"],
    dtype: _DTypeLike[_SCT_co],
) -> dia_array[Any, np.dtype[_SCT_co]] | dia_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def vstack(
    blocks: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: Literal["dia"],
    dtype: npt.DTypeLike | None = ...,
) -> dia_array[Any, np.dtype[_SCT_co]] | dia_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def vstack(
    blocks: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: Literal["dok"],
    dtype: _DTypeLike[_SCT_co],
) -> dok_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def vstack(
    blocks: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: Literal["dok"],
    dtype: npt.DTypeLike | None = ...,
) -> dok_matrix[Any, Any]: ...
@overload
def vstack(
    blocks: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: Literal["dok"],
    dtype: _DTypeLike[_SCT_co],
) -> dok_array[Any, np.dtype[_SCT_co]] | dok_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def vstack(
    blocks: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: Literal["dok"],
    dtype: npt.DTypeLike | None = ...,
) -> dok_array[Any, np.dtype[_SCT_co]] | dok_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def vstack(
    blocks: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: Literal["lil"],
    dtype: _DTypeLike[_SCT_co],
) -> lil_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def vstack(
    blocks: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: Literal["lil"],
    dtype: npt.DTypeLike | None = ...,
) -> lil_matrix[Any, Any]: ...
@overload
def vstack(
    blocks: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: Literal["lil"],
    dtype: _DTypeLike[_SCT_co],
) -> lil_array[Any, np.dtype[_SCT_co]] | lil_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def vstack(
    blocks: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: Literal["lil"],
    dtype: npt.DTypeLike | None = ...,
) -> lil_array[Any, np.dtype[_SCT_co]] | lil_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def bmat(
    blocks: (
        Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]]
    ),
    format: None,
    dtype: _DTypeLike[_SCT_co],
) -> spmatrix[Any, np.dtype[_SCT_co]]: ...
@overload
def bmat(
    blocks: (
        Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]]
    ),
    format: None = ...,
    *,
    dtype: _DTypeLike[_SCT_co],
) -> spmatrix[Any, np.dtype[_SCT_co]]: ...
@overload
def bmat(
    blocks: (
        Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]]
    ),
    format: None = ...,
    dtype: npt.DTypeLike | None = ...,
) -> spmatrix[Any, Any]: ...
@overload
def bmat(
    blocks: (
        Sequence[SparseArray[Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[SparseArray[Any] | npt.NDArray[Any] | None]]
    ),
    format: None,
    dtype: _DTypeLike[_SCT_co],
) -> SparseArray[_SCT_co]: ...
@overload
def bmat(
    blocks: (
        Sequence[SparseArray[Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[SparseArray[Any] | npt.NDArray[Any] | None]]
    ),
    format: None = ...,
    *,
    dtype: np.dtype[_SCT_co],
) -> SparseArray[_SCT_co]: ...
@overload
def bmat(
    blocks: (
        Sequence[SparseArray[Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[SparseArray[Any] | npt.NDArray[Any] | None]]
    ),
    format: None = ...,
    dtype: npt.DTypeLike | None = ...,
) -> SparseArray[Any]: ...
@overload
def bmat(
    blocks: (
        Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]]
    ),
    format: Literal["csc"],
    dtype: _DTypeLike[_SCT_co],
) -> csc_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def bmat(
    blocks: (
        Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]]
    ),
    format: Literal["csc"],
    dtype: npt.DTypeLike | None = ...,
) -> csc_matrix[Any, Any]: ...
@overload
def bmat(
    blocks: (
        Sequence[SparseArray[Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[SparseArray[Any] | npt.NDArray[Any] | None]]
    ),
    format: Literal["csc"],
    dtype: _DTypeLike[_SCT_co],
) -> csc_array[Any, np.dtype[_SCT_co]] | csc_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def bmat(
    blocks: (
        Sequence[SparseArray[Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[SparseArray[Any] | npt.NDArray[Any] | None]]
    ),
    format: Literal["csc"],
    dtype: npt.DTypeLike | None = ...,
) -> csc_array[Any, np.dtype[_SCT_co]] | csc_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def bmat(
    blocks: (
        Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]]
    ),
    format: Literal["csr"],
    dtype: _DTypeLike[_SCT_co],
) -> csr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def bmat(
    blocks: (
        Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]]
    ),
    format: Literal["csr"],
    dtype: npt.DTypeLike | None = ...,
) -> csr_matrix[Any, Any]: ...
@overload
def bmat(
    blocks: (
        Sequence[SparseArray[Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[SparseArray[Any] | npt.NDArray[Any] | None]]
    ),
    format: Literal["csr"],
    dtype: _DTypeLike[_SCT_co],
) -> csr_array[Any, np.dtype[_SCT_co]] | csr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def bmat(
    blocks: (
        Sequence[SparseArray[Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[SparseArray[Any] | npt.NDArray[Any] | None]]
    ),
    format: Literal["csr"],
    dtype: npt.DTypeLike | None = ...,
) -> csr_array[Any, np.dtype[_SCT_co]] | csr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def bmat(
    blocks: (
        Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]]
    ),
    format: Literal["coo"],
    dtype: _DTypeLike[_SCT_co],
) -> coo_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def bmat(
    blocks: (
        Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]]
    ),
    format: Literal["coo"],
    dtype: npt.DTypeLike | None = ...,
) -> coo_matrix[Any, Any]: ...
@overload
def bmat(
    blocks: (
        Sequence[SparseArray[Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[SparseArray[Any] | npt.NDArray[Any] | None]]
    ),
    format: Literal["coo"],
    dtype: _DTypeLike[_SCT_co],
) -> coo_array[Any, np.dtype[_SCT_co]] | coo_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def bmat(
    blocks: (
        Sequence[SparseArray[Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[SparseArray[Any] | npt.NDArray[Any] | None]]
    ),
    format: Literal["coo"],
    dtype: npt.DTypeLike | None = ...,
) -> coo_array[Any, np.dtype[_SCT_co]] | coo_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def bmat(
    blocks: (
        Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]]
    ),
    format: Literal["bsr"],
    dtype: _DTypeLike[_SCT_co],
) -> bsr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def bmat(
    blocks: (
        Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]]
    ),
    format: Literal["bsr"],
    dtype: npt.DTypeLike | None = ...,
) -> bsr_matrix[Any, Any]: ...
@overload
def bmat(
    blocks: (
        Sequence[SparseArray[Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[SparseArray[Any] | npt.NDArray[Any] | None]]
    ),
    format: Literal["bsr"],
    dtype: _DTypeLike[_SCT_co],
) -> bsr_array[Any, np.dtype[_SCT_co]] | bsr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def bmat(
    blocks: (
        Sequence[SparseArray[Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[SparseArray[Any] | npt.NDArray[Any] | None]]
    ),
    format: Literal["bsr"],
    dtype: npt.DTypeLike | None = ...,
) -> bsr_array[Any, np.dtype[_SCT_co]] | bsr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def bmat(
    blocks: (
        Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]]
    ),
    format: Literal["dia"],
    dtype: _DTypeLike[_SCT_co],
) -> dia_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def bmat(
    blocks: (
        Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]]
    ),
    format: Literal["dia"],
    dtype: npt.DTypeLike | None = ...,
) -> dia_matrix[Any, Any]: ...
@overload
def bmat(
    blocks: (
        Sequence[SparseArray[Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[SparseArray[Any] | npt.NDArray[Any] | None]]
    ),
    format: Literal["dia"],
    dtype: _DTypeLike[_SCT_co],
) -> dia_array[Any, np.dtype[_SCT_co]] | dia_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def bmat(
    blocks: (
        Sequence[SparseArray[Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[SparseArray[Any] | npt.NDArray[Any] | None]]
    ),
    format: Literal["dia"],
    dtype: npt.DTypeLike | None = ...,
) -> dia_array[Any, np.dtype[_SCT_co]] | dia_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def bmat(
    blocks: (
        Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]]
    ),
    format: Literal["dok"],
    dtype: _DTypeLike[_SCT_co],
) -> dok_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def bmat(
    blocks: (
        Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]]
    ),
    format: Literal["dok"],
    dtype: npt.DTypeLike | None = ...,
) -> dok_matrix[Any, Any]: ...
@overload
def bmat(
    blocks: (
        Sequence[SparseArray[Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[SparseArray[Any] | npt.NDArray[Any] | None]]
    ),
    format: Literal["dok"],
    dtype: _DTypeLike[_SCT_co],
) -> dok_array[Any, np.dtype[_SCT_co]] | dok_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def bmat(
    blocks: (
        Sequence[SparseArray[Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[SparseArray[Any] | npt.NDArray[Any] | None]]
    ),
    format: Literal["dok"],
    dtype: npt.DTypeLike | None = ...,
) -> dok_array[Any, np.dtype[_SCT_co]] | dok_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def bmat(
    blocks: (
        Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]]
    ),
    format: Literal["lil"],
    dtype: _DTypeLike[_SCT_co],
) -> lil_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def bmat(
    blocks: (
        Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]]
    ),
    format: Literal["lil"],
    dtype: npt.DTypeLike | None = ...,
) -> lil_matrix[Any, Any]: ...
@overload
def bmat(
    blocks: (
        Sequence[SparseArray[Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[SparseArray[Any] | npt.NDArray[Any] | None]]
    ),
    format: Literal["lil"],
    dtype: _DTypeLike[_SCT_co],
) -> lil_array[Any, np.dtype[_SCT_co]] | lil_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def bmat(
    blocks: (
        Sequence[SparseArray[Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[SparseArray[Any] | npt.NDArray[Any] | None]]
    ),
    format: Literal["lil"],
    dtype: npt.DTypeLike | None = ...,
) -> lil_array[Any, np.dtype[_SCT_co]] | lil_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_array(
    blocks: (
        Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]]
    ),
    *,
    format: None = ...,
    dtype: _DTypeLike[_SCT_co],
) -> spmatrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_array(
    blocks: (
        Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]]
    ),
    *,
    format: None = ...,
    dtype: npt.DTypeLike | None = ...,
) -> spmatrix[Any, Any]: ...
@overload
def block_array(
    blocks: (
        Sequence[SparseArray[Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[SparseArray[Any] | npt.NDArray[Any] | None]]
    ),
    *,
    format: None = ...,
    dtype: np.dtype[_SCT_co],
) -> SparseArray[_SCT_co]: ...
@overload
def block_array(
    blocks: (
        Sequence[SparseArray[Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[SparseArray[Any] | npt.NDArray[Any] | None]]
    ),
    *,
    format: None = ...,
    dtype: npt.DTypeLike | None = ...,
) -> SparseArray[Any]: ...
@overload
def block_array(
    blocks: (
        Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]]
    ),
    *,
    format: Literal["csc"],
    dtype: _DTypeLike[_SCT_co],
) -> csc_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_array(
    blocks: (
        Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]]
    ),
    *,
    format: Literal["csc"],
    dtype: npt.DTypeLike | None = ...,
) -> csc_matrix[Any, Any]: ...
@overload
def block_array(
    blocks: (
        Sequence[SparseArray[Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[SparseArray[Any] | npt.NDArray[Any] | None]]
    ),
    *,
    format: Literal["csc"],
    dtype: _DTypeLike[_SCT_co],
) -> csc_array[Any, np.dtype[_SCT_co]] | csc_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_array(
    blocks: (
        Sequence[SparseArray[Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[SparseArray[Any] | npt.NDArray[Any] | None]]
    ),
    *,
    format: Literal["csc"],
    dtype: npt.DTypeLike | None = ...,
) -> csc_array[Any, np.dtype[_SCT_co]] | csc_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_array(
    blocks: (
        Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]]
    ),
    *,
    format: Literal["csr"],
    dtype: _DTypeLike[_SCT_co],
) -> csr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_array(
    blocks: (
        Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]]
    ),
    *,
    format: Literal["csr"],
    dtype: npt.DTypeLike | None = ...,
) -> csr_matrix[Any, Any]: ...
@overload
def block_array(
    blocks: (
        Sequence[SparseArray[Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[SparseArray[Any] | npt.NDArray[Any] | None]]
    ),
    *,
    format: Literal["csr"],
    dtype: _DTypeLike[_SCT_co],
) -> csr_array[Any, np.dtype[_SCT_co]] | csr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_array(
    blocks: (
        Sequence[SparseArray[Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[SparseArray[Any] | npt.NDArray[Any] | None]]
    ),
    *,
    format: Literal["csr"],
    dtype: npt.DTypeLike | None = ...,
) -> csr_array[Any, np.dtype[_SCT_co]] | csr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_array(
    blocks: (
        Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]]
    ),
    *,
    format: Literal["coo"],
    dtype: _DTypeLike[_SCT_co],
) -> coo_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_array(
    blocks: (
        Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]]
    ),
    *,
    format: Literal["coo"],
    dtype: npt.DTypeLike | None = ...,
) -> coo_matrix[Any, Any]: ...
@overload
def block_array(
    blocks: (
        Sequence[SparseArray[Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[SparseArray[Any] | npt.NDArray[Any] | None]]
    ),
    *,
    format: Literal["coo"],
    dtype: _DTypeLike[_SCT_co],
) -> coo_array[Any, np.dtype[_SCT_co]] | coo_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_array(
    blocks: (
        Sequence[SparseArray[Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[SparseArray[Any] | npt.NDArray[Any] | None]]
    ),
    *,
    format: Literal["coo"],
    dtype: npt.DTypeLike | None = ...,
) -> coo_array[Any, np.dtype[_SCT_co]] | coo_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_array(
    blocks: (
        Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]]
    ),
    *,
    format: Literal["bsr"],
    dtype: _DTypeLike[_SCT_co],
) -> bsr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_array(
    blocks: (
        Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]]
    ),
    *,
    format: Literal["bsr"],
    dtype: npt.DTypeLike | None = ...,
) -> bsr_matrix[Any, Any]: ...
@overload
def block_array(
    blocks: (
        Sequence[SparseArray[Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[SparseArray[Any] | npt.NDArray[Any] | None]]
    ),
    *,
    format: Literal["bsr"],
    dtype: _DTypeLike[_SCT_co],
) -> bsr_array[Any, np.dtype[_SCT_co]] | bsr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_array(
    blocks: (
        Sequence[SparseArray[Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[SparseArray[Any] | npt.NDArray[Any] | None]]
    ),
    *,
    format: Literal["bsr"],
    dtype: npt.DTypeLike | None = ...,
) -> bsr_array[Any, np.dtype[_SCT_co]] | bsr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_array(
    blocks: (
        Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]]
    ),
    *,
    format: Literal["dia"],
    dtype: _DTypeLike[_SCT_co],
) -> dia_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_array(
    blocks: (
        Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]]
    ),
    *,
    format: Literal["dia"],
    dtype: npt.DTypeLike | None = ...,
) -> dia_matrix[Any, Any]: ...
@overload
def block_array(
    blocks: (
        Sequence[SparseArray[Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[SparseArray[Any] | npt.NDArray[Any] | None]]
    ),
    *,
    format: Literal["dia"],
    dtype: _DTypeLike[_SCT_co],
) -> dia_array[Any, np.dtype[_SCT_co]] | dia_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_array(
    blocks: (
        Sequence[SparseArray[Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[SparseArray[Any] | npt.NDArray[Any] | None]]
    ),
    *,
    format: Literal["dia"],
    dtype: npt.DTypeLike | None = ...,
) -> dia_array[Any, np.dtype[_SCT_co]] | dia_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_array(
    blocks: (
        Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]]
    ),
    *,
    format: Literal["dok"],
    dtype: _DTypeLike[_SCT_co],
) -> dok_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_array(
    blocks: (
        Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]]
    ),
    *,
    format: Literal["dok"],
    dtype: npt.DTypeLike | None = ...,
) -> dok_matrix[Any, Any]: ...
@overload
def block_array(
    blocks: (
        Sequence[SparseArray[Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[SparseArray[Any] | npt.NDArray[Any] | None]]
    ),
    *,
    format: Literal["dok"],
    dtype: _DTypeLike[_SCT_co],
) -> dok_array[Any, np.dtype[_SCT_co]] | dok_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_array(
    blocks: (
        Sequence[SparseArray[Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[SparseArray[Any] | npt.NDArray[Any] | None]]
    ),
    *,
    format: Literal["dok"],
    dtype: npt.DTypeLike | None = ...,
) -> dok_array[Any, np.dtype[_SCT_co]] | dok_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_array(
    blocks: (
        Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]]
    ),
    *,
    format: Literal["lil"],
    dtype: _DTypeLike[_SCT_co],
) -> lil_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_array(
    blocks: (
        Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[spmatrix[Any, Any] | npt.NDArray[Any] | None]]
    ),
    *,
    format: Literal["lil"],
    dtype: npt.DTypeLike | None = ...,
) -> lil_matrix[Any, Any]: ...
@overload
def block_array(
    blocks: (
        Sequence[SparseArray[Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[SparseArray[Any] | npt.NDArray[Any] | None]]
    ),
    *,
    format: Literal["lil"],
    dtype: _DTypeLike[_SCT_co],
) -> lil_array[Any, np.dtype[_SCT_co]] | lil_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_array(
    blocks: (
        Sequence[SparseArray[Any] | npt.NDArray[Any] | None]
        | Sequence[Sequence[SparseArray[Any] | npt.NDArray[Any] | None]]
    ),
    *,
    format: Literal["lil"],
    dtype: npt.DTypeLike | None = ...,
) -> lil_array[Any, np.dtype[_SCT_co]] | lil_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_diag(
    mats: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: None,
    dtype: _DTypeLike[_SCT_co],
) -> spmatrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_diag(
    mats: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: None = ...,
    *,
    dtype: _DTypeLike[_SCT_co],
) -> spmatrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_diag(
    mats: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: None = ...,
    dtype: npt.DTypeLike | None = ...,
) -> spmatrix[Any, Any]: ...
@overload
def block_diag(
    mats: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: None,
    dtype: _DTypeLike[_SCT_co],
) -> SparseArray[_SCT_co]: ...
@overload
def block_diag(
    mats: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: None = ...,
    *,
    dtype: np.dtype[_SCT_co],
) -> SparseArray[_SCT_co]: ...
@overload
def block_diag(
    mats: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: None = ...,
    dtype: npt.DTypeLike | None = ...,
) -> SparseArray[Any]: ...
@overload
def block_diag(
    mats: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: Literal["csc"],
    dtype: _DTypeLike[_SCT_co],
) -> csc_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_diag(
    mats: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: Literal["csc"],
    dtype: npt.DTypeLike | None = ...,
) -> csc_matrix[Any, Any]: ...
@overload
def block_diag(
    mats: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: Literal["csc"],
    dtype: _DTypeLike[_SCT_co],
) -> csc_array[Any, np.dtype[_SCT_co]] | csc_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_diag(
    mats: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: Literal["csc"],
    dtype: npt.DTypeLike | None = ...,
) -> csc_array[Any, np.dtype[_SCT_co]] | csc_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_diag(
    mats: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: Literal["csr"],
    dtype: _DTypeLike[_SCT_co],
) -> csr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_diag(
    mats: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: Literal["csr"],
    dtype: npt.DTypeLike | None = ...,
) -> csr_matrix[Any, Any]: ...
@overload
def block_diag(
    mats: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: Literal["csr"],
    dtype: _DTypeLike[_SCT_co],
) -> csr_array[Any, np.dtype[_SCT_co]] | csr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_diag(
    mats: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: Literal["csr"],
    dtype: npt.DTypeLike | None = ...,
) -> csr_array[Any, np.dtype[_SCT_co]] | csr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_diag(
    mats: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: Literal["coo"],
    dtype: _DTypeLike[_SCT_co],
) -> coo_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_diag(
    mats: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: Literal["coo"],
    dtype: npt.DTypeLike | None = ...,
) -> coo_matrix[Any, Any]: ...
@overload
def block_diag(
    mats: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: Literal["coo"],
    dtype: _DTypeLike[_SCT_co],
) -> coo_array[Any, np.dtype[_SCT_co]] | coo_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_diag(
    mats: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: Literal["coo"],
    dtype: npt.DTypeLike | None = ...,
) -> coo_array[Any, np.dtype[_SCT_co]] | coo_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_diag(
    mats: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: Literal["bsr"],
    dtype: _DTypeLike[_SCT_co],
) -> bsr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_diag(
    mats: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: Literal["bsr"],
    dtype: npt.DTypeLike | None = ...,
) -> bsr_matrix[Any, Any]: ...
@overload
def block_diag(
    mats: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: Literal["bsr"],
    dtype: _DTypeLike[_SCT_co],
) -> bsr_array[Any, np.dtype[_SCT_co]] | bsr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_diag(
    mats: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: Literal["bsr"],
    dtype: npt.DTypeLike | None = ...,
) -> bsr_array[Any, np.dtype[_SCT_co]] | bsr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_diag(
    mats: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: Literal["dia"],
    dtype: _DTypeLike[_SCT_co],
) -> dia_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_diag(
    mats: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: Literal["dia"],
    dtype: npt.DTypeLike | None = ...,
) -> dia_matrix[Any, Any]: ...
@overload
def block_diag(
    mats: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: Literal["dia"],
    dtype: _DTypeLike[_SCT_co],
) -> dia_array[Any, np.dtype[_SCT_co]] | dia_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_diag(
    mats: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: Literal["dia"],
    dtype: npt.DTypeLike | None = ...,
) -> dia_array[Any, np.dtype[_SCT_co]] | dia_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_diag(
    mats: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: Literal["dok"],
    dtype: _DTypeLike[_SCT_co],
) -> dok_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_diag(
    mats: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: Literal["dok"],
    dtype: npt.DTypeLike | None = ...,
) -> dok_matrix[Any, Any]: ...
@overload
def block_diag(
    mats: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: Literal["dok"],
    dtype: _DTypeLike[_SCT_co],
) -> dok_array[Any, np.dtype[_SCT_co]] | dok_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_diag(
    mats: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: Literal["dok"],
    dtype: npt.DTypeLike | None = ...,
) -> dok_array[Any, np.dtype[_SCT_co]] | dok_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_diag(
    mats: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: Literal["lil"],
    dtype: _DTypeLike[_SCT_co],
) -> lil_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_diag(
    mats: Sequence[spmatrix[Any, Any] | npt.NDArray[Any]],
    format: Literal["lil"],
    dtype: npt.DTypeLike | None = ...,
) -> lil_matrix[Any, Any]: ...
@overload
def block_diag(
    mats: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: Literal["lil"],
    dtype: _DTypeLike[_SCT_co],
) -> lil_array[Any, np.dtype[_SCT_co]] | lil_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def block_diag(
    mats: Sequence[SparseArray[Any] | npt.NDArray[Any]],
    format: Literal["lil"],
    dtype: npt.DTypeLike | None = ...,
) -> lil_array[Any, np.dtype[_SCT_co]] | lil_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def random_array(
    shape: SupportsIndex | tuple[SupportsIndex, SupportsIndex],
    *,
    density: SupportsFloat = ...,
    format: Literal["csc"],
    dtype: _DTypeLike[_SCT_co],
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
    data_sampler: DataSamplerType | None = ...,
) -> csc_array[Any, np.dtype[_SCT_co]]: ...
@overload
def random_array(
    shape: SupportsIndex | tuple[SupportsIndex, SupportsIndex],
    *,
    density: SupportsFloat = ...,
    format: Literal["csc"],
    dtype: npt.DTypeLike | None = ...,
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
    data_sampler: DataSamplerType | None = ...,
) -> csc_array[Any, Any]: ...
@overload
def random_array(
    shape: SupportsIndex | tuple[SupportsIndex, SupportsIndex],
    *,
    density: SupportsFloat = ...,
    format: Literal["csr"],
    dtype: _DTypeLike[_SCT_co],
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
    data_sampler: DataSamplerType | None = ...,
) -> csr_array[Any, np.dtype[_SCT_co]]: ...
@overload
def random_array(
    shape: SupportsIndex | tuple[SupportsIndex, SupportsIndex],
    *,
    density: SupportsFloat = ...,
    format: Literal["csr"],
    dtype: npt.DTypeLike | None = ...,
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
    data_sampler: DataSamplerType | None = ...,
) -> csr_array[Any, Any]: ...
@overload
def random_array(
    shape: SupportsIndex | tuple[SupportsIndex, SupportsIndex],
    *,
    density: SupportsFloat = ...,
    format: Literal["coo"] | None = ...,
    dtype: _DTypeLike[_SCT_co],
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
    data_sampler: DataSamplerType | None = ...,
) -> coo_array[Any, np.dtype[_SCT_co]]: ...
@overload
def random_array(
    shape: SupportsIndex | tuple[SupportsIndex, SupportsIndex],
    *,
    density: SupportsFloat = ...,
    format: Literal["coo"] | None = ...,
    dtype: npt.DTypeLike | None = ...,
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
    data_sampler: DataSamplerType | None = ...,
) -> coo_array[Any, Any]: ...
@overload
def random_array(
    shape: SupportsIndex | tuple[SupportsIndex, SupportsIndex],
    *,
    density: SupportsFloat = ...,
    format: Literal["bsr"],
    dtype: _DTypeLike[_SCT_co],
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
    data_sampler: DataSamplerType | None = ...,
) -> bsr_array[Any, np.dtype[_SCT_co]]: ...
@overload
def random_array(
    shape: SupportsIndex | tuple[SupportsIndex, SupportsIndex],
    *,
    density: SupportsFloat = ...,
    format: Literal["bsr"],
    dtype: npt.DTypeLike | None = ...,
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
    data_sampler: DataSamplerType | None = ...,
) -> bsr_array[Any, Any]: ...
@overload
def random_array(
    shape: SupportsIndex | tuple[SupportsIndex, SupportsIndex],
    *,
    density: SupportsFloat = ...,
    format: Literal["dia"],
    dtype: _DTypeLike[_SCT_co],
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
    data_sampler: DataSamplerType | None = ...,
) -> dia_array[Any, np.dtype[_SCT_co]]: ...
@overload
def random_array(
    shape: SupportsIndex | tuple[SupportsIndex, SupportsIndex],
    *,
    density: SupportsFloat = ...,
    format: Literal["dia"],
    dtype: npt.DTypeLike | None = ...,
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
    data_sampler: DataSamplerType | None = ...,
) -> dia_array[Any, Any]: ...
@overload
def random_array(
    shape: SupportsIndex | tuple[SupportsIndex, SupportsIndex],
    *,
    density: SupportsFloat = ...,
    format: Literal["dok"],
    dtype: _DTypeLike[_SCT_co],
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
    data_sampler: DataSamplerType | None = ...,
) -> dok_array[Any, np.dtype[_SCT_co]]: ...
@overload
def random_array(
    shape: SupportsIndex | tuple[SupportsIndex, SupportsIndex],
    *,
    density: SupportsFloat = ...,
    format: Literal["dok"],
    dtype: npt.DTypeLike | None = ...,
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
    data_sampler: DataSamplerType | None = ...,
) -> dok_array[Any, Any]: ...
@overload
def random_array(
    shape: SupportsIndex | tuple[SupportsIndex, SupportsIndex],
    *,
    density: SupportsFloat = ...,
    format: Literal["lil"],
    dtype: _DTypeLike[_SCT_co],
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
    data_sampler: DataSamplerType | None = ...,
) -> lil_array[Any, np.dtype[_SCT_co]]: ...
@overload
def random_array(
    shape: SupportsIndex | tuple[SupportsIndex, SupportsIndex],
    *,
    density: SupportsFloat = ...,
    format: Literal["lil"],
    dtype: npt.DTypeLike | None = ...,
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
    data_sampler: DataSamplerType | None = ...,
) -> lil_array[Any, Any]: ...
@overload
def random(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat,
    format: Literal["coo"] | None,
    dtype: _DTypeLike[_SCT_co],
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
    data_rvs: DataRVsType | None = ...,
) -> coo_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def random(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat = ...,
    format: Literal["coo"] | None = ...,
    *,
    dtype: _DTypeLike[_SCT_co],
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
    data_rvs: DataRVsType | None = ...,
) -> coo_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def random(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat,
    format: Literal["coo"] | None,
    dtype: npt.DTypeLike | None = ...,
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
    data_rvs: DataRVsType | None = ...,
) -> coo_matrix[Any, Any]: ...
@overload
def random(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat = ...,
    format: Literal["coo"] | None = ...,
    *,
    dtype: npt.DTypeLike | None = ...,
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
    data_rvs: DataRVsType | None = ...,
) -> coo_matrix[Any, Any]: ...
@overload
def random(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat,
    format: Literal["csc"],
    dtype: _DTypeLike[_SCT_co],
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
    data_rvs: DataRVsType | None = ...,
) -> csc_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def random(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat = ...,
    *,
    format: Literal["csc"],
    dtype: _DTypeLike[_SCT_co],
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
    data_rvs: DataRVsType | None = ...,
) -> csc_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def random(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat,
    format: Literal["csc"],
    dtype: npt.DTypeLike | None = ...,
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
    data_rvs: DataRVsType | None = ...,
) -> csc_matrix[Any, Any]: ...
@overload
def random(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat = ...,
    *,
    format: Literal["csc"],
    dtype: npt.DTypeLike | None = ...,
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
    data_rvs: DataRVsType | None = ...,
) -> csc_matrix[Any, Any]: ...
@overload
def random(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat,
    format: Literal["csr"],
    dtype: _DTypeLike[_SCT_co],
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
    data_rvs: DataRVsType | None = ...,
) -> csr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def random(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat = ...,
    *,
    format: Literal["csr"],
    dtype: _DTypeLike[_SCT_co],
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
    data_rvs: DataRVsType | None = ...,
) -> csr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def random(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat,
    format: Literal["csr"],
    dtype: npt.DTypeLike | None = ...,
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
    data_rvs: DataRVsType | None = ...,
) -> csr_matrix[Any, Any]: ...
@overload
def random(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat = ...,
    *,
    format: Literal["csr"],
    dtype: npt.DTypeLike | None = ...,
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
    data_rvs: DataRVsType | None = ...,
) -> csr_matrix[Any, Any]: ...
@overload
def random(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat,
    format: Literal["bsr"],
    dtype: _DTypeLike[_SCT_co],
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
    data_rvs: DataRVsType | None = ...,
) -> bsr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def random(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat = ...,
    *,
    format: Literal["bsr"],
    dtype: _DTypeLike[_SCT_co],
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
    data_rvs: DataRVsType | None = ...,
) -> bsr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def random(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat,
    format: Literal["bsr"],
    dtype: npt.DTypeLike | None = ...,
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
    data_rvs: DataRVsType | None = ...,
) -> bsr_matrix[Any, Any]: ...
@overload
def random(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat = ...,
    *,
    format: Literal["bsr"],
    dtype: npt.DTypeLike | None = ...,
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
    data_rvs: DataRVsType | None = ...,
) -> bsr_matrix[Any, Any]: ...
@overload
def random(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat,
    format: Literal["dia"],
    dtype: _DTypeLike[_SCT_co],
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
    data_rvs: DataRVsType | None = ...,
) -> dia_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def random(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat = ...,
    *,
    format: Literal["dia"],
    dtype: _DTypeLike[_SCT_co],
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
    data_rvs: DataRVsType | None = ...,
) -> dia_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def random(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat,
    format: Literal["dia"],
    dtype: npt.DTypeLike | None = ...,
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
    data_rvs: DataRVsType | None = ...,
) -> dia_matrix[Any, Any]: ...
@overload
def random(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat = ...,
    *,
    format: Literal["dia"],
    dtype: npt.DTypeLike | None = ...,
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
    data_rvs: DataRVsType | None = ...,
) -> dia_matrix[Any, Any]: ...
@overload
def random(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat,
    format: Literal["dok"],
    dtype: _DTypeLike[_SCT_co],
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
    data_rvs: DataRVsType | None = ...,
) -> dok_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def random(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat = ...,
    *,
    format: Literal["dok"],
    dtype: _DTypeLike[_SCT_co],
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
    data_rvs: DataRVsType | None = ...,
) -> dok_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def random(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat,
    format: Literal["dok"],
    dtype: npt.DTypeLike | None = ...,
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
    data_rvs: DataRVsType | None = ...,
) -> dok_matrix[Any, Any]: ...
@overload
def random(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat = ...,
    *,
    format: Literal["dok"],
    dtype: npt.DTypeLike | None = ...,
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
    data_rvs: DataRVsType | None = ...,
) -> dok_matrix[Any, Any]: ...
@overload
def random(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat,
    format: Literal["lil"],
    dtype: _DTypeLike[_SCT_co],
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
    data_rvs: DataRVsType | None = ...,
) -> lil_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def random(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat = ...,
    *,
    format: Literal["lil"],
    dtype: _DTypeLike[_SCT_co],
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
    data_rvs: DataRVsType | None = ...,
) -> lil_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def random(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat,
    format: Literal["lil"],
    dtype: npt.DTypeLike | None = ...,
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
    data_rvs: DataRVsType | None = ...,
) -> lil_matrix[Any, Any]: ...
@overload
def random(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat = ...,
    *,
    format: Literal["lil"],
    dtype: npt.DTypeLike | None = ...,
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
    data_rvs: DataRVsType | None = ...,
) -> lil_matrix[Any, Any]: ...
@overload
def rand(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat,
    format: Literal["coo"] | None,
    dtype: _DTypeLike[_SCT_co],
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
) -> coo_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def rand(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat = ...,
    format: Literal["coo"] | None = ...,
    *,
    dtype: _DTypeLike[_SCT_co],
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
) -> coo_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def rand(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat,
    format: Literal["coo"] | None,
    dtype: npt.DTypeLike | None = ...,
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
) -> coo_matrix[Any, Any]: ...
@overload
def rand(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat = ...,
    format: Literal["coo"] | None = ...,
    *,
    dtype: npt.DTypeLike | None = ...,
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
) -> coo_matrix[Any, Any]: ...
@overload
def rand(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat,
    format: Literal["csc"],
    dtype: _DTypeLike[_SCT_co],
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
) -> csc_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def rand(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat = ...,
    *,
    format: Literal["csc"],
    dtype: _DTypeLike[_SCT_co],
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
) -> csc_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def rand(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat,
    format: Literal["csc"],
    dtype: npt.DTypeLike | None = ...,
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
) -> csc_matrix[Any, Any]: ...
@overload
def rand(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat = ...,
    *,
    format: Literal["csc"],
    dtype: npt.DTypeLike | None = ...,
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
) -> csc_matrix[Any, Any]: ...
@overload
def rand(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat,
    format: Literal["csr"],
    dtype: _DTypeLike[_SCT_co],
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
) -> csr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def rand(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat = ...,
    *,
    format: Literal["csr"],
    dtype: _DTypeLike[_SCT_co],
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
) -> csr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def rand(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat,
    format: Literal["csr"],
    dtype: npt.DTypeLike | None = ...,
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
) -> csr_matrix[Any, Any]: ...
@overload
def rand(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat = ...,
    *,
    format: Literal["csr"],
    dtype: npt.DTypeLike | None = ...,
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
) -> csr_matrix[Any, Any]: ...
@overload
def rand(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat,
    format: Literal["bsr"],
    dtype: _DTypeLike[_SCT_co],
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
) -> bsr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def rand(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat = ...,
    *,
    format: Literal["bsr"],
    dtype: _DTypeLike[_SCT_co],
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
) -> bsr_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def rand(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat,
    format: Literal["bsr"],
    dtype: npt.DTypeLike | None = ...,
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
) -> bsr_matrix[Any, Any]: ...
@overload
def rand(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat = ...,
    *,
    format: Literal["bsr"],
    dtype: npt.DTypeLike | None = ...,
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
) -> bsr_matrix[Any, Any]: ...
@overload
def rand(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat,
    format: Literal["dia"],
    dtype: _DTypeLike[_SCT_co],
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
) -> dia_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def rand(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat = ...,
    *,
    format: Literal["dia"],
    dtype: _DTypeLike[_SCT_co],
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
) -> dia_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def rand(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat,
    format: Literal["dia"],
    dtype: npt.DTypeLike | None = ...,
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
) -> dia_matrix[Any, Any]: ...
@overload
def rand(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat = ...,
    *,
    format: Literal["dia"],
    dtype: npt.DTypeLike | None = ...,
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
) -> dia_matrix[Any, Any]: ...
@overload
def rand(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat,
    format: Literal["dok"],
    dtype: _DTypeLike[_SCT_co],
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
) -> dok_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def rand(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat = ...,
    *,
    format: Literal["dok"],
    dtype: _DTypeLike[_SCT_co],
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
) -> dok_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def rand(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat,
    format: Literal["dok"],
    dtype: npt.DTypeLike | None = ...,
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
) -> dok_matrix[Any, Any]: ...
@overload
def rand(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat = ...,
    *,
    format: Literal["dok"],
    dtype: npt.DTypeLike | None = ...,
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
) -> dok_matrix[Any, Any]: ...
@overload
def rand(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat,
    format: Literal["lil"],
    dtype: _DTypeLike[_SCT_co],
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
) -> lil_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def rand(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat = ...,
    *,
    format: Literal["lil"],
    dtype: _DTypeLike[_SCT_co],
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
) -> lil_matrix[Any, np.dtype[_SCT_co]]: ...
@overload
def rand(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat,
    format: Literal["lil"],
    dtype: npt.DTypeLike | None = ...,
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
) -> lil_matrix[Any, Any]: ...
@overload
def rand(
    m: SupportsIndex,
    n: SupportsIndex | None,
    density: SupportsFloat = ...,
    *,
    format: Literal["lil"],
    dtype: npt.DTypeLike | None = ...,
    random_state: (
        np.random.RandomState | np.random.Generator | SupportsInt | None
    ) = ...,
) -> lil_matrix[Any, Any]: ...
