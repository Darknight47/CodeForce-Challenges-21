"""


--------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1462/C -----------------------------------

You are given a positive number x. Find the smallest positive integer number that has the sum of digits equal to x and all digits are distinct (unique).

Input
The first line contains a single positive integer t (1 ≤ t ≤ 50) — the number of test cases in the test. Then t test cases follow.

Each test case consists of a single integer number x (1 ≤ x ≤ 50).

Output
Output t answers to the test cases:

if a positive integer number with the sum of digits equal to x and all digits are different exists, print the smallest such number;
otherwise print -1.

Input:
4
1
5
15
50

Output:
1
5
69
-1
"""
cases = int(input())
for _ in range(cases):
    x = int(input())
    if(x > 45):
        print(-1)
        continue
    digits = []
    for d in range(9, 0, -1):
        if x >= d:
            digits.append(d)
            x -= d

    digits.sort()
    print(int("".join(str(d) for d in digits)))