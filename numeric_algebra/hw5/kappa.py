from math import comb

import numpy as np
import matplotlib.pyplot as plt
from numeric_algebra.hw3.exercise2 import get_hilbert_matrix
from numeric_algebra.common import gaussian_column_pivoting, solve_by_LU


def hilbert_norm_1(n: int) -> float:
    max_col_sum = 0.0
    for j in range(n):
        col_sum = sum(1.0 / (i + j + 1) for i in range(n))
        max_col_sum = max(max_col_sum, col_sum)
    return max_col_sum


def hilbert_inv_norm_1_exact(n: int) -> int:
    max_col_sum = 0
    for j in range(1, n + 1):
        col_sum = 0
        for i in range(1, n + 1):
            val = (
                (-1) ** (i + j)
                * (i + j - 1)
                * comb(n + i - 1, n - j)
                * comb(n + j - 1, n - i)
                * comb(i + j - 2, i - 1) ** 2
            )
            col_sum += abs(val)
        max_col_sum = max(max_col_sum, col_sum)
    return max_col_sum


def hilbert_kappa_exact(n: int) -> float:
    return hilbert_norm_1(n) * hilbert_inv_norm_1_exact(n)


def gradient_descent_norm_1(
    B: np.ndarray,
    x0: np.ndarray,
    max_iter: int = 1000,
    eps: float = 1e-6,
):
    x = x0.copy()
    for _ in range(max_iter):
        w = B @ x
        v = np.sign(w)
        z = B.T @ v
        z_norm_inf = np.max(np.abs(z))  # or np.linalg.norm(z, ord=np.inf)
        if z_norm_inf - z @ x < eps:
            break
        z_norm_inf_idx = np.argmax(np.abs(z))
        x = np.zeros_like(x)
        x[z_norm_inf_idx] = 1
    return np.sum(np.abs(B @ x))


def calculate_kappa(B: np.ndarray):
    n = B.shape[0]
    x0 = np.ones(n) / n
    norm_B = gradient_descent_norm_1(B, x0)
    norm_B_inv = gradient_descent_norm_1(np.linalg.inv(B), x0)
    return norm_B * norm_B_inv


def test_kappa(H: np.ndarray):
    kappa = calculate_kappa(H)
    np_kappa = np.linalg.cond(H, p=1)
    diff = kappa - np_kappa
    return kappa, np_kappa, diff


def get_test_matrix(n: int):
    A = np.eye(n) - np.tri(n, n, k=-1)
    A[: n - 1, n - 1] = np.ones(n - 1)
    return A


def test_kappa_on_column_gauss(n: int):
    A = get_test_matrix(n)
    x = np.random.rand(n)
    b = A @ x
    P, L, U = gaussian_column_pivoting(A)
    x_solved = solve_by_LU(L, U, P @ b)
    kappa = calculate_kappa(A)
    r = b - A @ x_solved
    r_norm_inf = np.linalg.norm(r, ord=np.inf)
    b_norm_inf = np.linalg.norm(b, ord=np.inf)
    approx_acc = kappa * r_norm_inf / b_norm_inf if b_norm_inf != 0 else 0
    delta_x = x - x_solved
    delta_x_norm_inf = np.linalg.norm(delta_x, ord=np.inf)
    x_norm_inf = np.linalg.norm(x, ord=np.inf)
    real_acc = delta_x_norm_inf / x_norm_inf if x_norm_inf != 0 else 0
    return kappa, approx_acc, real_acc


def prob1():
    k_lst = []
    np_kappa_lst = []
    exact_kappa_lst = []
    maxn = 30
    for n in range(1, maxn + 1):
        H = get_hilbert_matrix(n)
        kappa, np_kappa, _ = test_kappa(H)
        exact_kappa = hilbert_kappa_exact(n)

        k_lst.append(kappa)
        np_kappa_lst.append(np_kappa)
        exact_kappa_lst.append(exact_kappa)

        print(f"{n=:2d}: {kappa=:.4e}, NumPy={np_kappa=:.4e}, Exact={exact_kappa=:.4e}")

    k_lst = np.array(k_lst)
    np_kappa_lst = np.array(np_kappa_lst)
    exact_kappa_lst = np.array(exact_kappa_lst)

    mse = np.mean((k_lst - exact_kappa_lst) ** 2)
    np_mse = np.mean((np_kappa_lst - exact_kappa_lst) ** 2)
    print(f"MSE of GD vs Exact: {mse:.4e}")
    print(f"MSE of NumPy vs Exact: {np_mse:.4e}")

    rel_err = np.abs(k_lst - exact_kappa_lst) / np.abs(exact_kappa_lst)
    np_rel_err = np.abs(np_kappa_lst - exact_kappa_lst) / np.abs(exact_kappa_lst)

    plt.figure(figsize=(10, 8))

    plt.subplot(2, 1, 1)
    plt.plot(range(1, maxn + 1), k_lst, "o-", label="Gradient Descent", markersize=3)
    plt.plot(range(1, maxn + 1), np_kappa_lst, "s-", label="NumPy", markersize=3)
    plt.plot(
        range(1, maxn + 1),
        exact_kappa_lst,
        "k--",
        label="Exact (analytic)",
        linewidth=2,
    )
    plt.yscale("log")
    plt.xlabel("n")
    plt.ylabel("kappa")
    plt.title("kappa of Hilbert matrix")
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.semilogy(range(1, maxn + 1), rel_err, "o-", label="GD vs Exact", markersize=3)
    plt.semilogy(
        range(1, maxn + 1), np_rel_err, "s-", label="NumPy vs Exact", markersize=3
    )
    plt.xlabel("n")
    plt.ylabel("Relative Error")
    plt.title("Relative Error vs Exact kappa")
    plt.legend()

    plt.tight_layout()
    plt.savefig("kappa_comparison.png")
    plt.show()


def prob2():
    minn = 5
    maxn = 30
    approx_acc_lst = []
    real_acc_lst = []
    for n in range(minn, maxn + 1):
        kappa, approx_acc, real_acc = test_kappa_on_column_gauss(n)
        approx_acc_lst.append(approx_acc)
        real_acc_lst.append(real_acc)
        print(f"n={n}, kappa={kappa}, approx_acc={approx_acc}, real_acc={real_acc}")

    acc_diff = np.array(approx_acc_lst) - np.array(real_acc_lst)
    mse_acc = np.mean(acc_diff**2)
    print(f"MSE of accuracy differences: {mse_acc}")

    plt.figure(figsize=(10, 6))
    plt.plot(range(minn, maxn + 1), approx_acc_lst, label="Approximate Accuracy")
    plt.plot(range(minn, maxn + 1), real_acc_lst, label="Real Accuracy")
    plt.yscale("log")
    plt.xlabel("n")
    plt.ylabel("Accuracy")
    plt.title("Approximate vs Real Accuracy of Column Gaussian Elimination")
    plt.legend()
    plt.tight_layout()
    plt.savefig("accuracy_comparison.png")
    plt.show()


if __name__ == "__main__":
    prob1()
    print("\n" + "=" * 50 + "\n")
    prob2()
