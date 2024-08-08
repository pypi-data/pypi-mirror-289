from collections.abc import Sequence
from typing import (
    Any,
    Literal,
    NoReturn,
    SupportsFloat,
    SupportsIndex,
    SupportsInt,
    overload,
)
from typing_extensions import TypeIs

import numpy as np
import numpy.typing as npt

from ._matrix import spmatrix
from .typing import (
    _SCT,
    SparseArray,
    _ArrayLike,
    _ArrayLikeInt_co,
    _ArrayType,
    _DType,
    _DType_co,
    _DTypeLike,
    _MatrixType,
    _ScalarLike_co,
    _ShapeAnno,
    _SupportsArrayFunc,
    _SupportsDType,
)

__all__ = [
    "upcast",
    "getdtype",
    "getdata",
    "isscalarlike",
    "isintlike",
    "isshape",
    "issequence",
    "isdense",
    "ismatrix",
    "get_sum_dtype",
]

supported_dtypes: list[type[np.generic]]

def upcast(*args: npt.ArrayLike | npt.DTypeLike) -> np.generic: ...
def upcast_char(*args: Any) -> np.generic: ...
def upcast_scalar(dtype: npt.DTypeLike, scalar: _ScalarLike_co) -> np.dtype[Any]: ...
def downcast_intp_index(
    arr: npt.NDArray[np.integer[Any]],
) -> npt.NDArray[np.intp]: ...
def to_native(A: _ArrayType) -> _ArrayType: ...
@overload
def getdtype(
    dtype: _DType, a: None | _SupportsDType[Any] = ..., default: None = ...
) -> _DType: ...
@overload
def getdtype(
    dtype: _SCT, a: None | _SupportsDType[Any] = ..., default: None = ...
) -> np.dtype[_SCT]: ...
@overload
def getdtype(
    dtype: _ScalarLike_co,
    a: None | _SupportsDType[Any] = ...,
    default: None = ...,
) -> np.dtype[Any]: ...
@overload
def getdtype(
    dtype: None, a: _SupportsDType[_DType_co], default: None = ...
) -> _DType_co: ...
@overload
def getdtype(dtype: None, a: None = ..., default: None = ...) -> NoReturn: ...
@overload
def getdtype(dtype: None, a: None, default: _DType = ...) -> _DType: ...
@overload
def getdtype(dtype: None, *, default: _DType) -> _DType: ...
@overload
def getdtype(dtype: None, a: None, default: _SCT) -> np.dtype[_SCT]: ...
@overload
def getdtype(dtype: None, *, default: _SCT) -> np.dtype[_SCT]: ...
@overload
def getdtype(dtype: None, a: None, default: _ScalarLike_co) -> np.dtype[Any]: ...
@overload
def getdtype(dtype: None, *, default: _ScalarLike_co) -> np.dtype[Any]: ...
def getdata(
    obj: npt.ArrayLike, dtype: npt.DTypeLike | None = ..., copy: bool = ...
) -> npt.NDArray[Any]: ...
def get_index_dtype(
    arrays: _ArrayLikeInt_co = ...,
    maxval: SupportsFloat | None = ...,
    check_contents: bool = False,
) -> np.int32 | np.int64: ...
@overload
def get_sum_dtype(
    dtype: np.dtype[np.int_ | np.bool_],
) -> np.dtype[np.int_]: ...
@overload
def get_sum_dtype(
    dtype: np.dtype[np.unsignedinteger[Any]],
) -> np.dtype[np.unsignedinteger[Any]]: ...
@overload
def get_sum_dtype(dtype: np.dtype[np.float_]) -> np.dtype[np.float_]: ...
@overload
def get_sum_dtype(dtype: np.dtype[np.complex_]) -> np.dtype[np.complex_]: ...
@overload
def get_sum_dtype(dtype: np.dtype[Any]) -> np.dtype[Any]: ...
def isscalarlike(x: Any) -> TypeIs[_ScalarLike_co | npt.NDArray[Any]]: ...
def isintlike(x: Any) -> TypeIs[SupportsIndex | SupportsInt]: ...
@overload
def isshape(
    x: Any, nonneg: bool = ..., *, allow_1d: Literal[False] = ...
) -> TypeIs[tuple[SupportsIndex, SupportsIndex]]: ...
@overload
def isshape(
    x: Any, nonneg: bool = ..., *, allow_1d: bool = ...
) -> TypeIs[tuple[SupportsIndex, SupportsIndex] | tuple[SupportsIndex]]: ...
def issequence(
    t: Any,
) -> TypeIs[Sequence[_ScalarLike_co] | npt.NDArray[Any]]: ...
def ismatrix(
    t: Any,
) -> TypeIs[
    Sequence[Sequence[_ScalarLike_co] | npt.NDArray[Any]] | npt.NDArray[Any]
]: ...
def isdense(x: Any) -> TypeIs[npt.NDArray[Any]]: ...
def validateaxis(axis: Literal[-2, -1, 0, 1, None]) -> None: ...
def check_shape(
    args: npt.ArrayLike,
    current_shape: Sequence[SupportsIndex] | None = None,
    *,
    allow_1d: bool = ...,
) -> tuple[int, ...]: ...
def check_reshape_kwargs(
    kwargs: dict[Any, Any],
) -> tuple[Literal["C", "F", None], bool]: ...
def is_pydata_spmatrix(m: Any) -> bool: ...
def convert_pydata_sparse_to_scipy(
    arg: Any, target_format: Literal["csc", "csr"] | None = ...
) -> Any | spmatrix[Any, Any]: ...

# matrix is like asarray but with view as matrix
@overload
def matrix(
    a: _ArrayLike[_SCT],
    dtype: None = ...,
    order: np._OrderKACF = ...,
    *,
    like: None | _SupportsArrayFunc = ...,
) -> np.matrix[Any, np.dtype[_SCT]]: ...
@overload
def matrix(
    a: object,
    dtype: None = ...,
    order: np._OrderKACF = ...,
    *,
    like: None | _SupportsArrayFunc = ...,
) -> np.matrix[Any, np.dtype[Any]]: ...
@overload
def matrix(
    a: Any,
    dtype: _DTypeLike[_SCT],
    order: np._OrderKACF = ...,
    *,
    like: None | _SupportsArrayFunc = ...,
) -> np.matrix[Any, np.dtype[_SCT]]: ...
@overload
def matrix(
    a: Any,
    dtype: npt.DTypeLike,
    order: np._OrderKACF = ...,
    *,
    like: None | _SupportsArrayFunc = ...,
) -> np.matrix[Any, np.dtype[Any]]: ...
@overload
def asmatrix(data: _MatrixType, dtype: None = ...) -> _MatrixType: ...
@overload
def asmatrix(
    data: np.ndarray[_ShapeAnno, _DType_co], dtype: None = ...
) -> np.matrix[_ShapeAnno, _DType_co]: ...
@overload
def asmatrix(
    data: np.ndarray[_ShapeAnno, Any], dtype: _DType
) -> np.matrix[_ShapeAnno, _DType]: ...
@overload
def asmatrix(
    data: np.ndarray[_ShapeAnno, Any], dtype: _DTypeLike[_SCT]
) -> np.matrix[_ShapeAnno, np.dtype[_SCT]]: ...
@overload
def asmatrix(
    data: np.ndarray[_ShapeAnno, Any], dtype: npt.DTypeLike
) -> np.matrix[_ShapeAnno, np.dtype[Any]]: ...
def _todata(s: SparseArray[_SCT]) -> npt.NDArray[_SCT]: ...
