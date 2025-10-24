import numpy as np
import random
from itertools import combinations
from math import comb
import matplotlib.pyplot as plt

def fib_matrix(n):
    def matrix_mult(A, B):
        return np.array([
            [A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
            [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]
        ])
    def matrix_power(M, power):
        if power == 1:
            return M
        if power % 2 == 0:
            half = matrix_power(M, power // 2)
            return matrix_mult(half, half)
        else:
            return matrix_mult(M, matrix_power(M, power - 1))
    if n == 0:
        return 0
    F = np.array([[1, 1],[1, 0]])
    result = matrix_power(F, n - 1)
    return result[0][0]

def knapsack(weights, values, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    chosen = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen.append(i - 1)
            w -= weights[i - 1]
    chosen.reverse()
    return dp[n][capacity], chosen

def generate_binary_vectors(num_vectors=100, N=20):
    return [np.random.randint(0, 2, N) for _ in range(num_vectors)]

def sim_dot(x, y):
    numerator = np.dot(x, y)
    denom = (np.sum(x) * np.sum(y))
    return numerator / denom if denom != 0 else 0

def sim_jaccard(x, y):
    intersection = np.sum(np.logical_and(x, y))
    union = np.sum(np.logical_or(x, y))
    return intersection / union if union != 0 else 0

def neuro_experiment(num_vectors=100, N=50):
    vectors = generate_binary_vectors(num_vectors, N)
    sims_dot, sims_jacc = [], []
    for a, b in combinations(vectors, 2):
        sims_dot.append(sim_dot(a, b))
        sims_jacc.append(sim_jaccard(a, b))
    plt.hist(sims_dot, bins=20, alpha=0.6, label="Dot similarity")
    plt.hist(sims_jacc, bins=20, alpha=0.6, label="Jaccard similarity")
    plt.title(f"Similarity Distributions for N={N}")
    plt.legend()
    plt.show()

def sparse_vector_capacity(N=2000, w=5):
    return comb(N, w)

if __name__ == "__main__":
    n = 10
    print("F(", n, ") =", fib_matrix(n))
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5
    max_value, chosen = knapsack(weights, values, capacity)
    print("Max value:", max_value)
    print("Chosen items:", chosen)
    neuro_experiment(num_vectors=100, N=30)
    print("Possible vectors for N=2000, w=5:", sparse_vector_capacity())
