"""

----------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1717/A -----------------------------------

Madoka is a very strange girl, and therefore she suddenly wondered how many pairs of integers (a,b) exist, where 1≤a,b≤n, for which lcm(a,b)gcd(a,b)≤3.

In this problem, gcd(a,b) denotes the greatest common divisor of the numbers a and b, and lcm(a,b) denotes the smallest common multiple of the numbers a and b.

Input
The input consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases. Description of the test cases follows.

The first and the only line of each test case contains the integer n (1 ≤ n ≤ 10^8).

Output
For each test case output a single integer — the number of pairs of integers satisfying the condition.

Input:
6
1
2
3
4
5
100000000

Output:
1
4
7
10
11
266666666
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    ans = n + 2 * ((n // 2) + (n // 3))
    print(ans)