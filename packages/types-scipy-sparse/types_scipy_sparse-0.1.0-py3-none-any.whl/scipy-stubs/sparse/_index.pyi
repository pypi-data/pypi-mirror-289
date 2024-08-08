from collections.abc import Sequence
from typing import Any, SupportsIndex, overload

import numpy as np

from ._base import sparray
from ._matrix import spmatrix
from .typing import (
    SparseArray,
    _BoolLike_co,
    _DType_co,
    _IntLike_co,
    _SCT_co,
    _SliceLike,
)

INT_TYPES: tuple[type[Any], ...]

class IndexMixin:
    # getitem calls _get_arrayXarray
    # TODO: check that _get_arrayXarray acts like this in all sparse cls-s:
    # [V] csr, [ ] csc, [ ] coo, [ ] dok, [ ] lil, [ ] bsr, [ ] dia
    @overload
    def __getitem__(
        self: sparray[Any, _DType_co],
        key: (
            Sequence[Sequence[_BoolLike_co]]
            | SparseArray[np.bool_]
            | tuple[Sequence[_IntLike_co], Sequence[_IntLike_co]]
        ),
    ) -> np.ndarray[Any, _DType_co]: ...
    @overload
    def __getitem__(
        self: spmatrix[Any, _DType_co],
        key: (
            Sequence[Sequence[_BoolLike_co]]
            | SparseArray[np.bool_]
            | tuple[Sequence[_IntLike_co], Sequence[_IntLike_co]]
        ),
    ) -> np.matrix[Any, _DType_co]: ...
    # getitem calls _get_intXint:
    @overload
    def __getitem__(
        self: sparray[Any, np.dtype[_SCT_co]],
        key: tuple[SupportsIndex, SupportsIndex],
    ) -> _SCT_co: ...
    @overload
    def __getitem__(
        self: spmatrix[Any, np.dtype[_SCT_co]],
        key: tuple[SupportsIndex, SupportsIndex],
    ) -> _SCT_co: ...
    # all else
    # TODO: cant it be tuple[_Slicelike, ...]?
    @overload
    def __getitem__(self, key: _SliceLike | tuple[_SliceLike, _SliceLike]) -> Any: ...
    def __setitem__(
        self,
        key: _SliceLike | tuple[_SliceLike, _SliceLike],
        value: Any,
    ) -> None: ...
