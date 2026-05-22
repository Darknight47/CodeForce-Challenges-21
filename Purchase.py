"""

---------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2230/A ----------------------------------------

You have a group of n students who need access to an online course. Two types of access keys are available in the store:

Individual key: costs a dollars and gives access to one student.
Group key: costs b dollars and gives access to a group of up to three students inclusive.
A group key can also be used for fewer students (one or two), and its price does not change.

Your task is to determine the minimum amount of money needed to provide access to the online course for all n students.

Input
The first line contains one integer t (1 ≤ t ≤ 10^4) — the number of test cases.

Each test case consists of one line containing three integers n,a,b (1 ≤ n, a, b ≤ 10^8) — the number of students, the cost of an individual key, and the cost of a group key.

Output
For each test case, output one integer — the minimum amount of money needed to provide access to the online course for all n students.

Input:
9
5 10 25
4 10 50
1 20 15
1 10 25
100000000 100 290
2 10 15
300 1 1
4 10 12
11 10 20

Output:
45
40
15
10
9666666670
15
100
22
80
"""
cases = int(input())
for _ in range(cases):
    n, a, b = map(int, input().split())
    # if all students buy an individual key, the cost is n*a
    all_individual_cost = n * a
    # if all students buy individually a group-key, the cost is n * b
    all_individual_group_cost = n * b
    # we can have group of 3 
    if(n > 3):
        group_of_3_cost = (n // 3) * b + min((n % 3) * a, b)
    else:
        group_of_3_cost = min((n * a), b)
    min_cost = min(all_individual_cost, all_individual_group_cost, group_of_3_cost)
    print(min_cost)