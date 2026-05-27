"""

--------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/11/A ---------------------------------------

A sequence a0, a1, ..., at - 1 is called increasing if ai - 1 < ai for each i: 0 < i < t.

You are given a sequence b0, b1, ..., bn - 1 and a positive integer d. In each move you may choose one element of the given sequence and add d to it. 
What is the least number of moves required to make the given sequence increasing?

Input
The first line of the input contains two integer numbers n and d (2 ≤ n ≤ 2000, 1 ≤ d ≤ 10^6). 
The second line contains space separated sequence b0, b1, ..., bn - 1 (1 ≤ bi ≤ 106).

Output
Output the minimal number of moves needed to make the sequence increasing.

Input:
4 2
1 3 3 2

Output:
3
"""
import math

sze, d = map(int, input().split())
arr = list(map(int, input().split()))
ops = 0
for i in range(sze - 1):
    l = arr[i]
    r = arr[i + 1]
    if(r <= l):
        diff = l - r
        temp = math.ceil(diff / d)
        new_val = r + temp * d
        if(temp == 0 or new_val <= l):
            temp += 1
        ops += temp
        arr[i + 1] += temp * d
print(ops)