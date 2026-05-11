"""

--------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1876/A ---------------------------------------

Pak Chanek is the chief of a village named Khuntien. On one night filled with lights, 
Pak Chanek has a sudden and important announcement that needs to be notified to all of the n residents in Khuntien.

First, Pak Chanek shares the announcement directly to one or more residents with a cost of p for each person. 
After that, the residents can share the announcement to other residents using a magical helmet-shaped device. 
However, there is a cost for using the helmet-shaped device. For each i, if the i-th resident has got the announcement at least once (either directly from Pak Chanek or from another resident), 
he/she can share the announcement to at most ai other residents with a cost of bi for each share.

If Pak Chanek can also control how the residents share the announcement to other residents, what is the minimum cost for Pak Chanek to notify all n residents of Khuntien about the announcement?


Input
Each test contains multiple test cases. The first line contains an integer t (1 ≤ t ≤ 10^4) — the number of test cases. The following lines contain the description of each test case.

The first line contains two integers n and p (1 ≤ n ≤ 10^5; 1 ≤ p ≤ 10^5) — the number of residents and the cost for Pak Chanek to share the announcement directly to one resident.

The second line contains n integers a1,a2,a3,…,an (1 ≤ ai ≤ 10^5) — the maximum number of residents that each resident can share the announcement to.

The third line contains n integers b1,b2,b3,…,bn (1 ≤ bi ≤ 10^5) — the cost for each resident to share the announcement to one other resident.

It is guaranteed that the sum of n over all test cases does not exceed 10^5.

Output
For each test case, output a line containing an integer representing the minimum cost to notify all n residents of Khuntien about the announcement.

Input:
3
6 3
2 3 2 1 1 3
4 3 2 6 3 6
1 100000
100000
1
4 94
1 4 2 3
103 96 86 57

Output:
16
100000
265
"""
cases = int(input())
for _ in range(cases):
    n, p = map(int, input().split())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    paired = list(zip(brr, arr))
    paired.sort()
    ans = p
    n -= 1
    for cost, quantity in paired:
        if(cost >= p or n <= 0):
            break
        temp_ans = min(quantity, n) * cost
        ans += temp_ans
        n -= min(quantity, n)
    if(n > 0):
        ans += n * p
    print(ans)