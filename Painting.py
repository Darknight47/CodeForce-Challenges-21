"""


-------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2175/A --------------------------------------

The little fairy has a ribbon with 10^18 cells and an infinite variety of colors. 
The first n cells of the ribbon have already been colored, where the i-th cell is colored with color ai.

Little fairy will color the remaining cells in order from n+1 to 10^18. For the i-th cell:

Little fairy first counts the number of distinct colors currently present on the ribbon, denoted as ci.
Then she will color the i-th cell with color ci.
What color will the fairy use for the 10^18-th cell?

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 500). The description of the test cases follows.

The first line of each test case contains a single integer n (1 ≤ n ≤ 100) — the number of colored cells.

The second line of each test case contains n integers a1,a2,…,an (1 ≤ ai ≤ 10^3) — the colors of the cells.

Output
For each test case, print the color of the last cell.

Input:
5
6
1 1 1 1 1 1
1
1000
5
8 10 15 20 25
8
2 5 2 4 1 2 5 3
6
40 4 1 95 8 40

Output:
1
1000
8
5
8
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    temp_set = set(arr)
    d = len(temp_set)
    if(d == 1):
        print(temp_set.pop())
    else:
        # while True:
        #     if(d not in arr):
        #         arr.append(d)
        #         temp_set.add(d)
        #     else:
        #         print(d)
        #         break
        #     d += 1
        sorted_arr = sorted(temp_set)
        for num in sorted_arr:
            if(num >= d):
                print(num)
                break