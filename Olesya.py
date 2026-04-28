"""

--------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/584/A ---------------------------------

Olesya loves numbers consisting of n digits, and Rodion only likes numbers that are divisible by t. Find some number that satisfies both of them.

Your task is: given the n and t print an integer strictly larger than zero consisting of n digits that is divisible by t. If such number doesn't exist, print  - 1.

Input
The single line contains two numbers, n and t (1 ≤ n ≤ 100, 2 ≤ t ≤ 10) — the length of the number and the number it should be divisible by.

Output
Print one such positive number without leading zeroes, — the answer to the problem, or  - 1, if such number doesn't exist. 
If there are multiple possible answers, you are allowed to print any of them.

Input:
3 2

Output:
200
"""
digits, delbar = map(int, input().split())

if delbar == 10:
    if digits == 1:
        print(-1)
    else:
        print("1" * (digits - 1) + "0")
else:
    s = str(delbar) * digits
    modified = int(s)

    if modified % delbar == 0 and len(s) == digits:
        print(modified)
    else:
        print(-1)
