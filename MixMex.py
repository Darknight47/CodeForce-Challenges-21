"""

-------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1738/A ---------------------------------------

The hero is addicted to glory, and is fighting against a monster.

The hero has n skills. The i-th skill is of type ai (either fire or frost) and has initial damage bi.

The hero can perform all of the n skills in any order (with each skill performed exactly once). When performing each skill, the hero can play a magic as follows:

If the current skill immediately follows another skill of a different type, then its damage is doubled.
In other words,
If a skill of type fire and with initial damage c is performed immediately after a skill of type fire, then it will deal c damage;
If a skill of type fire and with initial damage c is performed immediately after a skill of type frost, then it will deal 2c damage;
If a skill of type frost and with initial damage c is performed immediately after a skill of type fire, then it will deal 2c damage;
If a skill of type frost and with initial damage c is performed immediately after a skill of type frost , then it will deal c damage.
Your task is to find the maximum damage the hero can deal.

Input
Each test contains multiple test cases. The first line contains an integer t (1 ≤ t ≤ 10^5) — the number of test cases. The following lines contain the description of each test case.

The first line of each test case contains an integer n (1 ≤ n ≤ 10^5), indicating the number of skills.

The second line of each test case contains n integers a1,a2,…,an (0 ≤ ai ≤ 1), where ai indicates the type of the i-th skill. Specifically, the i-th skill is of type fire if ai=0, and of type frost if ai=1.

The third line of each test case contains n integers b1,b2,…,bn (1 ≤ bi ≤ 10^9), where bi indicates the initial damage of the i-th skill.

It is guaranteed that the sum of n over all test cases does not exceed 10^5.

Output
For each test case, output the maximum damage the hero can deal.

Input:
4
4
0 1 1 1
1 10 100 1000
6
0 0 0 1 1 1
3 4 5 6 7 8
3
1 1 1
1000000000 1000000000 1000000000
1
1
1

Output:
2112
63
3000000000
1
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    types = list(map(int, input().split()))
    damages = list(map(int, input().split()))

    fires = []
    frosts = []

    for t, d in zip(types, damages):
        if t == 0:
            fires.append(d)
        else:
            frosts.append(d)

    fires.sort(reverse=True)
    frosts.sort(reverse=True)

    k = min(len(fires), len(frosts))
    if len(fires) == len(frosts):
        total = sum(fires) + sum(frosts)
        smallest = min(fires + frosts)
        print(2 * total - smallest)
        continue
    ans = 0

    ans += 2 * sum(fires[:k])
    ans += 2 * sum(frosts[:k])

    if len(fires) > k:
        ans += sum(fires[k:])
    if len(frosts) > k:
        ans += sum(frosts[k:])

    print(ans)