import os
from typing import Any, Protocol, TypeVar

from .typing import SparseArray

__all__ = ["save_npz", "load_npz"]

_CharType_contra = TypeVar("_CharType_contra", str, bytes, contravariant=True)
_CharType_co = TypeVar("_CharType_co", str, bytes, covariant=True)

class _SupportsWrite(Protocol[_CharType_contra]):
    def write(self, s: _CharType_contra, /) -> object: ...

class _SupportsReadSeek(Protocol[_CharType_co]):
    def read(self, n: int, /) -> _CharType_co: ...
    def seek(self, offset: int, whence: int, /) -> object: ...

def save_npz(
    file: str | os.PathLike[str] | _SupportsWrite[bytes],
    matrix: SparseArray[Any],
    compressed: bool = ...,
) -> None: ...
def load_npz(
    file: str | bytes | os.PathLike[Any] | _SupportsReadSeek[bytes],
) -> SparseArray[Any]: ...
