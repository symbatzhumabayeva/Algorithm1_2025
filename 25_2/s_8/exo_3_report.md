# Problem Set #3 — Fundamental Algorithm Techniques

**Author:** Simba  
**Date:** October 2025  

---

## Problem 1 — Fibonacci Super Fast!

### Idea
Instead of using recursion, I used **matrix exponentiation**.  
The Fibonacci relation can be written as:

\[
\begin{bmatrix}
F_{n+1} \\
F_n
\end{bmatrix}
=
\begin{bmatrix}
1 & 1 \\
1 & 0
\end{bmatrix}^n
\begin{bmatrix}
1 \\
0
\end{bmatrix}
\]

This means we can compute Fibonacci numbers by raising the base matrix to the n-th power.  
I implemented fast exponentiation (divide & conquer).  

### Time Complexity
Recurrence:  
\[
T(n) = T(n/2) + O(1)
\]
Using **Master Theorem**, this gives  
\[
T(n) = O(\log n)
\]

That’s why it’s called “super fast” — we only multiply ~log₂(n) times.

### Result Example
For n = 10 → **F(10) = 55**

---

## Problem 2 — 0/1 Knapsack Algorithm

### Why not Greedy?
A greedy algorithm fails because choosing the locally best item (best value/weight ratio) may miss the global optimum.  
Example: one heavy but very valuable item can be skipped by greedy even if it gives the highest total value.

### Dynamic Programming Approach
We build a DP table where:

\[
dp[i][w] = \max(value_i + dp[i-1][w - weight_i], \ dp[i-1][w])
\]

Each cell represents the best value achievable using the first `i` items with capacity `w`.  

### Space Optimization
We can reduce memory from `O(n·W)` to **O(W)** by keeping only one DP row.

### Example
Weights = [2, 3, 4, 5]  
Values = [3, 4, 5, 6]  
Capacity = 5  

Result → **Max value = 7**, chosen items = `[1, 0]` (items 2 and 1)

---

## Problem 3 — Neuro Computing

### Setup
I generated **100 random binary vectors** of length `N`.  
Then computed two similarity measures between every pair:

\[
sim(x, y) = \frac{x \cdot y}{||x||_1 \ ||y||_1}
\]

\[
Jaccard(x, y) = \frac{|x \cap y|}{|x \cup y|}
\]

### Observation
When plotted, both similarity distributions look **Gaussian-like** (bell curve).  
When `N` increases, values concentrate closer to the mean — the variance shrinks.  
This is expected due to the **law of large numbers**.

### Sparse Vector Capacity
For a huge binary vector with N = 2000 and only w = 5 ones:

\[
\text{Possible combinations} = C(2000, 5)
\]

That’s an enormous number — roughly \(2.65 \times 10^{15}\).  
This can be interpreted as a form of “memory capacity”.

---

## Code Summary

All tasks were implemented in one Python file (`exo3.py`):

- **Fibonacci** via matrix exponentiation → O(log n)  
- **Knapsack** via dynamic programming → O(n·W)  
- **Neuro Computing** experiment using NumPy and Matplotlib  
- Included capacity computation via combinations.

---

## Conclusion

Each problem represents a core algorithmic technique:

| Problem | Technique | Complexity | Key Concept |
|----------|------------|-------------|--------------|
| Fibonacci | Divide & Conquer | O(log n) | Matrix exponentiation |
| Knapsack | Dynamic Programming | O(n·W) | Optimization |
| Neuro Computing | Vector Similarity | O(N²) | Statistical behavior of high-dim data |

The code works correctly, results match the theory, and complexity is optimal for each case.
