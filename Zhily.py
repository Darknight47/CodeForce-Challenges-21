"""


---------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2224/A ----------------------------------------

Deep in the wilderness, Zhily and Jily discovered a series of gathering places that contain abstract logic. 
Some of these gathering places harbor inconsistent errors in their logic, which may collapse at any moment. 
They hope to transmit logic between adjacent gathering places through reasonable transfer arrangements so that as many gathering places as possible can eventually restore logical stability.

You are given an array a of n integers. You can perform the following operation any number of times:

Choose an index i (1 ≤ i < n) and assign ai←ai+ai+1.
Each index can be chosen at most once.

Find the maximum number of positive integers in the final array after all operations.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^4). The description of the test cases follows.

The first line of each test case contains a single integer n (2 ≤ n ≤ 2⋅10^5).

The second line of each test case contains n integers a1,a2,…,an (−10^9 ≤ ai ≤ 10^9).

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, you should output a single line containing an integer k, the number of positive numbers in the final sequence.

Input:
4
5
0 -1 3 -3 0
5
0 -2 1 2 3
5
0 1 0 1 0
2
1000000000 -1000000000

Output:
3
5
4
1
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    # looping from right to left, adding arr[i] + arr[i - 1]  to arr[i - 1]
    # counting how many positive number are in the end
    count = 0
    for i in range(n - 1, 0, -1):
        first = arr[i - 1]
        second = arr[i]
        temp = first + second
        if(temp > first):
            arr[i - 1] = temp
        if arr[i] > 0:
            count += 1
    if(arr[0] > 0):
        count += 1
    print(count)