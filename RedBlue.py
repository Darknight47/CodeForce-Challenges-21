"""

------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1659/A -------------------------------------------

Team Red and Team Blue competed in a competitive FPS. Their match was streamed around the world. They played a series of n matches.

In the end, it turned out Team Red won r times and Team Blue won b times. Team Blue was less skilled than Team Red, so b was strictly less than r.

You missed the stream since you overslept, but you think that the match must have been neck and neck since so many people watched it. 
So you imagine a string of length n where the i-th character denotes who won the i-th match  — it is R if Team Red won or B if Team Blue won. 
You imagine the string was such that the maximum number of times a team won in a row was as small as possible. 
For example, in the series of matches RBBRRRB, Team Red won 3 times in a row, which is the maximum.

You must find a string satisfying the above conditions. If there are multiple answers, print any.

Input
The first line contains a single integer t (1 ≤ t ≤ 1000)  — the number of test cases.

Each test case has a single line containing three integers n, r, and b (3 ≤ n ≤ 100; 1 ≤ b < r ≤ n, r + b =n).

Output
For each test case, output a single line containing a string satisfying the given conditions. If there are multiple answers, print any.

Input:
3
7 4 3
6 5 1
19 13 6

Output:
RBRBRBR
RRRBRR
RRBRRBRRBRRBRRBRRBR
"""
cases = int(input())
for _ in range(cases):
    n, r, b = map(int, input().split())
    buckets = b + 1
    base = r // buckets
    extra = r % buckets
    result = []
    for i in range(buckets):
        size = base + (1 if i < extra else 0)
        result.append('R' * size)
    print('B'.join(result))