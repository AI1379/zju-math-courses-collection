"""
Linear system solvers using various decomposition methods.
"""

import numpy as np

from numeric_algebra.common.decompositions import cholesky_np, cholesky_np_im


def solve_cholesky(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Solve Ax = b using Cholesky decomposition A = L @ L.T.

    Args:
        A: Symmetric positive definite matrix
        b: Right-hand side vector

    Returns:
        Solution vector x
    """
    from numeric_algebra.hw2.exercise1 import backward_substitution, forward_substitution

    L = cholesky_np(A)
    y = forward_substitution(L, b, validate=False)
    x = backward_substitution(L.T, y, validate=False)
    return x


def solve_cholesky_im(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Solve Ax = b using improved Cholesky decomposition A = L @ D @ L.T.

    Args:
        A: Symmetric positive definite matrix
        b: Right-hand side vector

    Returns:
        Solution vector x
    """
    from numeric_algebra.hw2.exercise1 import backward_substitution, forward_substitution

    L, D = cholesky_np_im(A)
    y = forward_substitution(L, b, validate=False)
    DLT = D @ L.T
    x = backward_substitution(DLT, y, validate=False)
    return x
