"""

------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/839/A -------------------------------------

Bran and his older sister Arya are from the same house. Bran like candies so much, so Arya is going to give him some Candies.

At first, Arya and Bran have 0 Candies. There are n days, at the i-th day, Arya finds ai candies in a box, that is given by the Many-Faced God. 
Every day she can give Bran at most 8 of her candies. If she don't give him the candies at the same day, they are saved for her and she can give them to him later.

Your task is to find the minimum number of days Arya needs to give Bran k candies before the end of the n-th day. 
Formally, you need to output the minimum day index to the end of which k candies will be given out (the days are indexed from 1 to n).

Print -1 if she can't give him k candies during n given days.

Input
The first line contains two integers n and k (1 ≤ n ≤ 100, 1 ≤ k ≤ 10000).

The second line contains n integers a1, a2, a3, ..., an (1 ≤ ai ≤ 100).

Output
If it is impossible for Arya to give Bran k candies within n days, print -1.

Otherwise print a single integer — the minimum number of days Arya needs to give Bran k candies before the end of the n-th day.

Input:
2 3
1 2

Output:
2
"""
n, k = map(int, input().split())
arr = list(map(int, input().split()))
given = 0
left_over = 0
days = 0
for candies in arr:
    candies += left_over
    if(candies > 8):
        given += 8
        left_over = candies - 8
    else:
        given += candies
        left_over = 0
    days += 1
    if(given >= k):
        print(days)
        break
if(given < k):
    print(-1)