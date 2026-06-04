"""

---------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1904/A ----------------------------------------

Lunchbox is done with playing chess! His queen and king just got forked again!

In chess, a fork is when a knight attacks two pieces of higher value, commonly the king and the queen. 
Lunchbox knows that knights can be tricky, and in the version of chess that he is playing, knights are even trickier: 
instead of moving 1 tile in one direction and 2 tiles in the other, knights in Lunchbox's modified game move a tiles in one direction and b tiles in the other.

Lunchbox is playing chess on an infinite chessboard which contains all cells (x,y) where x and y are (possibly negative) integers. 
Lunchbox's king and queen are placed on cells (xK,yK) and (xQ,yQ) respectively. 
Find the number of positions such that if a knight was placed on that cell, it would attack both the king and queen.

Input
Each test contains multiple test cases. The first line contains an integer t (1 ≤ t ≤ 1000) — the number of test cases. The description of the test cases follows.

The first line of each test case contains two integers a and b (1 ≤ a, b ≤ 10^8) — describing the possible moves of the knight.

The second line of each test case contains two integers xK and yK (0 ≤ xK, yK ≤ 10^8) — the position of Lunchbox's king.

The third line in a test case contains xQ and yQ (0 ≤ xQ, yQ ≤ 10^8) — the position of Lunchbox's queen.

It is guaranteed that Lunchbox's queen and king will occupy different cells. That is, (xK,yK)≠(xQ,yQ).

Output
For each test case, output the number of positions on an infinite chessboard such that a knight can attack both the king and the queen.

Input:
4
2 1
0 0
3 3
1 1
3 1
1 3
4 4
0 0
8 0
4 2
1 4
3 4

Output:
2
1
2
0
"""
cases = int(input())
for _ in range(cases):
    a, b = map(int, input().split())
    xk, yk = map(int, input().split())
    xq, yq = map(int, input().split())
    king_positions = [(xk + a, yk + b), (xk + a, yk - b), (xk - a, yk + b), (xk - a, yk - b),
            (xk + b, yk + a), (xk + b, yk - a), (xk - b, yk + a), (xk - b, yk - a)]
    queen_positions = [(xq + a, yq + b), (xq + a, yq - b), (xq - a, yq + b), (xq - a, yq - b),
            (xq + b, yq + a), (xq + b, yq - a), (xq - b, yq + a), (xq - b, yq - a)]
    # number of equal unique positions between the knight and the queen
    count = len(set(king_positions) & set(queen_positions))
    print(count)