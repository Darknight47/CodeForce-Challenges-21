"""

---------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1326/B ------------------------------------------------

Alicia has an array, a1,a2,…,an, of non-negative integers. For each 1≤i≤n, she has found a non-negative integer xi=max(0,a1,…,ai−1). Note that for i=1, xi=0.

For example, if Alicia had the array a={0,1,2,0,3}, then x={0,0,1,2,2}.

Then, she calculated an array, b1,b2,…,bn: bi=ai−xi.

For example, if Alicia had the array a={0,1,2,0,3}, b={0−0,1−0,2−1,0−2,3−2}={0,1,1,−2,1}.

Alicia gives you the values b1,b2,…,bn and asks you to restore the values a1,a2,…,an. Can you help her solve the problem?

Input
The first line contains one integer n (3 ≤ n ≤ 200000) – the number of elements in Alicia's array.

The next line contains n integers, b1,b2,…,bn (−10^9 ≤ bi ≤ 10^9).

It is guaranteed that for the given array b there is a solution a1,a2,…,an, for all elements of which the following is true: 0 ≤ ai ≤ 10^9.

Output
Print n integers, a1,a2,…,an (0 ≤ ai ≤ 10^9), such that if you calculate x according to the statement, b1 will be equal to a1−x1, b2 will be equal to a2−x2, ..., and bn will be equal to an−xn.

It is guaranteed that there exists at least one solution for the given tests. It can be shown that the solution is unique.

Input:
5
0 1 1 -2 1

Output:
0 1 2 0 3
"""
n = int(input())
arr = list(map(int, input().split()))
a = [0] * n
mx = 0

for i in range(n):
    a[i] = arr[i] + mx
    mx = max(mx, a[i])
print(*a)