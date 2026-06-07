"""

------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1951/A -------------------------------------

There are n lamps numbered 1 to n lined up in a row, initially turned off. You can perform the following operation any number of times (possibly zero):

Choose two non-adjacent† lamps that are currently turned off, then turn them on.
Determine whether you can reach configuration s, where si=1 means the i-th lamp is turned on, and si=0 otherwise.

† Only lamp i and i+1 are adjacent for all 1≤i<n. Note that lamp n and 1 are not adjacent when n≠2.

Input
Each test contains multiple test cases. The first line contains an integer t (1 ≤ t ≤ 1000) — the number of test cases. The description of the test cases follows.

The first line of each test case contains an integer n (1 ≤ n ≤ 50) — the number of lamps.

The second line of each test case contains a binary string s of size n — the final desired configuration.

Output
For each test case, print on one line "YES" if we can reach the configuration s via applying the given operation any number of times. Otherwise, print "NO".

Input:
5
10
1101010110
10
1001001110
6
000000
1
1
12
111111111111

Output:
YES
NO
YES
NO
YES
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    s = input()
    cnt = 0
    mi = n
    mx = -1

    for i in range(n):
        if s[i] == '1':
            cnt += 1
            mi = min(mi, i)
            mx = max(mx, i)

    if cnt % 2 == 1 or (cnt == 2 and mx - mi == 1):
        print("NO")
    else:
        print("YES")