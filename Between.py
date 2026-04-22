"""

----------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2225/A -----------------------------------

You are given two integers x and y such that y>x and y mod x =0 (that is, y is divisible by x).

Your task is to determine whether there exists an integer z such that

z lies between x and y (that is, x < z < y);
z is divisible by x (that is, z mod x = 0);
y is not divisible by z (that is, y mod z ≠ 0).
Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^4). The description of the test cases follows.

Each test case consists of a single line containing two integers x and y (1 ≤ x < y ≤ 10^18; y mod x=0).

Output
For each test case, print the answer as follows: if the required number z exists, print YES; otherwise, print NO. You may print each letter in any case.

Input:
5
1 2
1 3
1234567890 12345678900
2 8
7 84

Output:
NO
YES
YES
YES
YES
"""
cases = int(input())
for _ in range(cases):
    x, y = map(int, input().split())
    if y >= 3 * x:
        print("YES")
    else:
        print("NO")