import sympy as sp

# Define symbolic matrix A and vector b
A = sp.Matrix([[1, 4, 7], [2, 5, 8], [3, 6, 10]])

b = sp.Matrix([1, 1, 1])

print("=" * 70)
print("SYMBOLIC LU DECOMPOSITION WITH SYMPY")
print("=" * 70)

print("\nOriginal matrix A:")
sp.pprint(A)

print("\nOriginal vector b:")
sp.pprint(b)

print("\n" + "=" * 70)
print("(1) Standard LU Decomposition (without pivoting)")
print("=" * 70)

# Symbolic LU decomposition without pivoting
L_U = A.LUdecomposition()
L_manual = L_U[0]
U_manual = L_U[1]

print("\nL matrix:")
sp.pprint(L_manual)

print("\nU matrix:")
sp.pprint(U_manual)

print("\nVerification: L * U = A?")
LU_prod = L_manual * U_manual
sp.pprint(LU_prod)

print("\nDifference (should be zero matrix):")
sp.pprint(LU_prod - A)

# Solve Ly = b using forward substitution (symbolic)
print("\n--- Solving Ly = b ---")
y = L_manual.inv() * b
print("y = L^{-1} * b =")
sp.pprint(y)

# Solve Ux = y using back substitution (symbolic)
print("\n--- Solving Ux = y ---")
x = U_manual.inv() * y
print("x = U^{-1} * y =")
sp.pprint(x)

print("\nVerification: A * x =")
Ax = A * x
sp.pprint(Ax)
print("Should equal b =")
sp.pprint(b)

print("\n" + "=" * 70)
print("(2) Partial Pivoting LU Decomposition (PA = LU)")
print("=" * 70)

print("\nNote: sympy doesn't directly support pivoting in LUdecomposition.")
print("We'll implement partial pivoting manually with symbolic operations.\n")

# Manual partial pivoting LU decomposition
# PA = LU, where P is row permutation matrix
# We'll use a different approach: track the elimination and build L properly
A_work = A.copy()
n = A_work.rows

# P: row permutation matrix
P_partial = sp.eye(n)
# L: will store multipliers (lower triangular)
L_partial = sp.eye(n)
# U: working copy (will become upper triangular)
U_work = A_work.copy()

# Track row permutation as a list
row_perm = list(range(n))

print("Starting partial pivoting LU decomposition...\n")

for k in range(n - 1):
    print(f"Step {k + 1}:")
    print("  Current U submatrix:")
    submatrix = U_work[k:, k:]
    sp.pprint(submatrix)

    # Find maximum element in column k (partial pivoting)
    max_val = sp.Abs(U_work[k, k])
    max_i = k
    for i in range(k + 1, n):
        if sp.simplify(sp.Abs(U_work[i, k]) - max_val) > 0:
            max_val = sp.Abs(U_work[i, k])
            max_i = i

    print(f"  Maximum element in column {k}: {U_work[max_i, k]} at row {max_i}")

    # Row swap in U_work
    if max_i != k:
        print(f"  Row swap: {k} <-> {max_i}")
        U_work.row_swap(k, max_i)
        # Also swap the corresponding rows in L (below diagonal)
        for j in range(k):
            L_partial[k, j], L_partial[max_i, j] = L_partial[max_i, j], L_partial[k, j]
        # Update row permutation
        row_perm[k], row_perm[max_i] = row_perm[max_i], row_perm[k]
        # Update P matrix to reflect the swap
        P_partial.row_swap(k, max_i)

    sp.pprint(U_work)

    # Elimination: compute multipliers and update U
    pivot = U_work[k, k]
    for i in range(k + 1, n):
        m_ik = sp.simplify(U_work[i, k] / pivot)
        L_partial[i, k] = m_ik
        # Eliminate: row_i = row_i - m_ik * row_k
        for j in range(k, n):
            U_work[i, j] = sp.expand(U_work[i, j] - m_ik * U_work[k, j])

    print("  After elimination:")
    sp.pprint(U_work)
    print()

# Extract U (upper triangular part)
U_partial = sp.zeros(n, n)
for i in range(n):
    for j in range(i, n):
        U_partial[i, j] = U_work[i, j]

print("\nP matrix (row permutation):")
sp.pprint(P_partial)

print("\nL matrix:")
sp.pprint(L_partial)

print("\nU matrix:")
sp.pprint(U_partial)

print("\nVerification: P * A = L * U?")
PA = P_partial * A
LU_prod = L_partial * U_partial

print("\nP * A:")
sp.pprint(PA)

print("\nL * U:")
sp.pprint(LU_prod)

print("\nDifference (should be zero matrix):")
sp.pprint(sp.simplify(PA - LU_prod))

# Solve with pivoting: PAx = Pb => Ly = Pb, Ux = y
print("\n--- Solving with partial pivoting ---")
Pb = P_partial * b
print("Pb =")
sp.pprint(Pb)

y = L_partial.inv() * Pb
print("\ny = L^{-1} * Pb =")
sp.pprint(y)

x = U_partial.inv() * y
print("\nx = U^{-1} * y =")
sp.pprint(x)

print("\nVerification: A * x =")
sp.pprint(A * x)
print("Should equal b =")
sp.pprint(b)

print("\n" + "=" * 70)
print("(3) Complete Pivoting LU Decomposition (PAQ = LU)")
print("=" * 70)

# Complete pivoting: PAQ = LU
A_work = A.copy()
n = A_work.rows

# Initialize permutation matrices
P_comp = sp.eye(n)  # Row permutations
Q_comp = sp.eye(n)  # Column permutations
L_comp = sp.eye(n)

# Track permutations
row_perm = list(range(n))
col_perm = list(range(n))

print(f"\nMatrix size: {n} x {n}")
print("\nStarting complete pivoting LU decomposition...\n")

for k in range(n - 1):
    print(f"\nStep {k + 1}:")
    print("  Current matrix A:")
    submatrix = A_work[k:, k:]
    sp.pprint(submatrix)

    # Find maximum element in the submatrix (complete pivoting)
    max_val = None
    max_i = k
    max_j = k

    for i in range(k, n):
        for j in range(k, n):
            val = sp.Abs(A_work[i, j])
            if max_val is None or sp.simplify(val - max_val) > 0:
                max_val = val
                max_i = i
                max_j = j

    print(f"  Maximum element: {A_work[max_i, max_j]} at ({max_i}, {max_j})")

    # Row swap
    if max_i != k:
        print(f"  Row swap: {k} <-> {max_i}")
        A_work.row_swap(k, max_i)
        # Swap rows in L for columns < k
        for j in range(k):
            L_comp[k, j], L_comp[max_i, j] = L_comp[max_i, j], L_comp[k, j]
        # Update P and row permutation
        P_comp.row_swap(k, max_i)
        row_perm[k], row_perm[max_i] = row_perm[max_i], row_perm[k]

    # Column swap
    if max_j != k:
        print(f"  Column swap: {k} <-> {max_j}")
        A_work.col_swap(k, max_j)
        # Update Q and column permutation
        Q_comp.col_swap(k, max_j)
        col_perm[k], col_perm[max_j] = col_perm[max_j], col_perm[k]

    print("  After swaps:")
    sp.pprint(A_work)

    # Elimination: make elements below pivot zero
    pivot = A_work[k, k]
    for i in range(k + 1, n):
        m_ik = sp.simplify(A_work[i, k] / pivot)
        L_comp[i, k] = m_ik
        # Row operation: R_i = R_i - m_ik * R_k
        for j in range(k, n):
            A_work[i, j] = sp.expand(A_work[i, j] - m_ik * A_work[k, j])

    print("  After elimination in column:")
    sp.pprint(A_work)
    print()

# Extract U (upper triangular part)
U_comp = sp.zeros(n, n)
for i in range(n):
    for j in range(i, n):
        U_comp[i, j] = A_work[i, j]

print("Final matrices:")
print("\nP matrix (row permutations):")
sp.pprint(P_comp)

print("\nQ matrix (column permutations):")
sp.pprint(Q_comp)

print("\nL matrix:")
sp.pprint(L_comp)

print("\nU matrix:")
sp.pprint(U_comp)

print("\nVerification: P * A * Q = L * U?")
PAQ = P_comp * A * Q_comp
LU_prod = L_comp * U_comp

print("\nP * A * Q:")
sp.pprint(PAQ)

print("\nL * U:")
sp.pprint(LU_prod)

print("\nDifference (should be zero matrix):")
sp.pprint(sp.simplify(PAQ - LU_prod))

# Solve with complete pivoting
# PAQ = L U
# Let z = Q^T * x (Q is permutation, so Q^T = Q^{-1})
# Then: PAz = L(Uz) = Pb

print("\n" + "=" * 70)
print("Solving with Complete Pivoting")
print("=" * 70)

print("\n--- Solving PAQx = Pb ---")
Pb_comp = P_comp * b
print("Pb =")
sp.pprint(Pb_comp)

y_comp = L_comp.inv() * Pb_comp
print("\ny = L^{-1} * Pb =")
sp.pprint(y_comp)

z_comp = U_comp.inv() * y_comp
print("\nz = U^{-1} * y =")
sp.pprint(z_comp)

x_comp = Q_comp * z_comp  # x = Q * z (since z = Q^T * x, so x = Q * z)
print("\nx = Q * z =")
sp.pprint(x_comp)

print("\nVerification: A * x =")
sp.pprint(A * x_comp)
print("Should equal b =")
sp.pprint(b)

# Verify by direct solve
print("\n" + "=" * 70)
print("Direct verification using sympy's solve")
print("=" * 70)
x_direct = A.inv() * b
print("\nx = A^{-1} * b =")
sp.pprint(x_direct)

print("\nDoes x from complete pivoting equal direct solution?")
sp.pprint(sp.simplify(x_comp - x_direct))
