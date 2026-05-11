"""

----------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1954/A -----------------------------------------

Alice and Bob have bought a ribbon consisting of n parts. Now they want to paint it.

First, Alice will paint every part of the ribbon into one of m colors. For each part, she can choose its color arbitrarily.

Then, Bob will choose at most k parts of the ribbon and repaint them into the same color (he chooses the affected parts and the color arbitrarily).

Bob would like all parts to have the same color. However, Alice thinks that this is too dull, so she wants to paint the ribbon in such a way that Bob cannot make all parts have the same color.

Is it possible to paint the ribbon in such a way?

Input
The first line contains one integer t (1 ≤ t ≤ 1000) — the number of test cases.

Each test case consists of one line containing three integers n , m and k (1 ≤ m, k ≤ n ≤ 50) — the number of parts, the number of colors and the number of parts Bob can repaint, respectively.

Output
For each test case, print YES if Alice can paint the ribbon so that Bob cannot make all parts have the same color. Otherwise, print NO.

You can print every letter in any register. For example, Yes, yes, yEs will all be recognized as positive answer.

Input:
5
1 1 1
5 1 1
5 2 1
5 2 2
5 5 3

Output:
NO
NO
YES
NO
YES
"""
import math
cases = int(input())
for _ in range(cases):
    n, m, k = map(int, input().split())
    if(m == 1):
        print("NO")
    else:
        x = math.ceil(n / m)
        print("YES" if x + k < n else "NO")