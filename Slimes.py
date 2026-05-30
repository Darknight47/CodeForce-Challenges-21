"""

------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2229/A -------------------------------------

There are n slimes on a line, where slime i is at position ai on the line. You will perform the following operation some number of times (possibly none):

select an integer x, then for each j (1 ≤ j ≤ n):
if aj<x then do aj:=aj+1.
if aj>x then do aj:=aj−1.
if aj=x then do nothing.
Determine the minimum number of operations to make all slimes occupy the same position.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 100). The description of the test cases follows.

The first line of each testcase contains an integer n (2 ≤ n ≤ 1000) — the number of slimes.

The second line of each testcase contains n integers a1,a2,…,an (1 ≤ ai ≤ 1000) — the initial positions of the slimes.

It is guaranteed that the sum of n over all test cases does not exceed 1000.

Output
For each testcase, output the minimum number of operations required to make all slimes occupy the same position.

Input:
10
5
1 2 3 4 5
5
3 3 3 3 3
6
5 6 7 1 2 3
2
2 5
4
1 3 8 7
4
6 2 1 8
3
1 3 9
5
1 10 1 10 10
8
10 8 5 9 1 6 9 10
2
1 1000

Output:
2
0
3
2
4
4
4
5
5
500
"""
import math
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    temp_max = max(arr)
    temp_min = min(arr)
    ans = math.ceil((temp_max - temp_min) / 2) 
    print(ans)