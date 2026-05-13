"""

--------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1326/A  ---------------------------------------

You are given a integer n (n > 0). Find any integer s which satisfies these conditions, or report that there are no such numbers:

In the decimal representation of s:
s > 0,
s consists of n digits,
no digit in s equals 0,
s is not divisible by any of it's digits.

Input
The input consists of multiple test cases. The first line of the input contains a single integer t (1 ≤ t ≤ 400), the number of test cases. The next t lines each describe a test case.

Each test case contains one positive integer n (1 ≤ n ≤ 10^5).

It is guaranteed that the sum of n for all test cases does not exceed 10^5.

Output
For each test case, print an integer s which satisfies the conditions described above, or "-1" (without quotes), if no such number exists. 
If there are multiple possible solutions for s, print any solution.

Input:
4
1
2
3
4

Output:
-1
57
239
6789
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    if(n == 1):
        print(-1)
    else:
        result = '2'
        result += '3' * (n - 1)
        print(result)