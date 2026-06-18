"""

----------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1981/A ----------------------------------

Turtle and Piggy are playing a number game.

First, Turtle will choose an integer x, such that l≤x≤r, where l,r are given. It's also guaranteed that 2l≤r.

Then, Piggy will keep doing the following operation until x becomes 1:

Choose an integer p such that p≥2 and p∣x (i.e. x is a multiple of p).
Set x to xp, and the score will increase by 1.
The score is initially 0. Both Turtle and Piggy want to maximize the score. Please help them to calculate the maximum score.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^4). The description of the test cases follows.

The first line of each test case contains two integers l,r (1 ≤ l ≤ r ≤ 10^9, 2l ≤ r) — The range where Turtle can choose the integer from.

Output
For each test case, output a single integer — the maximum score.

Input:
5
2 4
3 6
2 15
6 22
114514 1919810

Output:
2
2
3
4
20
"""
cases = int(input())
for _ in range(cases):
    L, R = map(int, input().split())
    if L == R:
        print((L & -L).bit_length() - 1)
    
    # XOR shows which bits change between L and R
    diff = L ^ R
    
    # Find the position of the highest bit that changed
    highest_changed_bit_pos = diff.bit_length() - 1
    
    best_num = (R >> highest_changed_bit_pos) << highest_changed_bit_pos
    
    print((best_num & -best_num).bit_length() - 1)