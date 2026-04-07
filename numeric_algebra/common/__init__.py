"""
Common utilities for numerical algebra computations.

This module provides:
- Gaussian elimination (with/without pivoting)
- Forward/backward substitution
- LU decomposition solver
- Gauss-Jordan matrix inversion
- Cholesky decomposition (standard and improved)
- Matrix generation utilities
- Linear system solvers
- Condition number computation
"""

# Gaussian elimination and substitution (from hw2)
from numeric_algebra.hw2.exercise1 import (
    forward_substitution,
    backward_substitution,
    gaussian_column_pivoting,
    gaussian_no_pivoting,
    solve_by_LU,
)

# Gauss-Jordan inversion
from numeric_algebra.common.gaussian_jordan_inv import (
    gaussian_jordan_inv_no_pivot,
    gaussian_jordan_inv_col_pivot,
)

# Matrix decompositions
from numeric_algebra.common.decompositions import (
    column_reverse_gaussian,
    cholesky_np,
    cholesky_sp,
    cholesky_np_im,
    cholesky_sp_im,
)

# Matrix generation
from numeric_algebra.common.matrix_gen import (
    make_matrix,
    get_hilbert_matrix,
    get_hilbert_vector,
    get_bar_matrix,
    get_test_matrix,
    gen_symmetric_pos_def_matrix,
)

# Solvers
from numeric_algebra.common.solvers import (
    solve_cholesky,
    solve_cholesky_im,
)

# Condition number
from numeric_algebra.common.condition import (
    gradient_descent_norm_1,
    calculate_kappa,
)

__all__ = [
    # Gaussian elimination
    "forward_substitution",
    "backward_substitution",
    "gaussian_column_pivoting",
    "gaussian_no_pivoting",
    "solve_by_LU",
    # Gauss-Jordan
    "gaussian_jordan_inv_no_pivot",
    "gaussian_jordan_inv_col_pivot",
    # Decompositions
    "column_reverse_gaussian",
    "cholesky_np",
    "cholesky_sp",
    "cholesky_np_im",
    "cholesky_sp_im",
    # Matrix generation
    "make_matrix",
    "get_hilbert_matrix",
    "get_hilbert_vector",
    "get_bar_matrix",
    "get_test_matrix",
    "gen_symmetric_pos_def_matrix",
    # Solvers
    "solve_cholesky",
    "solve_cholesky_im",
    # Condition number
    "gradient_descent_norm_1",
    "calculate_kappa",
]
