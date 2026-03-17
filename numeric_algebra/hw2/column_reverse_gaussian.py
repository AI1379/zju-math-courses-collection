import numpy as np

EPS = 1e-10


def column_reverse_gaussian(A: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    Return a unit upper triangular matrix U and a lower triangular matrix L such
    that A = UL.
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


if __name__ == "__main__":
    n = 4
    A = np.random.rand(n, n)
    # A = np.array(
    #     [
    #         [4, 2, 1, 3],
    #         [3, 5, 2, 1],
    #         [1, 2, 4, 2],
    #         [2, 1, 3, 4],
    #     ],
    #     dtype=float,
    # )
    print(f"Original matrix A:\n{A}\n")
    U, L = column_reverse_gaussian(A)
    print(f"Upper triangular matrix U:\n{U}\n")
    print(f"Lower triangular matrix L:\n{L}\n")
    print("Verification: UL = A?")
    print(U @ L)
    print("Difference:", np.linalg.norm(U @ L - A))
