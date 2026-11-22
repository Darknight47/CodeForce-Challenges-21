"""

------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/2288/A -----------------------------------

Youmu Konpaku is dueling a youkai. The youkai has x health, and Youmu's attack power is 1.

In one move Youmu does one of the following:

Charge: gain one stack. Each stack increases her attack power by 1.
Attack: deal damage equal to her current attack power to the youkai, then the number of stacks decreases by 1 (if she has any).
The youkai is defeated once its health becomes 0 or less. Find the minimum number of moves Youmu needs.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 100). The description of the test cases follows.

Each of the next t lines contains a single integer x (1 ≤ x ≤ 10^4) — the health of the youkai.

Output
For each test case, output a single integer — the minimum number of moves.

Input:
6
1
2
3
4
10
10000

Output:
1
2
3
4
7
244
"""
import math
cases = int(input())
for _ in range(cases):
    x = int(input())
    k_opt = math.isqrt(2 * x // 3)
    best = float("inf")
    for k in range(max(1, k_opt - 2), k_opt + 10):
        # Minimum starting coins s needed so k payments cover x
        s = (x + k * (k - 1) // 2 + k - 1) // k
        if s >= k:
            best = min(best, s - 1 + k)
    print(best)