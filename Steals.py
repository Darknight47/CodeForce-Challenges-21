"""

---------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2228/A ----------------------------------------

Marisa is a girl of integrity who always helps others safeguard their belongings. 
ver a period of n days, she comes each day to take one of Reimu's takeouts. The i-th takeout is described by its deliciousness value — an integer wi (0 ≤ wi ≤ 2), forming a sequence w of length n.

Marisa has a special fondness for the number 3. She can perform the following operation zero or more times:

Select a non-empty subsequence∗ of w whose sum is divisible by 3, and remove the elements of the subsequence from w.
Determine the maximum number of operations Marisa can perform.

∗ A sequence a is a subsequence of a sequence b if a can be obtained from b by the deletion of several (possibly, zero or all) element from arbitrary positions.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 500). The description of the test cases follows.

The first line of each test case contains a single integer n (1 ≤ n ≤ 100).

The second line contains n integers w1,w2,…,wn (0 ≤ wi ≤ 2), denoting the deliciousness values of the takeouts.

Output
For each test case, output the maximum number of operations Marisa can perform.

Input:
3
4
0 0 0 0
3
1 2 0
5
1 2 1 2 1

Output:
4
2
2
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    zeros = 0
    ones = 0
    twos = 0
    for i in arr:
        if i == 0:
            zeros += 1
        elif i == 1:
            ones += 1
        else:
            twos += 1
    pairs = min(ones, twos)
    ones -= pairs
    twos -= pairs

    triples_1 = ones // 3
    tiples_2 = twos // 3

    ans = zeros + pairs + triples_1 + tiples_2
    print(ans)