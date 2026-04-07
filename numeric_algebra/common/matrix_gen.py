"""
Matrix generation utilities.
"""

from typing import Callable

import numpy as np


def make_matrix(
    n: int,
    m: int,
    func: Callable[[int, int], float],
    **kwargs,
) -> np.ndarray:
    """
    Generate an n x m matrix where each element is computed by func(i, j).

    Args:
        n: Number of rows
        m: Number of columns
        func: Function taking (i, j) and returning the matrix element
        **kwargs: Additional arguments passed to np.array constructor

    Returns:
        Generated numpy array
    """
    return np.array(
        [[func(i, j) for j in range(m)] for i in range(n)],
        **kwargs,
    )


def get_hilbert_matrix(n: int) -> np.ndarray:
    """
    Generate the n x n Hilbert matrix H where H[i,j] = 1/(i+j+1).

    The Hilbert matrix is notoriously ill-conditioned.

    Args:
        n: Size of the matrix

    Returns:
        n x n Hilbert matrix
    """
    H = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            H[i, j] = 1 / (i + j + 1)
    return H


def get_hilbert_vector(n: int) -> np.ndarray:
    """
    Generate the vector b where b[i] = sum_j 1/(i+j+1) for the Hilbert matrix.

    This is equivalent to H @ np.ones(n) where H is the Hilbert matrix.

    Args:
        n: Size of the vector

    Returns:
        n-dimensional vector
    """
    b = np.zeros(n)
    for i in range(n):
        b[i] = sum(1 / (i + j + 1) for j in range(n))
    return b


def get_bar_matrix(n: int) -> np.ndarray:
    """
    Generate a tridiagonal "bar" matrix: 10 on diagonal, 1 on sub/super diagonal.

    Args:
        n: Size of the matrix

    Returns:
        n x n tridiagonal matrix
    """
    return np.eye(n) * 10 + np.eye(n, k=1) + np.eye(n, k=-1)


def get_test_matrix(n: int) -> np.ndarray:
    """
    Generate a test matrix for condition number experiments.

    Args:
        n: Size of the matrix

    Returns:
        n x n test matrix
    """
    A = np.eye(n) - np.tri(n, n, k=-1)
    A[: n - 1, n - 1] = np.ones(n - 1)
    return A


def gen_symmetric_pos_def_matrix(n: int) -> np.ndarray:
    """
    Generate a random symmetric positive definite matrix.

    Creates A = B + B.T where B has positive entries, ensuring positive definiteness.

    Args:
        n: Size of the matrix

    Returns:
        n x n symmetric positive definite matrix
    """
    A = np.abs(np.random.rand(n, n))
    return A + A.T
