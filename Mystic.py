"""

------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1689/B ------------------------------------

Monocarp is a little boy who lives in Byteland and he loves programming.

Recently, he found a permutation of length n. 
He has to come up with a mystic permutation. It has to be a new permutation such that it differs from the old one in each position.

More formally, if the old permutation is p1,p2,…,pn and the new one is q1,q2,…,qn it must hold that
p1≠q1,p2≠q2,…,pn≠qn.

Monocarp is afraid of lexicographically large permutations. Can you please help him to find the lexicographically minimal mystic permutation?

Input
There are several test cases in the input data. The first line contains a single integer t (1 ≤ t ≤ 200) — the number of test cases. This is followed by the test cases description.

The first line of each test case contains a positive integer n (1 ≤ n ≤ 1000) — the length of the permutation.

The second line of each test case contains n distinct positive integers p1,p2,…,pn (1 ≤ pi ≤ n). It's guaranteed that p is a permutation, i. e. pi≠pj for all i≠j.

It is guaranteed that the sum of n does not exceed 1000 over all test cases.

Output
For each test case, output n positive integers — the lexicographically minimal mystic permutations. If such a permutation does not exist, output −1 instead.

Input:
4
3
1 2 3
5
2 3 4 5 1
4
2 3 1 4
1
1

Output.
2 3 1
1 2 3 4 5
1 2 4 3
-1
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = list(range(1, n + 1))
    if(n == 1):
        print(-1)
        continue
    for i in range(n - 1):
        # If current element in arr and ans are equals, we swap the elements in ans for getting lexicographically smallest array
        if arr[i] == ans[i]:
            ans[i], ans[i + 1] = ans[i + 1], ans[i]
    if(ans[-1] == arr[-1]):
        ans[-1], ans[-2] = ans[-2], ans[-1]
    print(*ans)