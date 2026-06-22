"""

---------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1864/A -------------------------

You are given three integers x, y, and n.

Your task is to construct an array a consisting of n integers which satisfies the following conditions:

a1=x, an=y; 
a is strictly increasing (i.e. a1<a2<…<an);
if we denote bi=ai+1−ai for 1≤i≤n−1, then b is strictly decreasing (i.e. b1>b2>…>bn−1).
If there is no such array a, print a single integer −1.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 1000). The description of the test cases follows.

The only line of each test case contains three integers x, y, n (1 ≤ x < y ≤ 1000, 3 ≤ n ≤ 1000).

Output
For each test case, output n integers a1,a2,…,an. If there are multiple solutions, print any of them.

If there is no solution, print a single integer −1.

Input:
3
1 4 3
1 3 3
100 200 4

Output:
1 3 4
-1
100 150 180 200
"""
cases = int(input())
for _ in range(cases):
    x, y, n = map(int, input().split())
    ans = [y]
    diff = 1
 
    for _ in range(n - 1, 0, -1):
        temp = ans[-1] - diff
        ans.append(temp)
        diff += 1
    ans.reverse()
    if(ans[0] < x):
        print(-1)
    else:
        ans[0] = x
        print(*ans)