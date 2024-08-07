import numpy as np
from scipy.linalg import schur

def compute_A_matrices(A, P):
    P1, P2 = P
    A11 = P1.T @ A @ P1
    A12 = P1.T @ A @ P2
    A21 = P2.T @ A @ P1
    A22 = P2.T @ A @ P2
    return A11, A12, A21, A22

def schur_decomposition(A):
    return schur(A)

def update_A11(A11, A12, Rk):
    return A11 + A12 @ Rk

def compute_A21_hat(A21, Rk, A12, Q):
    A21_hat = (A21 + Rk @ A12 @ Rk) @ Q
    A21_hat = np.clip(A21_hat, -1e10, 1e10)  # 限制數值範圍
    return A21_hat

def solve_sylvester_equation(A22, Z, A21_hat, s):
    X = np.zeros((A21_hat.shape[0], s))
    for j in range(s):
        try:
            xj = np.linalg.solve(A22 - Z[j, j] * np.eye(A22.shape[0]), -A21_hat[:, j])
        except np.linalg.LinAlgError:
            xj = np.linalg.pinv(A22 - Z[j, j] * np.eye(A22.shape[0])) @ (-A21_hat[:, j])
        X[:, j] = xj
    return X

def check_for_infs_or_nans(matrix, step):
    if np.any(np.isnan(matrix)) or np.any(np.isinf(matrix)):
        print(f"Inf or NaN found at step: {step}")
        raise ValueError("Matrix contains inf or NaN values")

def image_compression_algorithm(A, P, epsilon):
    A11, A12, A21, A22 = compute_A_matrices(A, P)
    check_for_infs_or_nans(A11, "Initial A11")
    check_for_infs_or_nans(A12, "Initial A12")
    check_for_infs_or_nans(A21, "Initial A21")
    check_for_infs_or_nans(A22, "Initial A22")

    k = 0
    Rk = np.zeros_like(A21)
    rk = A21
    
    if np.linalg.norm(rk) < epsilon:
        return Rk, None
    
    while True:
        A11_tilde = update_A11(A11, A12, Rk)
        check_for_infs_or_nans(A11_tilde, f"Iteration {k} A11_tilde")
        
        Q, Z = schur_decomposition(A11_tilde)
        check_for_infs_or_nans(Q, f"Iteration {k} Q")
        check_for_infs_or_nans(Z, f"Iteration {k} Z")
        
        A21_hat = compute_A21_hat(A21, Rk, A12, Q)
        check_for_infs_or_nans(A21_hat, f"Iteration {k} A21_hat")
        
        X = solve_sylvester_equation(A22, Z, A21_hat, A21_hat.shape[1])
        check_for_infs_or_nans(X, f"Iteration {k} X")
        
        Rk_next = X @ Q.T
        rk_next = np.linalg.norm(Rk_next)
        
        if rk_next < epsilon:
            return Rk_next, A11_tilde
        
        Rk = Rk_next
        rk = rk_next
        k += 1

def ensure_no_infs_or_nans(matrix):
    matrix = matrix.copy()  # 創建副本
    matrix[np.isinf(matrix)] = 0
    matrix[np.isnan(matrix)] = 0
    return matrix
