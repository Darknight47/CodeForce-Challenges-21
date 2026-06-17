"""

------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1562/A ----------------------------------

You are given two integers l and r, l≤r. Find the largest possible value of amodb over all pairs (a,b) of integers for which r ≥ a ≥ b ≥ l.

As a reminder, a mod b is a remainder we get when dividing a by b. For example, 26mod8=2.

Input
Each test contains multiple test cases.

The first line contains one positive integer t (1 ≤ t ≤ 10^4), denoting the number of test cases. Description of the test cases follows.

The only line of each test case contains two integers l, r (1 ≤ l ≤ r ≤ 10^9).

Output
For every test case, output the largest possible value of a mod b over all pairs (a,b) of integers for which r ≥ a ≥ b ≥ l.

Input:
4
1 1
999999999 1000000000
8 26
1 999999999

Output:
0
1
12
499999999
"""
cases = int(input())
for _ in range(cases):
    l, r = map(int, input().split())
    b = (r - 1) // 2
    if(l * 2 > r):
        print(r - l)
    else:
        print(b)