# These are convenience typing objects that exist only at static type checking time.
# If use they should be imported conditionally, like so:
# ```python
# if TYPE_CHECKING:
#     from scipy.sparse._typing import _DType_co
# ```

from collections.abc import Callable, Sequence
from types import EllipsisType
from typing import (
    Any,
    Literal,
    Protocol,
    SupportsIndex,
    SupportsInt,
    TypeAlias,
)
from typing_extensions import TypeVar

import numpy as np
from numpy import typing as npt
from numpy._typing._array_like import _ArrayLike as _ArrayLike
from numpy._typing._array_like import _ArrayLikeInt_co as _ArrayLikeInt_co
from numpy._typing._array_like import _SupportsArray
from numpy._typing._array_like import _SupportsArrayFunc as _SupportsArrayFunc
from numpy._typing._scalars import _BoolLike_co as _BoolLike_co
from numpy._typing._scalars import _IntLike_co as _IntLike_co
from numpy._typing._scalars import _ScalarLike_co as _ScalarLike_co

from ._base import sparray
from ._matrix import spmatrix

_SCT = TypeVar("_SCT", bound=np.generic)
_SCT_co = TypeVar("_SCT_co", covariant=True, bound=np.generic)

_ShapeAnno = TypeVar("_ShapeAnno", default=Any)
_DType_co = TypeVar(
    "_DType_co", covariant=True, bound=np.dtype[Any], default=np.dtype[Any]
)
_DType = TypeVar("_DType", bound=np.dtype[Any])
# TODO: remove _T ?
_T = TypeVar("_T", default=Any)
_T_co = TypeVar("_T_co", default=Any, covariant=True)
_Formats: TypeAlias = Literal["csc", "csr", "coo", "bsr", "dia", "dok", "lil"]

_ArrayType = TypeVar("_ArrayType", bound=npt.NDArray[Any])
_MatrixType = TypeVar("_MatrixType", bound=np.matrix[Any, np.dtype[Any]])

_SCT_uifcO = TypeVar("_SCT_uifcO", bound=np.number[Any] | np.object_)

_CastingKind: TypeAlias = Literal["no", "equiv", "safe", "same_kind", "unsafe"]
_OrderType: TypeAlias = Literal["C", "F"]

_DTypeLike: TypeAlias = np.dtype[_SCT] | type[_SCT] | _SupportsDType[np.dtype[_SCT]]
_NumberLike_co: TypeAlias = int | float | complex | np.number[Any] | np.bool_
_ShapeLike: TypeAlias = SupportsIndex | Sequence[SupportsIndex]

class _SupportsDType(Protocol[_DType_co]):
    @property
    def dtype(self) -> _DType_co: ...
    def astype(self, dtype: npt.DTypeLike) -> _SupportsDType[Any]: ...

SparseArray: TypeAlias = (
    sparray[Any, np.dtype[_SCT_co]] | spmatrix[Any, np.dtype[_SCT_co]]
)

_ArrayLike1DDual: TypeAlias = _SupportsArray[_DType_co] | Sequence[_T_co]
_ArrayLike1DIndex: TypeAlias = _ArrayLike1DDual[np.dtype[np.int_], SupportsIndex]
_SliceLike: TypeAlias = (
    None
    | SupportsIndex
    | npt.NDArray[np.bool_]
    | npt.NDArray[np.integer[Any]]
    | slice
    | EllipsisType
    | npt.ArrayLike
)

DataRVsType: TypeAlias = Callable[[SupportsInt], npt.NDArray[Any]]

class DataSamplerType(Protocol):
    def __call__(self, size: SupportsInt) -> npt.NDArray[Any]: ...
