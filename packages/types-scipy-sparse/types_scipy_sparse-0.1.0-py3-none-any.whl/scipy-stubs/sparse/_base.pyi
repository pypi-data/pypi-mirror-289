from collections.abc import Iterator
from typing import (
    Any,
    Literal,
    Protocol,
    SupportsIndex,
    overload,
    runtime_checkable,
)
from typing_extensions import Self, TypeIs

import numpy as np
from numpy import typing as npt

from ._bsr import bsr_array
from ._coo import coo_array
from ._csc import csc_array
from ._csr import csr_array
from ._dia import dia_array
from ._dok import dok_array
from ._lil import lil_array
from ._matrix import spmatrix
from .typing import (
    _SCT,
    SparseArray,
    _ArrayType,
    _CastingKind,
    _DType_co,
    _DTypeLike,
    _Formats,
    _NumberLike_co,
    _OrderType,
    _SCT_uifcO,
    _ShapeAnno,
    _ShapeLike,
)

__all__ = [
    "isspmatrix",
    "issparse",
    "sparray",
    "SparseWarning",
    "SparseEfficiencyWarning",
]

MAXPRINT: int

class SparseWarning(Warning): ...
class SparseFormatWarning(SparseWarning): ...
class SparseEfficiencyWarning(SparseWarning): ...

# Although sparray is not a Protocol, I hint it as such such that if
# subclassed it is clear that the methods and attributes are meant to be
# implemented. All methods and attributes are as in the private base class
# _spbase (except for the missing `def __init__`)
@runtime_checkable
class sparray(Protocol[_ShapeAnno, _DType_co]):
    ###########################################################################
    # common attributes / methods common to all sparray/spmatrix
    # inherited from private base class _spbase
    ###########################################################################

    __array_priority__: float
    @property
    def ndim(self) -> int: ...
    maxprint: int
    @property
    def shape(self) -> tuple[int, ...]: ...
    def __iter__(self) -> Iterator[Any]: ...
    def count_nonzero(self) -> int: ...
    @property
    def nnz(self) -> int: ...
    @property
    def size(self) -> int: ...
    def __bool__(self) -> bool: ...
    def __nonzero__(self) -> bool: ...
    def __len__(self) -> int: ...
    def __eq__(self, other: object) -> Any: ...
    def __ne__(self, other: object) -> Any: ...
    def __lt__(self, other: object) -> Any: ...
    def __gt__(self, other: object) -> Any: ...
    def __le__(self, other: object) -> Any: ...
    def __ge__(self, other: object) -> Any: ...
    def conjugate(self, copy: bool = ...) -> Self: ...
    def conj(self, copy: bool = ...) -> Self: ...
    def nonzero(self) -> tuple[npt.NDArray[np.int_], npt.NDArray[np.int_]]: ...
    @overload
    def toarray(
        self, order: _OrderType | None = ..., out: None = ...
    ) -> np.ndarray[_ShapeAnno, _DType_co]: ...
    @overload
    def toarray(self, order: None = ..., out: _ArrayType = ...) -> _ArrayType: ...
    def copy(self) -> Self: ...
    def diagonal(self, k: SupportsIndex = ...) -> np.ndarray[Any, _DType_co]: ...
    def setdiag(self, values: npt.ArrayLike, k: SupportsIndex = ...) -> None: ...
    @overload
    def resize(self, shape: _ShapeLike) -> None: ...
    @overload
    def resize(self, *shape: SupportsIndex) -> None: ...
    @overload
    def sum(
        self: sparray[Any, np.dtype[np.bool_ | np.int_]],
        axis: None = ...,
        dtype: None = ...,
        out: None = ...,
    ) -> np.int_: ...
    @overload
    def sum(
        self: sparray[Any, np.dtype[np.unsignedinteger[Any]]],
        axis: None = ...,
        dtype: None = ...,
        out: None = ...,
    ) -> np.unsignedinteger[Any]: ...
    @overload
    def sum(
        self: sparray[Any, np.dtype[np.float_]],
        axis: None = ...,
        dtype: None = ...,
        out: None = ...,
    ) -> np.float_: ...
    @overload
    def sum(
        self: sparray[Any, np.dtype[np.complex_]],
        axis: None = ...,
        dtype: None = ...,
        out: None = ...,
    ) -> np.complex_: ...
    @overload
    def sum(
        self,
        axis: None = ...,
        dtype: None = ...,
        out: None = ...,
    ) -> Any: ...
    @overload
    def sum(
        self: sparray[Any, np.dtype[np.bool_ | np.int_]],
        axis: SupportsIndex,
        dtype: None = ...,
        out: None = ...,
    ) -> npt.NDArray[np.int_]: ...
    @overload
    def sum(
        self: sparray[Any, np.dtype[np.unsignedinteger[Any]]],
        axis: SupportsIndex,
        dtype: None = ...,
        out: None = ...,
    ) -> npt.NDArray[np.unsignedinteger[Any]]: ...
    @overload
    def sum(
        self: sparray[Any, np.dtype[np.float_]],
        axis: SupportsIndex,
        dtype: None = ...,
        out: None = ...,
    ) -> npt.NDArray[np.float_]: ...
    @overload
    def sum(
        self: sparray[Any, np.dtype[np.complex_]],
        axis: SupportsIndex,
        dtype: None = ...,
        out: None = ...,
    ) -> npt.NDArray[np.complex_]: ...
    @overload
    def sum(
        self,
        axis: SupportsIndex,
        dtype: None = ...,
        out: None = ...,
    ) -> npt.NDArray[Any]: ...
    @overload
    def sum(
        self,
        axis: None = ...,
        dtype: _DTypeLike[_SCT] = ...,
        out: None = ...,
    ) -> _SCT: ...
    @overload
    def sum(
        self,
        axis: SupportsIndex,
        dtype: _DTypeLike[_SCT],
        out: None = ...,
    ) -> npt.NDArray[_SCT]: ...
    @overload
    def sum(
        self,
        axis: None,
        dtype: npt.DTypeLike,
        out: None = ...,
    ) -> Any: ...
    @overload
    def sum(
        self,
        axis: None = ...,
        *,
        dtype: npt.DTypeLike = ...,
        out: None = ...,
    ) -> Any: ...
    @overload
    def sum(
        self,
        axis: SupportsIndex,
        dtype: npt.DTypeLike,
        out: None = ...,
    ) -> npt.NDArray[Any]: ...
    @overload
    def sum(
        self,
        *,
        out: _ArrayType,
    ) -> _ArrayType: ...
    @overload
    def sum(
        self,
        axis: SupportsIndex | None = ...,
        *,
        out: _ArrayType,
    ) -> _ArrayType: ...
    @overload
    def sum(
        self,
        *,
        out: _ArrayType,
        dtype: npt.DTypeLike | None = ...,
    ) -> _ArrayType: ...
    @overload
    def sum(
        self,
        axis: SupportsIndex | None,
        dtype: npt.DTypeLike | None,
        out: _ArrayType,
    ) -> _ArrayType: ...
    @overload
    def trace(
        self: sparray[Any, np.dtype[np.bool_ | np.int_]],
        offset: SupportsIndex = ...,
    ) -> np.int_: ...
    @overload
    def trace(
        self: sparray[Any, np.dtype[np.unsignedinteger[Any]]],
        offset: SupportsIndex = ...,
    ) -> np.unsignedinteger[Any]: ...
    @overload
    def trace(
        self: sparray[Any, np.dtype[np.float_]],
        offset: SupportsIndex = ...,
    ) -> np.float_: ...
    @overload
    def trace(
        self: sparray[Any, np.dtype[np.complex_]],
        offset: SupportsIndex = ...,
    ) -> np.complex_: ...
    @overload
    def trace(self, offset: SupportsIndex = ...) -> Any: ...
    @overload
    def todense(
        self, order: _OrderType | None = ..., out: None = ...
    ) -> np.ndarray[_ShapeAnno, _DType_co]: ...
    @overload
    def todense(self, *, out: _ArrayType = ...) -> _ArrayType: ...
    @overload
    def todense(self, order: None, out: _ArrayType = ...) -> _ArrayType: ...
    def tocsr(self, copy: bool = ...) -> csr_array[_ShapeAnno, _DType_co]: ...
    def todok(self, copy: bool = ...) -> dok_array[_ShapeAnno, _DType_co]: ...
    def tocoo(self, copy: bool = ...) -> coo_array[_ShapeAnno, _DType_co]: ...
    def tolil(self, copy: bool = ...) -> lil_array[_ShapeAnno, _DType_co]: ...
    def todia(self, copy: bool = ...) -> dia_array[_ShapeAnno, _DType_co]: ...
    def tobsr(
        self,
        blocksize: tuple[SupportsIndex, SupportsIndex] | None = ...,
        copy: bool = ...,
    ) -> bsr_array[_ShapeAnno, _DType_co]: ...
    def tocsc(self, copy: bool = ...) -> csc_array[_ShapeAnno, _DType_co]: ...
    @overload
    def mean(
        self: (
            sparray[Any, np.dtype[np.bool_]]
            | sparray[Any, np.dtype[np.integer[Any]]]
            | sparray[Any, np.dtype[np.float_]]
        ),
        axis: None = ...,
        dtype: None = ...,
        out: None = ...,
    ) -> np.float_: ...
    @overload
    def mean(
        self: sparray[Any, np.dtype[np.complex_]],
        axis: None = ...,
        dtype: None = ...,
        out: None = ...,
    ) -> np.complex_: ...
    @overload
    def mean(self, axis: None = ..., dtype: None = ..., out: None = ...) -> Any: ...
    @overload
    def mean(
        self, axis: None = ..., *, dtype: _DTypeLike[_SCT], out: None = ...
    ) -> _SCT: ...
    @overload
    def mean(self, axis: None, dtype: _DTypeLike[_SCT], out: None = ...) -> _SCT: ...
    @overload
    def mean(
        self, axis: None = ..., *, dtype: npt.DTypeLike, out: None = ...
    ) -> Any: ...
    @overload
    def mean(self, axis: None, dtype: npt.DTypeLike, out: None = ...) -> Any: ...
    @overload
    def mean(
        self: (
            sparray[Any, np.dtype[np.bool_]]
            | sparray[Any, np.dtype[np.integer[Any]]]
            | sparray[Any, np.dtype[np.float_]]
        ),
        axis: SupportsIndex,
        dtype: None = ...,
        out: None = ...,
    ) -> npt.NDArray[np.float_] | np.float_: ...
    @overload
    def mean(
        self: sparray[Any, np.dtype[np.complex_]],
        axis: SupportsIndex,
        dtype: None = ...,
        out: None = ...,
    ) -> npt.NDArray[np.complex_] | np.complex_: ...
    @overload
    def mean(
        self, axis: SupportsIndex, dtype: _DTypeLike[_SCT], out: None = ...
    ) -> npt.NDArray[_SCT] | _SCT: ...
    @overload
    def mean(
        self,
        axis: SupportsIndex,
        dtype: npt.DTypeLike | None = ...,
        out: None = ...,
    ) -> Any: ...
    @overload
    def mean(
        self,
        *,
        out: _ArrayType,
    ) -> _ArrayType: ...
    @overload
    def mean(
        self,
        axis: SupportsIndex | None = ...,
        *,
        out: _ArrayType,
    ) -> _ArrayType: ...
    @overload
    def mean(
        self,
        *,
        dtype: npt.DTypeLike | None = ...,
        out: _ArrayType,
    ) -> _ArrayType: ...
    @overload
    def mean(
        self,
        axis: SupportsIndex | None,
        dtype: npt.DTypeLike | None,
        out: _ArrayType,
    ) -> _ArrayType: ...
    # In asformat, copy=False is not Type annotated, though is valid runtime value.
    # This is because the dynamic type change is not compatible with static type
    # checker.
    @overload
    def asformat(self, format: None, copy: bool) -> Self: ...
    @overload
    def asformat(
        self, format: Literal["csr"], copy: Literal[True]
    ) -> csr_array[_ShapeAnno, _DType_co]: ...
    @overload
    def asformat(
        self, format: Literal["dok"], copy: Literal[True]
    ) -> dok_array[_ShapeAnno, _DType_co]: ...
    @overload
    def asformat(
        self, format: Literal["coo"], copy: Literal[True]
    ) -> coo_array[_ShapeAnno, _DType_co]: ...
    @overload
    def asformat(
        self, format: Literal["lil"], copy: Literal[True]
    ) -> lil_array[_ShapeAnno, _DType_co]: ...
    @overload
    def asformat(
        self, format: Literal["dia"], copy: Literal[True]
    ) -> dia_array[_ShapeAnno, _DType_co]: ...
    @overload
    def asformat(
        self, format: Literal["bsr"], copy: Literal[True]
    ) -> bsr_array[_ShapeAnno, _DType_co]: ...
    @overload
    def asformat(
        self, format: Literal["csc"], copy: Literal[True]
    ) -> csc_array[_ShapeAnno, _DType_co]: ...
    @overload
    def asformat(
        self, format: Literal["array", "dense"]
    ) -> np.ndarray[_ShapeAnno, _DType_co]: ...
    @overload
    def asformat(
        self,
        format: _Formats | None,
        copy: Literal[True],
    ) -> sparray[_ShapeAnno, _DType_co]: ...
    # In reshape, copy=False annotating is problematic, but I decided to copy from
    # numpy where it is permitted to mutate the shape without changing the ShapeType
    # typevar.
    @overload
    def reshape(
        self,
        shape: _ShapeLike,
        /,
        *,
        order: _OrderType | None = ...,
        copy: bool = ...,
    ) -> sparray[Any, _DType_co]: ...
    @overload
    def reshape(
        self,
        *shape: SupportsIndex,
        order: _OrderType | None = ...,
        copy: bool = ...,
    ) -> sparray[Any, _DType_co]: ...
    @overload
    def astype(
        self,
        dtype: _DTypeLike[_SCT],
        casting: _CastingKind = ...,
        copy: bool = ...,
    ) -> sparray[Any, np.dtype[_SCT]]: ...
    @overload
    def astype(
        self,
        dtype: npt.DTypeLike,
        casting: _CastingKind = ...,
        copy: bool = ...,
    ) -> sparray[Any, Any]: ...
    @property
    def real(self) -> sparray[_ShapeAnno, np.dtype[Any]]: ...
    @property
    def imag(self) -> sparray[_ShapeAnno, np.dtype[Any]]: ...
    @overload
    def power(
        self,
        n: _NumberLike_co,
        dtype: None = ...,
    ) -> sparray[_ShapeAnno, np.dtype[Any]]: ...
    @overload
    def power(
        self,
        n: _NumberLike_co,
        dtype: _DTypeLike[_SCT],
    ) -> sparray[_ShapeAnno, np.dtype[_SCT]]: ...
    @overload
    def power(
        self,
        n: _NumberLike_co,
        dtype: npt.DTypeLike,
    ) -> sparray[_ShapeAnno, np.dtype[Any]]: ...
    def __abs__(self) -> sparray[_ShapeAnno, Any]: ...
    @overload
    def __round__(
        self: sparray[Any, np.dtype[np.bool_]],
        ndigits: SupportsIndex = ...,
    ) -> sparray[_ShapeAnno, np.dtype[np.float16]]: ...
    @overload
    def __round__(
        self: sparray[Any, np.dtype[np.complex_ | np.object_]],
        ndigits: SupportsIndex = ...,
    ) -> sparray[_ShapeAnno, np.dtype[Any]]: ...
    @overload
    def __round__(
        self: sparray[Any, np.dtype[_SCT_uifcO]],
        ndigits: SupportsIndex = ...,
    ) -> sparray[_ShapeAnno, np.dtype[_SCT_uifcO]]: ...
    @overload
    def __round__(
        self,
        ndigits: SupportsIndex = ...,
    ) -> sparray[_ShapeAnno, np.dtype[Any]]: ...
    # TODO: The return type here can be refined
    def __add__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __radd__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __sub__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __rsub__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __matmul__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __rmatmul__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __truediv__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __div__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __rtruediv__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __rdiv__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __iadd__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __isub__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __imul__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __idiv__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __itruediv__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...

    # TODO: the `T` and `transpose` methods need refinement.csc -> csr anything else?
    # Despite T and transpose (if copy=False) by default mutate the shape of self, and
    # can cause incompatibility with the ShapeType variable, I followed numpy's
    # approach and allowed this.
    @property
    def T(self) -> sparray[Any, _DType_co]: ...
    def transpose(
        self, axes: None = ..., copy: bool = ...
    ) -> sparray[Any, _DType_co]: ...
    # TODO: the type annotations of multiply, maximum, minimum and dot can be refined by
    # defining them per-final sparse class, but for now I leave them quite general
    def multiply(self, other: npt.ArrayLike | SparseArray[Any]) -> SparseArray[Any]: ...
    def maximum(self, other: npt.ArrayLike | SparseArray[Any]) -> SparseArray[Any]: ...
    def minimum(self, other: npt.ArrayLike | SparseArray[Any]) -> SparseArray[Any]: ...
    def dot(
        self, other: npt.ArrayLike | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...

    # sparray format can be any value of its subclasses, which I leave as str
    @property
    def format(self) -> str: ...

    ###########################################################################
    # dunder methods that are different in sparray and spmatrix
    ###########################################################################
    def __mul__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __rmul__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __pow__(self, n: _NumberLike_co) -> sparray[_ShapeAnno, np.dtype[Any]]: ...

def issparse(x: Any) -> TypeIs[SparseArray[Any]]: ...
def isspmatrix(x: Any) -> TypeIs[spmatrix[Any, Any]]: ...
