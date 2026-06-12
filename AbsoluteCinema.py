"""

----------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2229/B ---------------------------  

You find yourself with two arrays of positive integers a and b, both of length n. You are to perform the following operation any number of times:

select an integer i (1 ≤ i ≤ n) and swap ai and bi.
Determine the maximum value of max(a)+∑ni=1bi attainable if you perform the operations optimally.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^4). The description of the test cases follows.

The first line of each testcase contains an integer n (1 ≤ n ≤ 10^5) — the length of the arrays a and b.

The second line of each testcase contains n integers a1,a2,…,an (1 ≤ ai ≤ 10^9).

The third line of each testcase contains n integers b1,b2,…,bn (1 ≤ bi ≤ 10^9).

It is guaranteed that the sum of n over all test cases does not exceed 10^5.

Output
For each testcase, output the maximum value of max(a)+∑ni=1bi attainable.

Input:
4
1
2
1
1
1
2
3
1 2 3
4 5 6
4
2 3 6 7
1 4 5 8

Output:
3
3
18
27
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))    
    current_max_a = 0
    b_sum = 0
    for i in range(n):
        if(arr[i] > brr[i]):
            # for b
            b_sum += arr[i]
            if(brr[i] > current_max_a):
                current_max_a = brr[i]
        else:
            # for a
            b_sum += brr[i]
            if(arr[i] > current_max_a):
                current_max_a = arr[i]
    print(b_sum + current_max_a)