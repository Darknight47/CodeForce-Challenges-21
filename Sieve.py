"""

------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2195/A ----------------------------------

You are given n positive integers a1,a2,…,an.

Please determine if it is possible to select any number of elements in a, so that their product is 67.

Note that you may not select zero elements, as the product of zero elements is not defined in this problem.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^4). The description of the test cases follows.

The first line of each test case contains a single integer n (1 ≤ n ≤ 5).

The second line of each test case contains n positive integers a1,a2,…,an (1 ≤ ai ≤ 67).

Output
If it is possible to select elements so that their product is 67, output "YES" on one line. Otherwise, output "NO" on one line.

You can output the answer in any case. For example, the strings "yEs", "yes", and "Yes" will also be recognized as positive responses.

Input:
2
5
1 7 6 7 67
5
1 3 5 7 8

Output:
YES
NO
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    sixseven = arr.count(67)
    if(sixseven > 0):
        print("YES")
    else:
        print("NO")