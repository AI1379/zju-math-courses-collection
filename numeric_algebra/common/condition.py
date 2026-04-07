"""
Condition number computation utilities.
"""

import numpy as np


def gradient_descent_norm_1(
    B: np.ndarray,
    x0: np.ndarray,
    max_iter: int = 1000,
    eps: float = 1e-6,
) -> float:
    """
    Compute the 1-norm of matrix B using gradient descent.

    Args:
        B: Input matrix
        x0: Initial guess vector
        max_iter: Maximum iterations
        eps: Convergence tolerance

    Returns:
        1-norm of B
    """
    x = x0.copy()
    for _ in range(max_iter):
        w = B @ x
        v = np.sign(w)
        z = B.T @ v
        z_norm_inf = np.max(np.abs(z))
        if z_norm_inf - z @ x < eps:
            break
        z_norm_inf_idx = np.argmax(np.abs(z))
        x = np.zeros_like(x)
        x[z_norm_inf_idx] = 1
    return np.sum(np.abs(B @ x))


def calculate_kappa(B: np.ndarray) -> float:
    """
    Compute the condition number kappa(B) in 1-norm.

    Args:
        B: Square matrix

    Returns:
        Condition number in 1-norm
    """
    n = B.shape[0]
    x0 = np.ones(n) / n
    norm_B = gradient_descent_norm_1(B, x0)
    norm_B_inv = gradient_descent_norm_1(np.linalg.inv(B), x0)
    return norm_B * norm_B_inv
