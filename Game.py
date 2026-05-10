"""

-------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2060/C --------------------------------------

Alice and Bob are playing a game. There are n (n is even) integers written on a blackboard, represented by x1,x2,…,xn. 
There is also a given integer k and an integer score that is initially 0. 
The game lasts for n2 turns, in which the following events happen sequentially:

Alice selects an integer from the blackboard and erases it. Let's call Alice's chosen integer a.
Bob selects an integer from the blackboard and erases it. Let's call Bob's chosen integer b.
If a+b=k, add 1 to score.
Alice is playing to minimize the score while Bob is playing to maximize the score. Assuming both players use optimal strategies, what is the score after the game ends?

Input
The first line contains an integer t (1 ≤ t ≤ 10^4) — the number of test cases.

The first line of each test case contains two integers n and k (2 ≤ n ≤ 2⋅10^5, 1 ≤ k ≤ 2⋅n, n is even).

The second line of each test case contains n integers x1,x2,…,xn (1 ≤ xi ≤ n) — the integers on the blackboard.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, output the score if both players play optimally.

Input:
4
4 4
1 2 3 2
8 15
1 2 3 4 5 6 7 8
6 1
1 1 1 1 1 1
16 9
3 1 4 1 5 9 2 6 5 3 5 8 9 7 9 3

Output:
2
1
0
4
"""
cases = int(input())

for _ in range(cases):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    freq = [0] * (k + 1)

    for x in arr:
        if x < k:
            freq[x] += 1

    ans = 0

    for i in range(1, (k // 2) + 1):
        if i == k - i:
            ans += freq[i] // 2
        else:
            m = min(freq[i], freq[k - i])
            ans += m

    print(ans)