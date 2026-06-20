"""


--------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2140/B --------------------------

Alice and Bob are playing a game in which Alice has given Bob a positive integer x<108.

To win the game, Bob has to find another positive integer y<109 such that x#y is divisible by x+y.

Here x#y denotes the integer formed by concatenating the integers x and y in that order. For example, if x=835, y=47, then x#y=83547.

However, since Bob is dumb, he is unable to find such an integer. Please help him.

It can be shown that such an integer always exists.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^4). The description of the test cases follows.

The only line of each test case contains a single integer x (1 ≤ x < 10^8) — the integer that Alice has given to Bob.

Output
For each test case, print a single integer y (1 ≤ y < 10^9) so that Bob can win the game.

If there are multiple answers, print any one of them.

Input:
6
8
42
1000
66666
106344
9876543

Output:
1
12
998
7872
8190
174036
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    print(n)