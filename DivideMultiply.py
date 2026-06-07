"""

------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1609/A ---------------------------------

William has array of n numbers a1,a2,…,an. He can perform the following sequence of operations any number of times:

Pick any two items from array ai and aj, where ai must be a multiple of 2
ai=ai2
aj=aj⋅2
Help William find the maximal sum of array elements, which he can get by performing the sequence of operations described above.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^4). Description of the test cases follows.

The first line of each test case contains an integer n (1 ≤ n ≤ 15), the number of elements in William's array.

The second line contains n integers a1,a2,…,an (1 ≤ ai < 16), the contents of William's array.

Output
For each test case output the maximal sum of array elements after performing an optimal sequence of operations.

Input:
5
3
6 4 2
5
1 2 3 4 5
1
10
3
2 3 4
15
8 8 8 8 8 8 8 8 8 8 8 8 8 8 8

Output:
50
46
10
26
35184372088846
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    total_twos = 0
    odd_parts = []

    for x in arr:
        cnt = (x & -x).bit_length() - 1   # number of trailing zeros
        total_twos += cnt
        odd_parts.append(x >> cnt)

    odd_parts.sort()
    odd_parts[-1] <<= total_twos   # multiply largest odd part by all 2^k

    print(sum(odd_parts))