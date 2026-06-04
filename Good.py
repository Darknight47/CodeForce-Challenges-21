"""

------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1856/B ------------------------------------------

You are given an array of positive integers a of length n.

Let's call an array of positive integers b of length n good if:

ai≠bi for all i from 1 to n,
a1+a2+…+an=b1+b2+…+bn.
Does a good array exist?

Input
Each test contains multiple test cases. The first line of input contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases. The description of the test cases follows.

The first line of each test case contains a single integer n (1 ≤ n ≤ 10^5) — the length of the array a.

The second line of each test case contains n integers a1,a2,…,an (1 ≤ ai ≤ 10^9) — the elements of the array a.

It is guaranteed that the sum of n over all test cases does not exceed 10^5.

Output
For each test case, output "YES" (without quotes) if there exists a good array, and "NO" (without quotes) otherwise.

You can output the answer in any case (upper or lower). For example, the strings "yEs","yes", "Yes", and "YES" will be recognized as positive responses.

Input:
6
3
6 1 2
2
1 1
4
3 1 2 4
1
17
5
1 2 1 1 1
3
618343152 819343431 1000000000

Output:
YES
NO
YES
NO
NO
YES
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    if(n == 1):
        print("NO")
    else:
        total_sum = 0
        ones = 0
        for num in arr:
            total_sum += num
            if num == 1:
                ones += 1
        if(total_sum >= n + ones):
            print("YES")
        else:
            print("NO")