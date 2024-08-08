# Type annotations types-package for `scipy.sparse`

This is a [PEP-561](https://peps.python.org/pep-0561/) compilant type information package for the `sparse` module of the [`SciPy`](https://scipy.org/) package.
Installing this package will allow [`mypy`](https://mypy.readthedocs.io/en/latest/installed_packages.html) and possibly other static type checkers (e.g., pyright) to recognize type annotations for `scipy.sparse` classes and functions.


> [!CAUTION]
> This package is a work in progress, and while it is tests the test coverage is still lacking (see this issue https://github.com/BarakKatzir/types-scipy-sparse/issues/6 ).
> 
> Currently the `csgraph` and `linalg` submodules are not type annotated (see issue https://github.com/BarakKatzir/types-scipy-sparse/issues/5).
> 
> This package only supports `"numpy <2.0.0"` for now (see issue https://github.com/BarakKatzir/types-scipy-sparse/issues/7).

## Installation

In your python environment run

```bash
pip install types-scipy-sparse
```

## Annotations

The basic annotations work fine. For example, if we have the file `important_func.py`

```python
# content of important_func.py
from scipy.sparse import coo_array

def make_sparse(
    x: list[int], y: list[int], vals: list[float]
) -> csr_array:
    return coo_array((vals, (x, y))).tocsr()

```

it will pass a mypy check

```console
$ mypy important_func.py
Success: no issues found in 1 source file
```

### `numpy`-flavored generics

The different sparse array and sparse matrix classes are type annotated similarly to `numpy.ndarray`s, with two `TypeVar`s: `<sparse_class>[ShapeType, DType]`, for example `csc_array[Any, numpy.float32]`. As for `numpy.ndarray`, the `DType` is bound by `numpy.dtype[Any]` and the `ShapeType` can be anything.

For example,

```python
# content of important_script.py
import numpy
from scipy.sparse import csr_array, lil_array

x = csr_array([[0, 1], [2, 0]], dtype=numpy.float64)
y = lil_array(numpy.array([[0, 1], [2, 0]], dtype=numpy.float32))
reveal_locals()

```

passes mypy with the revealed types of the `x` and `y` arrays

```console
$ mypy important_script.py
important_script.py:6: note: Revealed local types are:
important_script.py:6: note:     x: scipy.sparse._csr.csr_array[Any, numpy.dtype[numpy.floating[numpy._typing._64Bit]]]
important_script.py:6: note:     y: scipy.sparse._lil.lil_array[Any, numpy.dtype[numpy.floating[numpy._typing._32Bit]]]
Success: no issues found in 1 source file
```

As in numpy, the first type variable, `ShapeType`, is left for user customization.

Note that for compatibility with any other type packages, The `ShapeType` and `DType` type variables default to `Any`, using the [PEP-696](https://peps.python.org/pep-0696/) feature. This means that type annotatin `x: dok_array` will implicitly insert these `Any`s:

```console
$ mypy -c "import scipy.sparse as sp; x: sp.dok_array; reveal_type(x)"
<string>:1: note: Revealed type is "scipy.sparse._dok.dok_array[Any, numpy.dtype[Any]]"
Success: no issues found in 1 source file
```

> [!NOTE]
> Since these generics are only introduced in the type stubs, they will raise an error at runtime. Thus, `x: coo_array[Any, numpy.dtype[numpy.uint8]]` will raise an error.
> If you desire to use this feature when annotating `.py` files then there are two easy solutions:
> 
> * Use implicit forward references by adding `from __future__ import annotations` at the top of your script
> 
> * Use explicit forward references by putting troublesome annotations in quotation marks, e.g., `x: "coo_array[Any, numpy.dtype[numpy.uint8]]"`


### Type narrowing functions

There are several convenience type-narrowing functions in the `sparse` module, e.g., `issparse`, `isspmatrix` and `isdense`. These are annotated with the `TypeIs` introduced in [PEP-742](https://peps.python.org/pep-0742/). This conveniently narrows the type (and not casts to it, like `typing.TypeGuard`) and allows type narrowing in both `if` and `else` branches of a conditional.

For example the python file

```python
# content of my_script.py
from typing import Any

import numpy
from scipy.sparse import csr_array, issparse

x: numpy.ndarray[Any, Any] | csr_array
if issparse(x):
    reveal_type(x)
    # attribute of csr_array
    x.indptr
elif isinstance(x, numpy.ndarray):
    # attribute of ndarray
    reveal_type(x)
    x.strides
else:
    # This branch is inferred to be unreachable
    # so mypy ignores the following
    reveal_type(x)
    x.mystery_attribute

```

will pass mypy with the correct revealed types

```console
$ mypy my_script.py
my_script.py:8: note: Revealed type is "scipy.sparse._csr.csr_array[Any, numpy.dtype[Any]]"
my_script.py:12: note: Revealed type is "numpy.ndarray[Any, Any]"
Success: no issues found in 1 source file
```

### The `sparray` and `spmatrix` namespace classes

The classes `sparray` and `spmatrix` have empty bodies and are used for mainly for namespacing and `isinstance` checks, while the many sparse array/matrix class' methods are implemented via private mixin classes. While the private classes are not type annotated by this types package, the sparray and spmatrix are conveniantly type annotated as `Protocol[ShapeType, DType]`, this way it is conveyed to the type-checker that any methods they carry (such as `sum` and `asformat`) is not implemented, while still stating what method theri subclasses do implement.


### New `scipy.sparse.typing`

This type package introduces a new `scipy.sparse.typing` module for convenience. This new module is used internally for common type aliases and it exposes the `SparseArray` type alias which can specify a sparse array or sparse matrix by its scalar type similarly to `numpy`'s `numpy.typing.NDArray` (a scalar type is the subtype of the `numpy.generic`, e.g., `numpy.int8` and `numpy.complex128`),

```python
_SCT_co = TypeVar("_SCT_co", covariant=True, bound=numpy.generic)
SparseArray: TypeAlias = (
    sparray[Any, numpy.dtype[_SCT_co]] | spmatrix[Any, numpy.dtype[_SCT_co]]
)
```

For example, the following passes mypy

```python
from __future__ import annotations

from typing import TYPE_CHECKING
import numpy

if TYPE_CHECKING:
    from scipy.sparse.typing import SparseArray

def foo(x: SparseArray[numpy.float64]) -> None:
    print(f"doing serious calculations with {x}")

```

> [!NOTE]
> `SparseArray` cannot be used in runtime so it's best to use it in forward references (see above explanation for more)

### What is and what isn't annotated?

I aim to annotate all the public object of `scipy.sparse`, see https://github.com/BarakKatzir/types-scipy-sparse/issues/5 for track of missing types. However, most of the private objects are left untyped (the private functions/classes/methods are those whose name begin with `'_'` and do not end with `'_'`, or that they reside in a private module and are not re-exported in a public module). There are a few exceptions to this that I keep track of here.

Currently, there are only two expections to the above rule: the function `_todata` and function `_ravel_coords` that seems useful and well docstringed.

Another thing to point out is that the whole *private* module `scipy.sparse._sparsetools` is not exposed in `sparse`'s `__init__.py`, but some of its functions are re-exposed by some deprecated modules such as `bsr.py`, `compressed.py`, `construct.py` and some others. As such, the `_sparsetools` module is typed in this package, but it would be prudent to not rely on these stubs.

## Development

### Development environment setup

The current development environment uses the experimental `uv` package.

Here are a few steps for anyone to set up the development environment quickly:

1) clone that package

2) [install uv](https://docs.astral.sh/uv/installation/) (consider fixing the version of `uv` to that of this repo)

In workspace root, create virtual environment

  ```bash
  uv venv -p 3.10 --python-preference managed
  ```

  and activate the venv (e.g., run `source .venv/bin/activate` if in a linux terminal).

3) To install dependencies run

  ```bash
  uv sync --frozen
  ```

4) to make sure the type package is correctly installed, install in **non-editable** mode

  ```bash
  uv pip install . --no-deps
  ```

> [!NOTE]
> If you plan to change the version of `uv`, know that it is fixed separately in different places as the `uv` command is run separately in different environments: the dev venv, tox venvs, when building wheels, and in github workflows

### Type stub generation

A big portion of the stub files are generated by code from common templates, since the scipy sparse module has a lot of similar classes with common functionality and common inheritance.
The repository includes the stub generating CLI tool named `make-scipy-sparse-stubs`. The tool can be installed as a package in editable mode (with the `uv sync` command or with `uv pip install -e make-scipy-sparse-stubs@tools/make-scipy-sparse-stubs`). It contains the python module `make_scipy_sparse_stubs` which can be run to either generate the type stubs or to check that the present / installed type stubs are in sync.

To check that the stubs are in sync with the generated stubs run

```console
$ python -m make_scipy_sparse_stubs --check
Finished without any changes 🎉
```

or to overwrite the current stubs by specifying their location in the workspace

```console
$ python -m make_scipy_sparse_stubs -sp src/scipy-stubs
Finished without any changes 🎉
```

For more on the tool, see it's help:

```bash
python -m make_scipy_sparse_stubs --help
```

> [!WARNING]
> The tool's functionality and interface can change between different revisions of the repository.

### Tests

Pull requests to `main` are automatically run through tests, so you can develop locally and push to main and see if it passes. You can run the tests locally by running `tox` before pushing

```bash
uv run tox
```

or if you activated the venv, then simply run `tox`.

The stubs are tested for:

* type stubs match the generated `make_scipy_sparse_stubs` tool

* `ruff` formatters and checkers

* `mypy` and mypy's `stubtest`

* `pytest` examines mypy failure / pass / reveal on example code (the template for these tests was adapted from the now archived `numpy-stubs` repo (see https://github.com/numpy/numpy-stubs)
