"""

------------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1709/B ------------------------------------------------

You are beta testing the new secret Terraria update. This update will add quests to the game!

Simply, the world map can be represented as an array of length n, where the i-th column of the world has height ai.

There are m quests you have to test. The j-th of them is represented by two integers sj and tj. 
In this quest, you have to go from the column sj to the column tj. At the start of the quest, you are appearing at the column sj.

In one move, you can go from the column x to the column x−1 or to the column x+1. 
In this version, you have Spectre Boots, which allow you to fly. Since it is a beta version, they are bugged, so they only allow you to fly when you are going up and have infinite fly duration. 
When you are moving from the column with the height p to the column with the height q, then you get some amount of fall damage. If the height p is greater than the height q, you get p−q fall damage, otherwise you fly up and get 0 damage.

For each of the given quests, determine the minimum amount of fall damage you can get during this quest.

Input
The first line of the input contains two integers n and m (2 ≤ n ≤ 10^5; 1 ≤ m ≤ 10^5) — the number of columns in the world and the number of quests you have to test, respectively.

The second line of the input contains n integers a1,a2,…,an (1 ≤ ai ≤ 10^9), where ai is the height of the i-th column of the world.

The next m lines describe quests. The j-th of them contains two integers sj and tj (1≤sj,tj≤n;sj≠tj), which means you have to move from the column sj to the column tj during the j-th quest.

Note that sj can be greater than tj.

Output
Print m integers. The j-th of them should be the minimum amount of fall damage you can get during the j-th quest completion.

Input:
7 6
10 8 9 6 8 12 7
1 2
1 7
4 6
7 1
3 5
4 2

Output:
2
10
0
7
3
1
"""
n, q = map(int, input().split())
arr = list(map(int, input().split()))

# Left → Right drops
pLR = [0] * (n + 1)
for i in range(n - 1):
    pLR[i+1] = pLR[i] + max(0, arr[i] - arr[i+1])

# Right → Left drops
pRL = [0] * (n + 1)
for i in range(n - 1, 0, -1):
    pRL[i-1] = pRL[i] + max(0, arr[i] - arr[i-1])

for _ in range(q):
    l, r = map(int, input().split())
    if l < r:
        print(pLR[r - 1] - pLR[l - 1])
    else:
        print(pRL[r - 1] - pRL[l - 1])