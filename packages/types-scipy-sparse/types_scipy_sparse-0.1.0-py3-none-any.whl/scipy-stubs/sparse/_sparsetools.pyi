from typing import Any, NoReturn, SupportsIndex, overload

import numpy as np
import numpy.typing as npt

from .typing import _SCT_co

def bsr_diagonal(
    k: SupportsIndex,
    n_brow: SupportsIndex,
    n_bcol: SupportsIndex,
    R: SupportsIndex,
    C: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[Any],
    Yx: npt.NDArray[Any],  # output
    /,
) -> None: ...
def bsr_eldiv_bsr(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    R: SupportsIndex,
    C: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],
    Bp: npt.NDArray[np.int_],
    Bj: npt.NDArray[np.int_],
    Bx: npt.NDArray[np.number[Any]],
    Cp: npt.NDArray[np.int_],  # output
    Cj: npt.NDArray[np.int_],  # output
    Cx: npt.NDArray[np.number[Any]],  # output
    /,
) -> None: ...
def bsr_elmul_bsr(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    R: SupportsIndex,
    C: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],
    Bp: npt.NDArray[np.int_],
    Bj: npt.NDArray[np.int_],
    Bx: npt.NDArray[np.number[Any]],
    Cp: npt.NDArray[np.int_],  # output
    Cj: npt.NDArray[np.int_],  # output
    Cx: npt.NDArray[np.number[Any]],  # output
    /,
) -> None: ...
def bsr_ge_bsr(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    R: SupportsIndex,
    C: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],
    Bp: npt.NDArray[np.int_],
    Bj: npt.NDArray[np.int_],
    Bx: npt.NDArray[np.number[Any]],
    Cp: npt.NDArray[np.int_],  # output
    Cj: npt.NDArray[np.int_],  # output
    Cx: npt.NDArray[np.number[Any]],  # output
    /,
) -> None: ...
def bsr_gt_bsr(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    R: SupportsIndex,
    C: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],
    Bp: npt.NDArray[np.int_],
    Bj: npt.NDArray[np.int_],
    Bx: npt.NDArray[np.number[Any]],
    Cp: npt.NDArray[np.int_],  # output
    Cj: npt.NDArray[np.int_],  # output
    Cx: npt.NDArray[np.number[Any]],  # output
    /,
) -> None: ...
def bsr_le_bsr(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    R: SupportsIndex,
    C: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],
    Bp: npt.NDArray[np.int_],
    Bj: npt.NDArray[np.int_],
    Bx: npt.NDArray[np.number[Any]],
    Cp: npt.NDArray[np.int_],  # output
    Cj: npt.NDArray[np.int_],  # output
    Cx: npt.NDArray[np.number[Any]],  # output
    /,
) -> None: ...
def bsr_lt_bsr(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    R: SupportsIndex,
    C: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],
    Bp: npt.NDArray[np.int_],
    Bj: npt.NDArray[np.int_],
    Bx: npt.NDArray[np.number[Any]],
    Cp: npt.NDArray[np.int_],  # output
    Cj: npt.NDArray[np.int_],  # output
    Cx: npt.NDArray[np.number[Any]],  # output
    /,
) -> None: ...
def bsr_matmat(
    maxnnz: SupportsIndex,
    n_brow: SupportsIndex,
    n_bcol: SupportsIndex,
    R: SupportsIndex,
    C: SupportsIndex,
    N: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],
    Bp: npt.NDArray[np.int_],
    Bj: npt.NDArray[np.int_],
    Bx: npt.NDArray[np.number[Any]],
    Cp: npt.NDArray[np.int_],  # output
    Cj: npt.NDArray[np.int_],  # output
    Cx: npt.NDArray[np.number[Any]],  # output
    /,
) -> None: ...
def bsr_matvec(
    n_brow: SupportsIndex,
    n_bcol: SupportsIndex,
    R: SupportsIndex,
    C: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],
    Xx: npt.NDArray[np.number[Any]],
    Yx: npt.NDArray[np.number[Any]],  # output
    /,
) -> None: ...
def bsr_matvecs(
    n_brow: SupportsIndex,
    n_bcol: SupportsIndex,
    n_vecs: SupportsIndex,
    R: SupportsIndex,
    C: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],
    Xx: npt.NDArray[np.number[Any]],
    Yx: npt.NDArray[np.number[Any]],  # output
    /,
) -> None: ...
def bsr_maximum_bsr(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    R: SupportsIndex,
    C: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],
    Bp: npt.NDArray[np.int_],
    Bj: npt.NDArray[np.int_],
    Bx: npt.NDArray[np.number[Any]],
    Cp: npt.NDArray[np.int_],  # output
    Cj: npt.NDArray[np.int_],  # output
    Cx: npt.NDArray[np.number[Any]],  # output
    /,
) -> None: ...
def bsr_minimum_bsr(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    R: SupportsIndex,
    C: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],
    Bp: npt.NDArray[np.int_],
    Bj: npt.NDArray[np.int_],
    Bx: npt.NDArray[np.number[Any]],
    Cp: npt.NDArray[np.int_],  # output
    Cj: npt.NDArray[np.int_],  # output
    Cx: npt.NDArray[np.number[Any]],  # output
    /,
) -> None: ...
def bsr_minus_bsr(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    R: SupportsIndex,
    C: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],
    Bp: npt.NDArray[np.int_],
    Bj: npt.NDArray[np.int_],
    Bx: npt.NDArray[np.number[Any]],
    Cp: npt.NDArray[np.int_],  # output
    Cj: npt.NDArray[np.int_],  # output
    Cx: npt.NDArray[np.number[Any]],  # output
    /,
) -> None: ...
def bsr_ne_bsr(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    R: SupportsIndex,
    C: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],
    Bp: npt.NDArray[np.int_],
    Bj: npt.NDArray[np.int_],
    Bx: npt.NDArray[np.number[Any]],
    Cp: npt.NDArray[np.int_],  # output
    Cj: npt.NDArray[np.int_],  # output
    Cx: npt.NDArray[np.number[Any]],  # output
    /,
) -> None: ...
def bsr_plus_bsr(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    R: SupportsIndex,
    C: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],
    Bp: npt.NDArray[np.int_],
    Bj: npt.NDArray[np.int_],
    Bx: npt.NDArray[np.number[Any]],
    Cp: npt.NDArray[np.int_],  # output
    Cj: npt.NDArray[np.int_],  # output
    Cx: npt.NDArray[np.number[Any]],  # output
    /,
) -> None: ...
def bsr_scale_columns(
    n_brow: SupportsIndex,
    n_bcol: SupportsIndex,
    R: SupportsIndex,
    C: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[Any],  # mutated
    Xx: npt.NDArray[Any],
    /,
) -> None: ...
def bsr_scale_rows(
    n_brow: SupportsIndex,
    n_bcol: SupportsIndex,
    R: SupportsIndex,
    C: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[Any],  # mutated
    Xx: npt.NDArray[Any],
    /,
) -> None: ...
def bsr_sort_indices(
    n_brow: SupportsIndex,
    n_bcol: SupportsIndex,
    R: SupportsIndex,
    C: SupportsIndex,
    Ap: npt.NDArray[np.int_],  # mutated
    Aj: npt.NDArray[np.int_],  # mutated
    Ax: npt.NDArray[Any],  # mutated
    /,
) -> None: ...
def bsr_tocsr(
    n_brow: SupportsIndex,
    n_bcol: SupportsIndex,
    R: SupportsIndex,
    C: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[Any],
    Bp: npt.NDArray[np.int_],  # output
    Bj: npt.NDArray[np.int_],  # output
    Bx: npt.NDArray[Any],  # output
    /,
) -> None: ...
def bsr_transpose(
    n_brow: SupportsIndex,
    n_bcol: SupportsIndex,
    R: SupportsIndex,
    C: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[Any],
    Bp: npt.NDArray[np.int_],  # output
    Bj: npt.NDArray[np.int_],  # output
    Bx: npt.NDArray[Any],  # output
    /,
) -> None: ...
def coo_matvec(
    nnz: np.int64,
    Ai: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],
    Xx: npt.NDArray[np.number[Any]],
    Yx: npt.NDArray[np.number[Any]],
    /,
) -> None: ...
def coo_tocsr(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    nnz: SupportsIndex,
    Ai: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[Any],
    Bp: npt.NDArray[np.int_],  # output
    Bj: npt.NDArray[np.int_],  # output
    Bx: npt.NDArray[Any],  # output
    /,
) -> None: ...
def coo_todense(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    nnz: np.int64,
    Ai: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[Any],
    Bx: npt.NDArray[Any],  # output
    fortran: bool,
    /,
) -> None: ...
def cs_graph_components(
    n_nod: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    flag: npt.NDArray[np.int_],  # output
    /,
) -> int: ...
def csc_diagonal(
    k: SupportsIndex,
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[Any],
    Yx: npt.NDArray[Any],  # output
    /,
) -> None: ...
def csc_eldiv_csc(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Ai: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],
    Bp: npt.NDArray[np.int_],
    Bi: npt.NDArray[np.int_],
    Bx: npt.NDArray[np.number[Any]],
    Cp: npt.NDArray[np.int_],  # output
    Ci: npt.NDArray[np.int_],  # output
    Cx: npt.NDArray[np.number[Any]],  # output
    /,
) -> None: ...
def csc_elmul_csc(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Ai: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],
    Bp: npt.NDArray[np.int_],
    Bi: npt.NDArray[np.int_],
    Bx: npt.NDArray[np.number[Any]],
    Cp: npt.NDArray[np.int_],  # output
    Ci: npt.NDArray[np.int_],  # output
    Cx: npt.NDArray[np.number[Any]],  # output
    /,
) -> None: ...
def csc_ge_csc(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Ai: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],
    Bp: npt.NDArray[np.int_],
    Bi: npt.NDArray[np.int_],
    Bx: npt.NDArray[np.number[Any]],
    Cp: npt.NDArray[np.int_],  # output
    Ci: npt.NDArray[np.int_],  # output
    Cx: npt.NDArray[np.number[Any]],  # output
    /,
) -> None: ...
def csc_gt_csc(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Ai: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],
    Bp: npt.NDArray[np.int_],
    Bi: npt.NDArray[np.int_],
    Bx: npt.NDArray[np.number[Any]],
    Cp: npt.NDArray[np.int_],  # output
    Ci: npt.NDArray[np.int_],  # output
    Cx: npt.NDArray[np.number[Any]],  # output
    /,
) -> None: ...
def csc_le_csc(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Ai: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],
    Bp: npt.NDArray[np.int_],
    Bi: npt.NDArray[np.int_],
    Bx: npt.NDArray[np.number[Any]],
    Cp: npt.NDArray[np.int_],  # output
    Ci: npt.NDArray[np.int_],  # output
    Cx: npt.NDArray[np.number[Any]],  # output
    /,
) -> None: ...
def csc_lt_csc(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Ai: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],
    Bp: npt.NDArray[np.int_],
    Bi: npt.NDArray[np.int_],
    Bx: npt.NDArray[np.number[Any]],
    Cp: npt.NDArray[np.int_],  # output
    Ci: npt.NDArray[np.int_],  # output
    Cx: npt.NDArray[np.number[Any]],  # output
    /,
) -> None: ...
def csc_matmat(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Ai: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],
    Bp: npt.NDArray[np.int_],
    Bi: npt.NDArray[np.int_],
    Bx: npt.NDArray[np.number[Any]],
    Cp: npt.NDArray[np.int_],  # output
    Ci: npt.NDArray[np.int_],  # output
    Cx: npt.NDArray[np.number[Any]],  # output
    /,
) -> None: ...
def csc_matmat_maxnnz(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Ai: npt.NDArray[np.int_],
    Bp: npt.NDArray[np.int_],
    Bi: npt.NDArray[np.int_],
    /,
) -> int: ...  # is this the right return type?
def csc_matvec(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Ai: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],
    Xx: npt.NDArray[np.number[Any]],
    Yx: npt.NDArray[np.number[Any]],  # output
    /,
) -> None: ...
def csc_matvecs(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    n_vecs: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Ai: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],
    Xx: npt.NDArray[np.number[Any]],
    Yx: npt.NDArray[np.number[Any]],  # output
    /,
) -> None: ...
def csc_maximum_csc(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Ai: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],
    Bp: npt.NDArray[np.int_],
    Bi: npt.NDArray[np.int_],
    Bx: npt.NDArray[np.number[Any]],
    Cp: npt.NDArray[np.int_],  # output
    Ci: npt.NDArray[np.int_],  # output
    Cx: npt.NDArray[np.number[Any]],  # output
    /,
) -> None: ...
def csc_minimum_csc(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Ai: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],
    Bp: npt.NDArray[np.int_],
    Bi: npt.NDArray[np.int_],
    Bx: npt.NDArray[np.number[Any]],
    Cp: npt.NDArray[np.int_],  # output
    Ci: npt.NDArray[np.int_],  # output
    Cx: npt.NDArray[np.number[Any]],  # output
    /,
) -> None: ...
def csc_minus_csc(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Ai: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],
    Bp: npt.NDArray[np.int_],
    Bi: npt.NDArray[np.int_],
    Bx: npt.NDArray[np.number[Any]],
    Cp: npt.NDArray[np.int_],  # output
    Ci: npt.NDArray[np.int_],  # output
    Cx: npt.NDArray[np.number[Any]],  # output
    /,
) -> None: ...
def csc_ne_csc(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Ai: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],
    Bp: npt.NDArray[np.int_],
    Bi: npt.NDArray[np.int_],
    Bx: npt.NDArray[np.number[Any]],
    Cp: npt.NDArray[np.int_],  # output
    Ci: npt.NDArray[np.int_],  # output
    Cx: npt.NDArray[np.number[Any]],  # output
    /,
) -> None: ...
def csc_plus_csc(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Ai: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],
    Bp: npt.NDArray[np.int_],
    Bi: npt.NDArray[np.int_],
    Bx: npt.NDArray[np.number[Any]],
    Cp: npt.NDArray[np.int_],  # output
    Ci: npt.NDArray[np.int_],  # output
    Cx: npt.NDArray[np.number[Any]],  # output
    /,
) -> None: ...
def csc_tocsr(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Ai: npt.NDArray[np.int_],
    Ax: npt.NDArray[Any],
    Bp: npt.NDArray[np.int_],  # output
    Bj: npt.NDArray[np.int_],  # output
    Bx: npt.NDArray[Any],  # output
    /,
) -> None: ...
def csr_column_index1(
    n_idx: SupportsIndex,
    col_idxs: npt.NDArray[np.int_],
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    col_offsets: npt.NDArray[np.int_],  # output
    Bp: npt.NDArray[np.int_],  # output
    /,
) -> None: ...
def csr_column_index2(
    col_order: npt.NDArray[np.int_],
    col_offsets: npt.NDArray[np.int_],
    nnz: SupportsIndex,
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[Any],
    Bj: npt.NDArray[np.int_],  # output
    Bx: npt.NDArray[Any],  # output
    /,
) -> None: ...
def csr_count_blocks(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    R: SupportsIndex,
    C: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    /,
) -> int: ...
def csr_diagonal(
    k: SupportsIndex,
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[Any],
    Yx: npt.NDArray[Any],  # output
    /,
) -> None: ...
def csr_eldiv_csr(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],
    Bp: npt.NDArray[np.int_],
    Bj: npt.NDArray[np.int_],
    Bx: npt.NDArray[np.number[Any]],
    Cp: npt.NDArray[np.int_],  # output
    Cj: npt.NDArray[np.int_],  # output
    Cx: npt.NDArray[np.number[Any]],  # output
    /,
) -> None: ...
def csr_eliminate_zeros(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    Ap: npt.NDArray[np.int_],  # mutated
    Aj: npt.NDArray[np.int_],  # mutated
    Ax: npt.NDArray[Any],  # mutated
    /,
) -> None: ...
def csr_elmul_csr(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],
    Bp: npt.NDArray[np.int_],
    Bj: npt.NDArray[np.int_],
    Bx: npt.NDArray[np.number[Any]],
    Cp: npt.NDArray[np.int_],  # output
    Cj: npt.NDArray[np.int_],  # output
    Cx: npt.NDArray[np.number[Any]],  # output
    /,
) -> None: ...
def csr_ge_csr(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],
    Bp: npt.NDArray[np.int_],
    Bj: npt.NDArray[np.int_],
    Bx: npt.NDArray[np.number[Any]],
    Cp: npt.NDArray[np.int_],  # output
    Cj: npt.NDArray[np.int_],  # output
    Cx: npt.NDArray[np.number[Any]],  # output
    /,
) -> None: ...
def csr_gt_csr(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],
    Bp: npt.NDArray[np.int_],
    Bj: npt.NDArray[np.int_],
    Bx: npt.NDArray[np.number[Any]],
    Cp: npt.NDArray[np.int_],  # output
    Cj: npt.NDArray[np.int_],  # output
    Cx: npt.NDArray[np.number[Any]],  # output
    /,
) -> None: ...
def csr_has_canonical_format(
    n_row: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    /,
) -> bool: ...
def csr_has_sorted_indices(
    n_row: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    /,
) -> bool: ...
def csr_hstack(
    n_blocks: SupportsIndex,
    n_row: SupportsIndex,
    n_col_cat: npt.NDArray[np.int_],
    Ap_cat: npt.NDArray[np.int_],
    Aj_cat: npt.NDArray[np.int_],
    Ax_cat: npt.NDArray[Any],
    Bp: npt.NDArray[np.int_],  # output
    Bj: npt.NDArray[np.int_],  # output
    Bx: npt.NDArray[Any],  # output
    /,
) -> None: ...
def csr_le_csr(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],
    Bp: npt.NDArray[np.int_],
    Bj: npt.NDArray[np.int_],
    Bx: npt.NDArray[np.number[Any]],
    Cp: npt.NDArray[np.int_],  # output
    Cj: npt.NDArray[np.int_],  # output
    Cx: npt.NDArray[np.number[Any]],  # output
    /,
) -> None: ...
def csr_lt_csr(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],
    Bp: npt.NDArray[np.int_],
    Bj: npt.NDArray[np.int_],
    Bx: npt.NDArray[np.number[Any]],
    Cp: npt.NDArray[np.int_],  # output
    Cj: npt.NDArray[np.int_],  # output
    Cx: npt.NDArray[np.number[Any]],  # output
    /,
) -> None: ...
def csr_matmat(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],
    Bp: npt.NDArray[np.int_],
    Bj: npt.NDArray[np.int_],
    Bx: npt.NDArray[np.number[Any]],
    Cp: npt.NDArray[np.int_],  # output
    Cj: npt.NDArray[np.int_],  # output
    Cx: npt.NDArray[np.number[Any]],  # output
    /,
) -> None: ...
def csr_matmat_maxnnz(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Bp: npt.NDArray[np.int_],
    Bj: npt.NDArray[np.int_],
    /,
) -> int: ...
def csr_matvec(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],
    Xx: npt.NDArray[np.number[Any]],
    Yx: npt.NDArray[np.number[Any]],  # output
    /,
) -> None: ...
def csr_matvecs(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    n_vecs: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],
    Xx: npt.NDArray[np.number[Any]],
    Yx: npt.NDArray[np.number[Any]],  # output
    /,
) -> None: ...
def csr_maximum_csr(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],
    Bp: npt.NDArray[np.int_],
    Bj: npt.NDArray[np.int_],
    Bx: npt.NDArray[np.number[Any]],
    Cp: npt.NDArray[np.int_],  # output
    Cj: npt.NDArray[np.int_],  # output
    Cx: npt.NDArray[np.number[Any]],  # output
    /,
) -> None: ...
def csr_minimum_csr(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],
    Bp: npt.NDArray[np.int_],
    Bj: npt.NDArray[np.int_],
    Bx: npt.NDArray[np.number[Any]],
    Cp: npt.NDArray[np.int_],  # output
    Cj: npt.NDArray[np.int_],  # output
    Cx: npt.NDArray[np.number[Any]],  # output
    /,
) -> None: ...
def csr_minus_csr(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],
    Bp: npt.NDArray[np.int_],
    Bj: npt.NDArray[np.int_],
    Bx: npt.NDArray[np.number[Any]],
    Cp: npt.NDArray[np.int_],  # output
    Cj: npt.NDArray[np.int_],  # output
    Cx: npt.NDArray[np.number[Any]],  # output
    /,
) -> None: ...
def csr_ne_csr(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],
    Bp: npt.NDArray[np.int_],
    Bj: npt.NDArray[np.int_],
    Bx: npt.NDArray[np.number[Any]],
    Cp: npt.NDArray[np.int_],  # output
    Cj: npt.NDArray[np.int_],  # output
    Cx: npt.NDArray[np.number[Any]],  # output
    /,
) -> None: ...
def csr_plus_csr(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],
    Bp: npt.NDArray[np.int_],
    Bj: npt.NDArray[np.int_],
    Bx: npt.NDArray[np.number[Any]],
    Cp: npt.NDArray[np.int_],  # output
    Cj: npt.NDArray[np.int_],  # output
    Cx: npt.NDArray[np.number[Any]],  # output
    /,
) -> None: ...
def csr_row_index(
    n_row_idx: SupportsIndex,
    rows: npt.NDArray[np.int_],
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[Any],
    Bj: npt.NDArray[np.int_],  # output
    Bx: npt.NDArray[Any],  # output
    /,
) -> None: ...
def csr_row_slice(
    start: SupportsIndex,
    stop: SupportsIndex,
    step: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[Any],
    Bj: npt.NDArray[np.int_],  # output
    Bx: npt.NDArray[Any],  # output
    /,
) -> None: ...
def csr_sample_offsets(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    n_samples: SupportsIndex,
    Bi: npt.NDArray[np.int_],
    Bj: npt.NDArray[np.int_],
    Bp: npt.NDArray[np.int_],  # output
    /,
) -> None: ...
def csr_sample_values(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[Any],
    n_samples: SupportsIndex,
    Bi: npt.NDArray[np.int_],
    Bj: npt.NDArray[np.int_],
    Bx: npt.NDArray[Any],  # output
    /,
) -> None: ...
def csr_scale_columns(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],  # mutated
    Xx: npt.NDArray[np.number[Any]],
    /,
) -> None: ...
def csr_scale_rows(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[np.number[Any]],  # mutated
    Xx: npt.NDArray[np.number[Any]],
    /,
) -> None: ...
def csr_sort_indices(
    n_row: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],  # mutated
    Ax: npt.NDArray[Any],  # mutated
    /,
) -> None: ...
def csr_sum_duplicates(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    Ap: npt.NDArray[np.int_],  # mutated
    Aj: npt.NDArray[np.int_],  # mutated
    Ax: npt.NDArray[np.number[Any]],  # mutated
    /,
) -> None: ...
def csr_tobsr(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    R: SupportsIndex,
    C: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[Any],
    Bp: npt.NDArray[np.int_],  # output
    Bj: npt.NDArray[np.int_],  # output
    Bx: npt.NDArray[Any],  # output
    /,
) -> None: ...
def csr_tocsc(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[Any],
    Bp: npt.NDArray[np.int_],  # output
    Bi: npt.NDArray[np.int_],  # output
    Bx: npt.NDArray[Any],  # output
    /,
) -> None: ...
def csr_todense(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[Any],
    Bx: npt.NDArray[Any],  # output
    /,
) -> None: ...
def dia_matvec(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    n_diags: SupportsIndex,
    L: SupportsIndex,
    offsets: npt.NDArray[np.int_],
    diags: npt.NDArray[np.number[Any]],
    Xx: npt.NDArray[np.number[Any]],
    Yx: npt.NDArray[np.number[Any]],  # output
    /,
) -> None: ...
def expandptr(
    n_row: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Bi: npt.NDArray[np.int_],  # output
    /,
) -> None: ...
@overload
def get_csr_submatrix(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[_SCT_co],
    ir0: SupportsIndex,
    ir1: SupportsIndex,
    ic0: SupportsIndex,
    ic1: SupportsIndex,
    /,
) -> tuple[npt.NDArray[np.int_], npt.NDArray[np.int_], npt.NDArray[_SCT_co]]: ...
@overload
def get_csr_submatrix(
    n_row: SupportsIndex,
    n_col: SupportsIndex,
    Ap: npt.NDArray[np.int_],
    Aj: npt.NDArray[np.int_],
    Ax: npt.NDArray[Any],
    ir0: SupportsIndex,
    ir1: SupportsIndex,
    ic0: SupportsIndex,
    ic1: SupportsIndex,
    /,
) -> tuple[npt.NDArray[np.int_], npt.NDArray[np.int_], npt.NDArray[Any]]: ...
def test_throw_error() -> NoReturn: ...

## must annotate:
# csc_tocsr
# coo_matvec
