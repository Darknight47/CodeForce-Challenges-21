"""

---------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2204/B -----------------------------------

You are given an array a consisting of n integers.

While the array is not empty, an operation is performed consisting of two steps:

first, the maximum element in the array is chosen (if there are multiple maximum elements, the rightmost maximum is chosen);
then, all elements after the chosen element, including it, are removed from the array.
Your task is to calculate the number operations that will be performed before the array becomes empty.

Input
The first line contains one integer t (1 ≤ t ≤ 10^4) — the number of test cases.

Each test case consists of two lines:

the first line contains one integer n (2 ≤ n ≤ 2⋅10^5);
the second line contains n integers a1,a2,…,an (1≤ai≤n).
Additional constraint on the input: the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, print one integer — the number of operations that will be performed.

Input:
4
5
2 1 2 3 1
6
1 2 3 4 5 6
3
3 2 1
4
1 3 3 1

Output:
3
6
1
3
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    mx = 0
    ans = 0
    for i in range(n):
        if(arr[i] >= mx):
            ans += 1
        mx = max(mx, arr[i])
    print(ans)