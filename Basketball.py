"""

----------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1725/B -----------------------------------------

A basketball competition is held where the number of players in a team does not have a maximum or minimum limit (not necessarily 5 players in one team for each match). 
There are N candidate players in the competition that will be trained by Pak Chanek, the best basketball coach on earth. The i-th candidate player has a power of Pi.

Pak Chanek will form zero or more teams from the N candidate players on the condition that each candidate player may only join in at most one team. 
Each of Pak Chanek's teams will be sent to compete once with an enemy team that has a power of D. 
In each match, the team sent is said to defeat the enemy team if the sum of powers from the formed players is strictly greater than D.

One of Pak Chanek's skills is that when a team that has been formed plays in a match, he can change the power of each player in the team to be equal to the biggest player power from the team.

Determine the maximum number of wins that can be achieved by Pak Chanek.

Input
The first line contains two integers N and D (1 ≤ N ≤ 10^5, 1 ≤ D ≤ 10^9) — the number of candidate players and the power of the enemy team.

The second line contains N integers P1,P2,…,PN (1 ≤ Pi ≤ 10^9) — the powers of all candidate players.

Output
A line containing an integer representing the maximum number of wins that can be achieved by Pak Chanek.

Input:
6 180
90 80 70 60 50 100

Output:
2
"""
import math
n, d = map(int, input().split())
arr = sorted(list(map(int, input().split())))
teams = 0
idx = n - 1
while n > 0:
    temp_max = arr[idx]
    if(temp_max > d):
        teams += 1
        idx -= 1
        n -= 1
    else:
        temp = math.ceil(d / temp_max)
        if(d % temp_max == 0):
            temp += 1
        if(temp > n):
            break
        else:
            teams += 1
            idx -= 1
            n -= temp
print(teams)