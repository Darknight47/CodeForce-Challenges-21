"""

-------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1047/B ----------------------------------------

There are n points on the plane, (x1,y1),(x2,y2),…,(xn,yn).

You need to place an isosceles triangle with two sides on the coordinate axis to cover all points (a point is covered if it lies inside the triangle or on the side of the triangle). 
Calculate the minimum length of the shorter side of the triangle.

Input
First line contains one integer n (1 ≤ n ≤ 10^5).

Each of the next n lines contains two integers xi and yi (1 ≤ xi, yi ≤ 10^9).

Output
Print the minimum length of the shorter side of the triangle. It can be proved that it's always an integer.

Input:
3
1 1
1 2
2 1

Output:
3
"""
n = int(input())
ans = 0
for _ in range(n):
    x, y = map(int, input().split())
    ans = max(ans, (x + y))
print(ans)