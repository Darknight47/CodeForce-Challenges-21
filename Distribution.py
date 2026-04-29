"""

--------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2226/A ---------------------------------------------

You are given an array [a1,a2,…,an]. You wish to make the array empty by performing the following operation any number of times:

Select any sequence of indices 1≤i1<i2<…<ik≤|a| (note that |a| denotes the current length of the array a) such that
ai1 ≤ ai2 ≤ … ≤ aik
Remove the elements ai1,ai2,…,aik from the array a.
This operation incurs a cost equal to ai1×ai2×⋯×aik.
Determine the minimum total cost required to remove all the elements from the array a. 
Note that the total cost is equal to the sum of costs incurred over all the operations performed.

As the answer can be very large, report the answer modulo 676767677.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 500). The description of the test cases follows.

The first line of each testcase contains a single integer n (1 ≤ n ≤ 100) — the length of the array a.

The second line of each testcase contains n integers a1,a2,…,an (1 ≤ ai ≤ 100) — the elements of the array.

Output
For each testcase, output a single integer — the minimum total cost required to make the array a empty.

As the answer may be large, output the answer modulo 676767677.

Input:
3
5
1 2 1 2 3
3
3 2 1
4
1 1 1 1

Output:
7
6
1
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    for num in arr:
        if(num != 1):
            ans += num
    if(arr[-1] == 1):
        ans += 1 
    print(ans)