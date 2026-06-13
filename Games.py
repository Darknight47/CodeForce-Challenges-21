"""

--------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2236/A -----------------------------------

Dabir, Egor, and Arseniy just got on the train and decided to play a game. Dabir has a backpack with an infinite number of cubes. He built n towers from them, where the i-th tower has height hi cubes.

Egor and Arseniy must choose an integer xi for each tower i and increase its height by xi exactly once. 
For example, if h = [1,3,2,2], x = [3,2,2,8], then after increasing h it will become [4,5,4,10]. Their goal is to make the heights of all towers equal.

To make the game more interesting, Dabir wants to choose an integer k and add a restriction: each xi must satisfy 1≤xi≤k. 
Help him find the smallest k for which it is possible to finish the game.

Input
The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases.

Then t test cases follow.

The first line of each test case contains a single integer n (1 ≤ n ≤ 5).

The second line contains n integers h1,h2,…,hn (1 ≤ hi ≤ 6).

Output
For each test case, output a single integer — the minimum value of k such that it is possible to make all towers have equal height.

Input:
4
2
1 3
3
2 6 4
5
5 4 6 6 1
4
3 3 3 3

Output:
3
5
6
1
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    temp_max = max(arr) + 1
    temp_min = min(arr)
    print(temp_max - temp_min)