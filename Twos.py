"""

------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1891/A ------------------------------------

You are given an array of integers a1,a2,…,an. In one operation, you do the following:

Choose a non-negative integer m, such that 2^m≤n.
Subtract 1 from ai for all integers i, such that 1≤i≤2^m.
Can you sort the array in non-decreasing order by performing some number (possibly zero) of operations?

An array is considered non-decreasing if ai≤ai+1 for all integers i such that 1≤i≤n−1.

Input
The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases. The description of the test cases follows.

The first line of each test case contains a single integer n (1 ≤ n ≤ 20) — the length of array a.

The second line of each test case contains n integers a1,a2,…,an — the integers in array a (0 ≤ ai ≤ 1000).

Output
For each test case, output "YES" if the array can be sorted, and "NO" otherwise.

Input:
8
5
1 2 3 4 5
5
6 5 3 4 4
9
6 5 5 7 5 6 6 8 7
4
4 3 2 1
6
2 2 4 5 3 2
8
1 3 17 19 27 57 179 13
5
3 17 57 179 92
10
1 2 3 4 0 6 7 8 9 10


Output:
YES
YES
YES
NO
NO
NO
YES
YES
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    diffs = [arr[i] - arr[i-1] for i in range(1, sze)]
    for i in range(len(diffs)):
        idx = i + 1
        if (idx & (idx - 1)) != 0 and diffs[i] < 0:
            print("NO")
            break
    else:
        print("YES")