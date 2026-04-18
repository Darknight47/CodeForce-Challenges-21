"""

------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1585/B ------------------------------------------

You are given an array a of length n.

Let's define the eversion operation. Let x=an. 
Then array a is partitioned into two parts: left and right. The left part contains the elements of a that are not greater than x (≤x). 
The right part contains the elements of a that are strictly greater than x (>x). The order of elements in each part is kept the same as before the operation, 
i. e. the partition is stable. Then the array is replaced with the concatenation of the left and the right parts.

For example, if the array a is [2,4,1,5,3], the eversion goes like this: [2,4,1,5,3]→[2,1,3],[4,5]→[2,1,3,4,5].

We start with the array a and perform eversions on this array. We can prove that after several eversions the array a stops changing. 
Output the minimum number k such that the array stops changing after k eversions.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 100). Description of the test cases follows.

The first line contains a single integer n (1 ≤ n ≤ 2⋅10^5).

The second line contains n integers a1,a2,…,an (1 ≤ ai ≤ 10^9).

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case print a single integer k — the number of eversions after which the array stops changing.

Input:
3
5
2 4 1 5 3
5
5 3 2 4 1
4
1 1 1 1

Output:
1
2
0
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    cur = arr[-1]
    k = 0
    for i in range(n - 2, -1, -1):
        if arr[i] > cur:
            k += 1
            cur = arr[i]
    print(k)