"""
Matrix decomposition algorithms.
"""

import numpy as np
import sympy as sp

EPS = 1e-10


def column_reverse_gaussian(A: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    Column-reverse Gaussian elimination: decompose A = UL where U is unit upper
    triangular and L is lower triangular.

    Args:
        A: Square matrix to decompose

    Returns:
        Tuple (U, L) such that A = U @ L
    """
    U, L = np.eye(A.shape[0], dtype=float), A.copy()
    n = A.shape[0]
    for j in range(n - 1, 0, -1):
        if abs(L[j, j]) < EPS:
            raise ValueError("Zero pivot encountered.")
        factors = L[:j, j] / L[j, j]
        U[:j, j] = factors
        L[:j, :] -= np.outer(factors, L[j, :])
    return U, L


def cholesky_np(mat: np.ndarray) -> np.ndarray:
    """
    Cholesky decomposition: A = L @ L.T for symmetric positive definite A.

    Args:
        mat: Symmetric positive definite matrix

    Returns:
        Lower triangular matrix L such that A = L @ L.T
    """
    A = mat.copy()
    n = A.shape[0]
    L = np.zeros_like(A)
    for k in range(n):
        L[k, k] = np.sqrt(A[k, k])
        L[k + 1 : n, k] = A[k + 1 : n, k] / L[k, k]
        for j in range(k + 1, n):
            A[j:n, j] = A[j:n, j] - L[j:n, k] * L[j, k]
    return L


def cholesky_sp(mat: sp.Matrix) -> sp.Matrix:
    """
    Symbolic Cholesky decomposition: A = L @ L.T for symmetric positive definite A.

    Args:
        mat: SymPy Matrix, symmetric positive definite

    Returns:
        Lower triangular SymPy Matrix L such that A = L * L.T
    """
    A = mat.copy()
    n = A.shape[0]
    L = sp.zeros(n)
    for k in range(n):
        L[k, k] = sp.sqrt(A[k, k])
        L[k + 1 : n, k] = A[k + 1 : n, k] / L[k, k]
        for j in range(k + 1, n):
            A[j:n, j] = A[j:n, j] - L[j:n, k] * L[j, k]
    return L


def cholesky_np_im(mat: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    Improved Cholesky decomposition (LDL^T): A = L @ D @ L.T for symmetric matrix A.

    This version avoids computing square roots, which can be more numerically stable.

    Args:
        mat: Symmetric matrix (positive definite for positive D)

    Returns:
        Tuple (L, D) where L is unit lower triangular and D is diagonal
    """
    A = mat.copy()
    n = A.shape[0]
    D = np.zeros_like(A)
    L = np.eye(n)
    for j in range(n):
        v = np.ndarray(shape=(j,))
        for i in range(j):
            v[i] = L[j, i] * D[i, i]
        D[j, j] = A[j, j] - L[j, :j] @ v
        L[j + 1 : n, j] = (A[j + 1 : n, j] - L[j + 1 : n, :j] @ v) / D[j, j]
    return L, D


def cholesky_sp_im(mat: sp.Matrix) -> tuple[sp.Matrix, sp.Matrix]:
    """
    Symbolic improved Cholesky decomposition (LDL^T): A = L @ D @ L.T.

    Args:
        mat: SymPy Matrix, symmetric

    Returns:
        Tuple (L, D) where L is unit lower triangular and D is diagonal
    """
    A = mat.copy()
    n = A.shape[0]
    D = sp.zeros(n)
    L = sp.eye(n)
    for j in range(n):
        v = sp.zeros(j, 1)
        for i in range(j):
            v[i, 0] = L[j, i] * D[i, i]
        D[j, j] = A[j, j] - (L[j, :j] * v)[0, 0]
        L[j + 1 : n, j] = (A[j + 1 : n, j] - L[j + 1 : n, :j] * v) / D[j, j]
    return L, D
