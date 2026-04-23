"""

------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1057/A ------------------------------------

Once upon a time there was only one router in the well-known company Bmail. Years went by and over time new routers were purchased. 
Every time they bought a new router, they connected it to one of the routers bought before it. 
You are given the values pi — the index of the router to which the i-th router was connected after being purchased (pi<i).

There are n routers in Boogle in total now. Print the sequence of routers on the path from the first to the n-th router.

Input
The first line contains integer number n (2 ≤ n ≤ 200000) — the number of the routers. 
The following line contains n−1 integers p2,p3,…,pn (1 ≤ pi < i), where pi is equal to index of the router to which the i-th was connected after purchase.

Output
Print the path from the 1-st to the n-th router. It starts with 1 and ends with n. All the elements in the path should be distinct.

Input:
8
1 1 2 2 3 2 5

Output:
1 2 5 8 
"""
n = int(input())
p = list(map(int, input().split()))
path = [n]
cur = n
# p[i] is the parent of router (i+2)
# because p[0] = parent of router 2
while cur != 1:
    cur = p[cur - 2]
    path.append(cur)
path.reverse()
print(*path)