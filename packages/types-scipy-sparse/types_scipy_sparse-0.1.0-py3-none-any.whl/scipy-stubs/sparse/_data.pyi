from collections.abc import Callable
from typing import Any

__all__: list[str] = []

# `data.pyi` explicitly re-exports the following
npfunc: Callable[..., Any]
name: str
