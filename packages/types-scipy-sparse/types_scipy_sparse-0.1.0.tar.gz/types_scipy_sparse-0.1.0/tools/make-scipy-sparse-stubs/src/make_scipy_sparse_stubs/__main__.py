"""
Creates the type annotations for the scipy.sparse module.
These annotations are written from templates in order to avoid repetition and
to ensure consistency across the different classes.
"""

import argparse
import difflib
import importlib.resources
import itertools
import os
import traceback
from collections.abc import Sequence
from typing import Literal

from make_scipy_sparse_stubs import annotation_snippets

ANNOTATION_SNIPPETS = importlib.resources.files(annotation_snippets)
SPARSE_TYPE_TO_DENSE_TYPE = {"sparray": "np.ndarray", "spmatrix": "np.matrix"}
CONSTRUCT_FUNCS = (
    "spdiags",
    "diags_array",
    "diags",
    "identity",
    "eye_array",
    "eye",
    "kron",
    "kronsum",
    "hstack",
    "vstack",
    "bmat",
    "block_array",
    "block_diag",
    "random_array",
    "random",
    "rand",
)
EXTRACT_FUNCS = ("tril", "triu")


def _indent_line(line: str, spaces: int = 4) -> str:
    if not line:
        return ""
    if line == "\n":
        return "\n"
    return " " * spaces + line


def _get_commons(commons: str) -> str:
    """Append the common type annotations to the given text."""
    txt = ""
    with (
        (ANNOTATION_SNIPPETS / "class_commons" / commons)
        .with_suffix(".txt")
        .open() as f
    ):
        for line in f.readlines():
            txt += _indent_line(line)
    return txt


def _get_func_snippet(func_name: str, module: str) -> str:
    """Append the common type annotations to the given text."""
    with (ANNOTATION_SNIPPETS / module / func_name).with_suffix(".txt").open() as f:
        return f.read()


def _get_sparray_spmatrix_body(tp: Literal["sparray", "spmatrix"]) -> str:
    """
    Return class body annotations for sparray / spmatrix that are ``inherited''
    from _spbase.
    """
    body = _get_commons("spbase_commons")
    return body.format(
        _Sparse_Type=tp,
        _sparse_suffix=tp[2:],
        _Self_Base=tp,
        _Dense_Type=SPARSE_TYPE_TO_DENSE_TYPE[tp],
    )


def make__base() -> str:
    """Return the content of _base.pyi."""
    with (ANNOTATION_SNIPPETS / "module_templates" / "_base_template.txt").open() as f:
        module = f.read()
    return module.format(cls_body=_get_sparray_spmatrix_body("sparray"))


def make__matrix() -> str:
    """Return the content of _matrix.pyi."""
    with (
        ANNOTATION_SNIPPETS / "module_templates" / "_matrix_template.txt"
    ).open() as f:
        module = f.read()
    return module.format(cls_body=_get_sparray_spmatrix_body("spmatrix"))


def _get_csc_csr_body(
    tp: Literal["array", "matrix"], format_: Literal["csr", "csc"]
) -> str:
    """Return the class body for csc_array, csr_array, csr_matrix or csc_matrix."""
    commons = (
        "spbase_commons",
        "cs_matrix_init",
        "cs_matrix_commons",
        "data_matrix_commons",
        "minmax_mixin_commons",
    )
    body = "".join(map(_get_commons, commons))
    return body.format(
        _Self_Base=format_ + "_" + tp,
        _Sparse_Type="sp" + tp,
        _sparse_suffix=tp,
        _Dense_Type=SPARSE_TYPE_TO_DENSE_TYPE["sp" + tp],
    )


def make__csc() -> str:
    """Return the content of _csc.pyi."""
    with (ANNOTATION_SNIPPETS / "module_templates" / "_csc_template.txt").open() as f:
        module = f.read()
    return module.format(
        array_body=_get_csc_csr_body("array", "csc")[:-1],
        matrix_body=_get_csc_csr_body("matrix", "csc")[:-1],
    )


def make__csr() -> str:
    """Return the content of _csr.pyi."""
    with (ANNOTATION_SNIPPETS / "module_templates" / "_csr_template.txt").open() as f:
        module = f.read()
    return module.format(
        array_body=_get_csc_csr_body("array", "csr")[:-1],
        matrix_body=_get_csc_csr_body("matrix", "csr")[:-1],
    )


def _get_bsr_body(tp: Literal["array", "matrix"]) -> str:
    """Return the class body for bsr_array or bsr_matrix."""
    commons = (
        "spbase_commons",
        "bsr_base_commons",
        "cs_matrix_commons",
        "data_matrix_commons",
        "minmax_mixin_commons",
    )
    body = "".join(map(_get_commons, commons))
    return body.format(
        _Self_Base="bsr_" + tp,
        _Sparse_Type="sp" + tp,
        _sparse_suffix=tp,
        _Dense_Type=SPARSE_TYPE_TO_DENSE_TYPE["sp" + tp],
    )


def make__bsr() -> str:
    """Return the content of _bsr.pyi."""
    with (ANNOTATION_SNIPPETS / "module_templates" / "_bsr_template.txt").open() as f:
        module = f.read()
    return module.format(
        array_body=_get_bsr_body("array")[:-1],
        matrix_body=_get_bsr_body("matrix")[:-1],
    )


def _get_coo_body(tp: Literal["array", "matrix"]) -> str:
    """Return the class body for coo_array or coo_matrix."""
    commons = (
        "spbase_commons",
        "coo_base_commons",
        "data_matrix_commons",
        "minmax_mixin_commons",
    )
    body = "".join(map(_get_commons, commons))
    return body.format(
        _Self_Base="coo_" + tp,
        _Sparse_Type="sp" + tp,
        _sparse_suffix=tp,
        _Dense_Type=SPARSE_TYPE_TO_DENSE_TYPE["sp" + tp],
    )


def make__coo() -> str:
    """Return the content of _coo.pyi."""
    with (ANNOTATION_SNIPPETS / "module_templates" / "_coo_template.txt").open() as f:
        module = f.read()
    return module.format(
        array_body=_get_coo_body("array")[:-1],
        matrix_body=_get_coo_body("matrix")[:-1],
    )


def _get_dia_body(tp: Literal["array", "matrix"]) -> str:
    """Return the class body for dia_array or dia_matrix."""
    commons = (
        "spbase_commons",
        "dia_base_commons",
        "data_matrix_commons",
    )
    body = "".join(map(_get_commons, commons))
    return body.format(
        _Self_Base="dia_" + tp,
        _Sparse_Type="sp" + tp,
        _sparse_suffix=tp,
        _Dense_Type=SPARSE_TYPE_TO_DENSE_TYPE["sp" + tp],
    )


def make__dia() -> str:
    """Return the content of _dia.pyi."""
    with (ANNOTATION_SNIPPETS / "module_templates" / "_dia_template.txt").open() as f:
        module = f.read()
    return module.format(
        array_body=_get_dia_body("array")[:-1],
        matrix_body=_get_dia_body("matrix")[:-1],
    )


def _get_dok_body(tp: Literal["array", "matrix"]) -> str:
    """Return the class body for dok_array or dok_matrix."""
    commons = (
        "spbase_commons",
        "dok_base_commons",
    )
    body = "".join(map(_get_commons, commons))
    return body.format(
        _Self_Base="dok_" + tp,
        _Sparse_Type="sp" + tp,
        _sparse_suffix=tp,
        _Dense_Type=SPARSE_TYPE_TO_DENSE_TYPE["sp" + tp],
    )


def make__dok() -> str:
    """Return the content of _dok.pyi."""
    with (ANNOTATION_SNIPPETS / "module_templates" / "_dok_template.txt").open() as f:
        module = f.read()
    return module.format(
        array_body=_get_dok_body("array")[:-1],
        matrix_body=_get_dok_body("matrix")[:-1],
    )


def _get_lil_body(tp: Literal["array", "matrix"]) -> str:
    """Return the class body for lil_array or lil_matrix."""
    commons = (
        "spbase_commons",
        "lil_base_commons",
    )
    body = "".join(map(_get_commons, commons))
    return body.format(
        _Self_Base="lil_" + tp,
        _Sparse_Type="sp" + tp,
        _sparse_suffix=tp,
        _Dense_Type=SPARSE_TYPE_TO_DENSE_TYPE["sp" + tp],
    )


def make__lil() -> str:
    """Return the content of _lil.pyi."""
    with (ANNOTATION_SNIPPETS / "module_templates" / "_lil_template.txt").open() as f:
        module = f.read()
    return module.format(
        array_body=_get_lil_body("array")[:-1],
        matrix_body=_get_lil_body("matrix")[:-1],
    )


def _make_func(func_name: str, module: str) -> str:
    txt = ""
    match func_name:
        case (
            "spdiags"
            | "identity"
            | "eye"
            | "diags"
            | "hstack"
            | "vstack"
            | "bmat"
            | "block_array"
            | "block_diag"
        ):
            txt += _get_func_snippet(func_name + "_default", module)
            for fmt in ["csc", "csr", "coo", "bsr", "dia", "dok", "lil"]:
                txt += _get_func_snippet(func_name, module).format(_Spec_Format=fmt)
        case "diags_array" | "eye_array":
            for fmt in ["csc", "csr", "coo", "bsr", "dia", "dok", "lil"]:
                opt_none = " | None = ..." if fmt == "dia" else ""
                txt += _get_func_snippet(func_name, module).format(
                    _Spec_Format=fmt, _Opt_None=opt_none
                )
        case "random_array":
            for fmt in ["csc", "csr", "coo", "bsr", "dia", "dok", "lil"]:
                opt_none = " | None = ..." if fmt == "coo" else ""
                txt += _get_func_snippet(func_name, module).format(
                    _Spec_Format=fmt, _Opt_None=opt_none
                )
        case "random" | "rand":
            txt += _get_func_snippet(func_name + "_default", module)
            # "coo" is included in default case
            for fmt in ["csc", "csr", "bsr", "dia", "dok", "lil"]:
                txt += _get_func_snippet(func_name, module).format(_Spec_Format=fmt)
        case "kron" | "kronsum":
            array_ol = ""
            matrix_ol = ""
            for fmt in ["csc", "csr", "coo", "bsr", "dia", "dok", "lil"]:
                array_ol += _get_func_snippet(func_name + "_array", module).format(
                    _Spec_Format=fmt
                )
                matrix_ol += _get_func_snippet(func_name + "_matrix", module).format(
                    _Spec_Format=fmt
                )
            # remove last newlines if present
            array_ol = array_ol.rstrip("\n")
            matrix_ol = matrix_ol.rstrip("\n")
            txt += _get_func_snippet(func_name + "_template", module).format(
                sparray_overloads=array_ol,
                spmatrix_overloads=matrix_ol,
            )
        # TODO: make tril / triu compatible with random / rand:
        case "tril" | "triu":
            # "coo" is included in default case
            for fmt in ["csc", "csr", "bsr", "dia", "dok", "lil"]:
                txt += _get_func_snippet(func_name, module).format(_Spec_Format=fmt)

        case _:
            raise ValueError(f"Invalid function name {func_name}")
    return txt


def make__construct() -> str:
    """Return the content of _construct.pyi."""
    with (
        ANNOTATION_SNIPPETS / "module_templates" / "_construct_template.txt"
    ).open() as f:
        module = f.read()
    body = ""
    for func_name in CONSTRUCT_FUNCS:
        body += _make_func(func_name, "construct")
    return module.format(body=body)[:-1]


def make__extract() -> str:
    """Return the content of _extract.pyi."""
    with (
        ANNOTATION_SNIPPETS / "module_templates" / "_extract_template.txt"
    ).open() as f:
        module = f.read()
    overloads = {}
    for func_name in EXTRACT_FUNCS:
        overloads[func_name] = _make_func(func_name, "extract")
    return module.format(**overloads)[:-1]


GENERATING_FUNCS = {
    "_base.pyi": make__base,
    "_matrix.pyi": make__matrix,
    "_csc.pyi": make__csc,
    "_csr.pyi": make__csr,
    "_coo.pyi": make__coo,
    "_bsr.pyi": make__bsr,
    "_dia.pyi": make__dia,
    "_dok.pyi": make__dok,
    "_lil.pyi": make__lil,
    "_construct.pyi": make__construct,
    "_extract.pyi": make__extract,
}


def make_stubs(
    verbose: bool = False,
    check_only: bool = False,
    stub_path: str | None = None,
    filenames: Sequence[str] = tuple(GENERATING_FUNCS),
) -> bool:
    """
    Write the type annotations to the scipy-stubs package.

    :param verbose: If True, print the diff of the changes.
    :param check_only: If True, do not write the changes to the files.
    :return: True if generated stubs are different from the existing ones,
     else False.
    """
    if set(filenames).difference(GENERATING_FUNCS):
        raise ValueError(
            f"Invalid filenames provided. Valid filenames are "
            f"{list(GENERATING_FUNCS)}"
        )
    if stub_path is None:
        if not check_only:
            raise ValueError(
                "If `check_only` is false a path to 'scipy-stubs' dir must be supplied"
            )
        try:
            sparse_stubs_path = importlib.resources.files("scipy-stubs") / "sparse"
        except ModuleNotFoundError as e:
            raise ModuleNotFoundError(
                e.msg + ", try non-editable install of scipy-stubs "
            ) from None
    else:
        sparse_stubs_path = os.path.join(stub_path, "sparse")
        if not os.path.isdir(sparse_stubs_path):
            raise FileNotFoundError(f"No such file or directory: {sparse_stubs_path!r}")

    found_diff = False
    for fname in filenames:
        stub_gen_func = GENERATING_FUNCS[fname]
        try:
            new_stub_file = stub_gen_func()
        except Exception as e:
            raise RuntimeError(f"Error while generating {fname}") from e
        try:
            with open(os.path.join(sparse_stubs_path, fname), encoding="utf-8") as f:
                existing_stub_lines = f.readlines()
        except FileNotFoundError:
            existing_stub_lines = None
        if existing_stub_lines is not None:
            # compare the existing with new file, if no differences, continue
            diff = difflib.unified_diff(
                existing_stub_lines, new_stub_file.splitlines(keepends=True)
            )
            try:
                first_diff_line = next(diff)
            except StopIteration:
                # No differences
                continue
            diff = itertools.chain([first_diff_line], diff)
            found_diff = True
            header = "Found a difference in" if check_only else "Changing"
            header += f" {fname}"
        else:
            diff = iter(())
            found_diff = True
            header = "Found missing" if check_only else "Creating new"
            header += f" file {fname}"

        print(header)
        if verbose:
            print("=" * len(header))
            print("".join(diff))
        if not check_only:
            with open(
                os.path.join(sparse_stubs_path, fname), "w", encoding="utf-8"
            ) as f:
                f.write(new_stub_file)
    return found_diff


def _is_dir_path(string: str) -> str:
    if os.path.isdir(string):
        return string
    raise NotADirectoryError(string)


def main() -> int:
    """Parse the command line arguments and run the script"""
    parser = argparse.ArgumentParser(
        description=("Create the type annotations for the 'scipy.sparse' module.")
    )
    parser.add_argument(
        "-c",
        "--check",
        help=(
            "don't write the files back, just check for differences;"
            "return 0 if no changes were required, 1 if found difference "
            "between the generated and the new files, and 123 if an internal "
            "error occurred."
        ),
        action="store_true",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        help="emit changed line differences",
        action="store_true",
    )
    parser.add_argument(
        "-f",
        "--files",
        help=f"specify files, options: {', '.join(GENERATING_FUNCS)}",
        choices=list(GENERATING_FUNCS),
        default=list(GENERATING_FUNCS),
        metavar="filename",
        dest="files",
        nargs="+",
    )
    parser.add_argument(
        "-sp",
        "--stub-path",
        type=_is_dir_path,
        help=(
            "Path to the scipy-stubs package files. If not provided, the path is "
            "found from installed 'scipy-stubs' package. For overriding files this "
            "parameter must be supplied. When in workspace root use 'src/scipy-stubs'."
            "Can also be input via env variable SCIPY_SPARSE_STUBS_PATH."
        ),
    )
    args = parser.parse_args()
    if args.stub_path is None:
        args.stub_path = os.environ.get("SCIPY_SPARSE_STUBS_PATH")
    if args.check is False and args.stub_path is None:
        print(
            "Cannot modify stub files without specifying the STUB_PATH.\n"
            "Either set run with --check to compare with installed types package or "
            "supply path with --stub-path STUB_PATH.\n"
            "Run with --help for more details."
        )
        return 1
    try:
        changed = make_stubs(
            verbose=args.verbose,
            check_only=args.check,
            stub_path=args.stub_path,
            filenames=args.files,
        )

    except Exception as e:  # pylint: disable=broad-exception-caught
        print("Something went wrong! 💣💣💣")
        if args.verbose:
            print(traceback.format_exc())
        else:
            print(
                f"Encountered error: {e}\n"
                "For full tracestack run with make_scipy_sparse_stubs --verbose"
            )
        return 123

    fin_msg = "Finished"
    if not changed or args.check:
        fin_msg += " without any changes"
    if not changed:
        fin_msg += " 🎉"
    print(fin_msg)
    if args.check:
        return changed
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
