"""


------------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1561/A -------------------------------------------------------

You have a permutation: an array a=[a1,a2,…,an] of distinct integers from 1 to n. The length of the permutation n is odd.

Consider the following algorithm of sorting the permutation in increasing order.

A helper procedure of the algorithm, f(i), takes a single argument i (1 ≤ i ≤ n−1) and does the following. 
If ai > ai+1, the values of ai and ai+1 are exchanged. Otherwise, the permutation doesn't change.

The algorithm consists of iterations, numbered with consecutive integers starting with 1. 
On the i-th iteration, the algorithm does the following:

if i is odd, call f(1),f(3),…,f(n−2);
if i is even, call f(2),f(4),…,f(n−1).
It can be proven that after a finite number of iterations the permutation will be sorted in increasing order.

After how many iterations will this happen for the first time?

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 100). Description of the test cases follows.

The first line of each test case contains a single integer n (3 ≤ n ≤ 999; n is odd) — the length of the permutation.

The second line contains n distinct integers a1,a2,…,an (1 ≤ ai ≤ n) — the permutation itself.

It is guaranteed that the sum of n over all test cases does not exceed 999.

Output
For each test case print the number of iterations after which the permutation will become sorted in increasing order for the first time.

If the given permutation is already sorted, print 0.

Input:
3
3
3 2 1
7
4 5 7 1 3 2 6
5
1 2 3 4 5

Output:
3
5
0
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    target = list(range(1, n + 1))

    iterations = 0
    odd = True

    while arr != target:
        if odd:
            for i in range(1, n, 2):  # 1,3,5...
                i -= 1
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
        else:
            for i in range(2, n, 2):  # 2,4,6...
                i -= 1
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]

        iterations += 1
        odd = not odd

    print(iterations)