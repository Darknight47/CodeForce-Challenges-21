"""

----------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2013/B -----------------------------------

Eralim, being the mafia boss, manages a group of n fighters. Fighter i has a rating of ai.

Eralim arranges a tournament of n−1 battles, in each of which two not yet eliminated fighters i and j (1 ≤ i < j ≤ n) are chosen, 
and as a result of the battle, fighter i is eliminated from the tournament, and the rating of fighter j is reduced by the rating of fighter i. That is, aj is decreased by ai. 
Note that fighter j's rating can become negative. The fighters indexes do not change.

Eralim wants to know what maximum rating the last remaining fighter can preserve if he chooses the battles optimally.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^4). 
The description of the test cases follows.

The first line of each test case contains a single integer n (2 ≤ n ≤ 2⋅10^5) — the number of fighters.

The second line of each test case contains n integers a1,a2,…an (1 ≤ ai ≤ 10^9) — the ratings of the fighters.

The sum of n over all testcases does not exceed 2⋅10^5.

Output
For each testcase, output a single integer — the maximum rating that the last remaining fighter can preserve.

Input:
5
2
2 1
3
2 2 8
4
1 2 4 3
5
1 2 3 4 5
5
3 2 4 5 4

Output:
-1
8
2
7
8
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    temp_sum = sum(arr)
    temp_max = arr[n - 2]
    ans = temp_sum - (2 * temp_max)
    print(ans)