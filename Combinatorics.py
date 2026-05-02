"""

---------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1771/A -------------------------------------

Hossam woke up bored, so he decided to create an interesting array with his friend Hazem.

Now, they have an array a of n positive integers, Hossam will choose a number ai and Hazem will choose a number aj.

Count the number of interesting pairs (ai,aj) that meet all the following conditions:

1 ≤ i , j ≤ n;
i≠j;
The absolute difference |ai−aj| must be equal to the maximum absolute difference over all the pairs in the array. More formally, |ai−aj|=max1≤p,q≤n|ap−aq|.

Input
The input consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 100), which denotes the number of test cases. Description of the test cases follows.

The first line of each test case contains an integer n (2 ≤ n ≤ 10^5).

The second line of each test case contains n integers a1,a2,…,an (1 ≤ ai ≤ 10^5).

It is guaranteed that the sum of n over all test cases does not exceed 10^5.

Output
For each test case print an integer — the number of interesting pairs (ai,aj).

Input:
2
5
6 2 3 8 1
6
7 2 8 3 2 10

Output:
2
4
"""
from collections import Counter
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    counter = Counter(arr)
    
    mn = min(arr)
    mx = max(arr)
    if(mn == mx):
        print(n * (n - 1))
    else:
        print(counter[mn] * counter[mx] * 2 )