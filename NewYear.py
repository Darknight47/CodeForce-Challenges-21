"""

----------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1106/C -----------------------------------------

Lunar New Year is approaching, and Bob is struggling with his homework – a number division problem.

There are n positive integers a1,a2,…,an on Bob's homework paper, where n is always an even number. 
Bob is asked to divide those numbers into groups, where each group must contain at least 2 numbers. 
Suppose the numbers are divided into m groups, and the sum of the numbers in the j-th group is sj. 
Bob's aim is to minimize the sum of the square of sj, that is

Bob is puzzled by this hard problem. Could you please help him solve it?

Input
The first line contains an even integer n (2 ≤ n ≤ 3⋅10^5), denoting that there are n integers on Bob's homework paper.

The second line contains n integers a1,a2,…,an (1 ≤ ai ≤ 10^4), describing the numbers you need to deal with.

Output
A single line containing one integer, denoting the minimum of the sum of the square of sj.

Input:
4
8 5 2 3

Output:
164
"""
n = int(input())
arr = sorted(list(map(int, input().split())))
i, j = 0, n-1
ans = 0
while i < j:
    temp_sum = (arr[i] + arr[j])**2
    ans += temp_sum
    i += 1
    j -= 1
print(ans)