"""

------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1845/B -------------------------------------------

Bob and Carol hanged out with Alice the whole day, but now it's time to go home. Alice, Bob and Carol live on an infinite 2D grid in cells A, B, and C respectively. Right now, all of them are in cell A.

If Bob (or Carol) is in some cell, he (she) can move to one of the neighboring cells. 
Two cells are called neighboring if they share a side. For example, the cell (3,5) has four neighboring cells: (2,5), (4,5), (3,6) and (3,4).

Bob wants to return to the cell B, Carol — to the cell C. 
Both of them want to go along the shortest path, i. e. along the path that consists of the minimum possible number of cells. But they would like to walk together as well.

What is the maximum possible number of cells that Bob and Carol can walk together if each of them walks home using one of the shortest paths?

Input
The first line contains the single integer t (1 ≤ t ≤ 10^4) — the number of test cases.

The first line of each test case contains two integers xA and yA (1 ≤ xA, yA ≤ 10^8) — the position of cell A, where both Bob and Carol are right now.

The second line contains two integers xB and yB (1 ≤ xB, yB ≤ 10^8) — the position of cell B (Bob's house).

The third line contains two integers xC and yC (1 ≤ xC, yC ≤ 10^8) — the position of cell C (Carol's house).

Additional constraint on the input: the cells A, B, and C are pairwise distinct in each test case.

Output
For each test case, print the single integer — the maximum number of cells Bob and Carol can walk together if each of them goes home along one of the shortest paths.

Input:
3
3 1
1 3
6 4
5 2
2 2
7 2
1 1
4 3
5 5

Output:
3
1
6
"""
cases = int(input())
for _ in range(cases):
    a1, a2 = map(int, input().split())
    b1, b2 = map(int, input().split())
    c1, c2 = map(int, input().split())
    b_left = False
    c_left = False
    ans = 1
    b_down = False
    c_down = False
    if(b1 < a1):
        b_left = True
    if(c1 < a1):
        c_left = True
    if(b_left and c_left or not b_left and not c_left):
        diff1 = abs(a1 - b1)
        diff2 = abs(a1 - c1)
        ans += min(diff1, diff2)
    if(b2 < a2):
        b_down = True
    if(c2 < a2):
        c_down = True
    if(b_down and c_down or not b_down and not c_down):
        diff1 = abs(a2 - b2)
        diff2 = abs(a2 - c2)
        ans += min(diff1, diff2)
    print(ans)