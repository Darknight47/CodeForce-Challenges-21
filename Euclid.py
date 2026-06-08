"""


------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2234/A  ---------------------------------

We define a Euclid algorithm sequence of length k (k≥2) for two positive integers x≥y as the following sequence of positive integers:

a1,a2,…,ak, where a1=x, a2=y, and for any i (1≤i≤k−2), the equality ai+2=(aimodai+1) holds∗.
For example, for x=13,y=8,k=4, the corresponding Euclid algorithm sequence is a=[13,8,5,3]. (a3=13mod8=5, a4=8mod5=3).

You are given a sequence b1,b2,…,bn. 
You need to determine whether it is possible to permute its elements so that it becomes a Euclid algorithm sequence for some two positive integers x≥y.

∗ x mod y denotes the remainder when x is divided by y.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 500). The description of the test cases follows.

The first line of each test case contains an integer n (2 ≤ n ≤ 100) — the size of the sequence.

The second line of each test case contains n integers b1,b2,…,bn (1 ≤ bi ≤ 10^9) — the sequence b.

Output
For each test case, if it is possible to permute the elements of sequence b so that there exists a suitable pair of positive integers x≥y, output x,y on a separate line. Otherwise, output −1 on a separate line.

If there are several suitable pairs x,y, you may output any of them.

Input:
6
2
1 1
2
1 2
4
1 2 3 4
3
6 4 2
4
3 8 13 5
3
1 1 1

Output:
1 1
2 1
-1
6 4
13 8
-1
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    sorted_arr = sorted(arr, reverse=True)
    ok = True
    if(n == 2):
        print(sorted_arr[0], sorted_arr[1])
    else:        
        for i in range(n - 2):
            first = sorted_arr[i]
            second = sorted_arr[i + 1]
            third = sorted_arr[i + 2]
            if(first % second != third):
                ok = False
                break
        if(not ok):
            print(-1)
        else:
            print(sorted_arr[0], sorted_arr[1])