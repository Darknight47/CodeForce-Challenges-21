"""

--------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1879/B ------------------------------

You are given a board of size n×n (n rows and n colums) and two arrays of positive integers a and b of size n.

Your task is to place the chips on this board so that the following condition is satisfied for every cell (i,j):

there exists at least one chip in the same column or in the same row as the cell (i,j). 
I. e. there exists a cell (x,y) such that there is a chip in that cell, and either x=i or y=j (or both).
The cost of putting a chip in the cell (i,j) is equal to ai+bj.

For example, for n=3, a=[1,4,1] and b=[3,2,2]. One of the possible chip placements is as follows:

The total cost of that placement is (1+3)+(1+2)+(1+2)=10.

Calculate the minimum possible total cost of putting chips according to the rules above.

Input
The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases.

The first line of each test case contains a single integer n (1 ≤ n ≤ 3⋅10^5).

The second line contains n integers a1,a2,…,an (1 ≤ ai ≤ 10^9).

The third line contains n integers b1,b2,…,bn (1 ≤ bi ≤ 10^9).

The sum of n over all test cases doesn't exceed 3⋅10^5.

Output
For each test case, print a single integer — the minimum possible total cost of putting chips according to the rules.

Input:
4
3
1 4 1
3 2 2
1
4
5
2
4 5
2 3
5
5 2 4 5 3
3 4 2 1 5

Output:
10
9
13
24
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    arr_min = min(arr)
    brr_min = min(brr)
    temp_sum = sum(brr)
    ans1 = temp_sum + (n * arr_min)
    temp_sum = sum(arr)
    ans2 = temp_sum + (n * brr_min)
    print(min(ans1, ans2))