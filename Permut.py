"""

------------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2137/B ---------------------------------------

You are given a permutation∗ p of size n.

Your task is to find a permutation q of size n such that GCD
† (pi+qi,pi+1+qi+1)≥3 for all 1≤i<n. In other words, the greatest common divisor of the sum of any two adjacent positions should be at least 3.

It can be shown that this is always possible.

∗ A permutation of length m is an array consisting of m distinct integers from 1 to m in arbitrary order. 
For example, [2,3,1,5,4] is a permutation, but [1,2,2] is not a permutation (2 appears twice in the array), and [1,3,4] is also not a permutation (m=3 but there is 4 in the array).

† gcd(x,y) denotes the greatest common divisor (GCD) of integers x and y.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^4). The description of the test cases follows.

The first line of each test case contains an integer n (2 ≤ n ≤ 2⋅10^5).

The second line contains n integers p1,p2,…,pn (1 ≤ pi ≤ n).

It is guaranteed that the given array forms a permutation.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, output the permutation q on a new line. If there are multiple possible answers, you may output any.

Input:
3
3
1 3 2
5
5 1 2 4 3
7
6 7 1 5 4 3 2

Output:
2 3 1
4 5 1 2 3
2 1 3 7 5 6 4
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    q = [0] * n
    for i in range(n):
        q[i] = n + 1 - arr[i]
    print(*q)