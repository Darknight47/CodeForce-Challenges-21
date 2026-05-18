"""

-------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2171/B --------------------------------------------

Yuu is trying out the student council! Unfortunately, she is being forced to do clerical work... Touko wants her to fill out the blanks in various student council documents.

You are given a partially filled array of nonnegative integers a1,a2,…,an, where blank elements are denoted with −1. 
You would like to fill in the blank elements with nonnegative integers, such that the absolute value of the sum of the elements in its difference array is minimized.

More formally, let b be the array of length n−1 such that bi=ai+1−ai for all 1≤i≤n−1. 
Find the minimum possible value of |b1+b2+⋯+bn−1|, across all possible ways to fill in the blank elements of a.

Additionally, output the array that achieves this minimum. If there are multiple such arrays, output the one that is lexicographically smallest∗.

∗ For two arbitrary arrays c and d of length n, we say that c is lexicographically smaller than d if there exists an index i (1 ≤ i ≤ n) such that cj=dj for all j<i, and ci<di. 
In other words, c and d differ in at least one index, and at the first index at which they differ, ci is smaller than di.

Input
The first line contains a single integer t (1 ≤ t ≤ 10^4)  — the number of test cases.

The first line of each test case contains a single integer n (2 ≤ n ≤ 2⋅10^5).

The second line of each test case contains n integers, a1,a2,…,an (−1 ≤ ai ≤ 10^6).

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, on the first line, output the minimum possible value of |b1+b2+⋯+bn−1|. 
Then, on the second line, output n integers, the values of a1,a2,…,an in the lexicographically smallest array achieving this minimum.

Input:
6
4
2 -1 7 1
4
-1 2 4 -1
8
2 -1 1 5 11 12 1 -1
3
-1 -1 -1
3
2 5 4
2
-1 5

Output:
1
2 0 7 1
0
0 2 4 0
0
2 0 1 5 11 12 1 2
0
0 0 0
2
2 5 4
0
5 5
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    if(arr[0] == -1 and arr[sze-1] == -1):
        arr[0] = 0
        arr[sze-1] = 0
    if(arr[0] == -1):
        arr[0] = arr[sze-1]
    if(arr[sze-1] == -1):
        arr[sze-1] = arr[0]
    temp_sum = 0
    for i in range(sze - 1):
        if(arr[i] == -1):
            arr[i] = 0
        elif(arr[i + 1] == -1):
            arr[i + 1] = 0
        temp_sum += arr[i + 1] - arr[i]
    print(abs(temp_sum))
    print(*arr)