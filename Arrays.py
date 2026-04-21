"""

----------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1584/C ------------------------------------------

You are given two arrays of integers a1,a2,…,an and b1,b2,…,bn.

Let's define a transformation of the array a:

Choose any non-negative integer k such that 0≤k≤n.
Choose k distinct array indices 1 ≤ i1 < i2 < … < ik ≤ n.
Add 1 to each of ai1,ai2,…,aik, all other elements of array a remain unchanged.
Permute the elements of array a in any order.
Is it possible to perform some transformation of the array a exactly once, so that the resulting array is equal to b?

Input
The first line contains a single integer t (1 ≤ t ≤ 100) — the number of test cases. Descriptions of test cases follow.

The first line of each test case contains a single integer n (1 ≤ n ≤ 100) — the size of arrays a and b.

The second line of each test case contains n integers a1,a2,…,an (−100 ≤ ai ≤ 100).

The third line of each test case contains n integers b1,b2,…,bn (−100 ≤ bi ≤ 100).

Output
For each test case, print "YES" (without quotes) if it is possible to perform a transformation of the array a, 
so that the resulting array is equal to b. Print "NO" (without quotes) otherwise.

You can print each letter in any case (upper or lower).

Input:
3
3
-1 1 0
0 0 2
1
0
2
5
1 2 3 4 5
1 2 3 4 5

Output:
YES
NO
YES
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    brr = sorted(list(map(int, input().split())))  
    ok = True
    for i in range(n):
        diff = brr[i] - arr[i]
        if(diff > 1 or diff < 0):
            ok = False
            break
    print("YES" if ok else "NO")