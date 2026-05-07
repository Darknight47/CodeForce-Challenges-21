"""

------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1471/A ------------------------------------------

You are given an array a of length n, and an integer x. 
You can perform the following operation as many times as you would like (possibly zero): replace two adjacent elements of the array by their sum. 
For example, if the initial array was [3,6,9], in a single operation one can replace the last two elements by their sum, yielding an array [3,15], 
or replace the first two elements to get an array [9,9]. Note that the size of the array decreases after each operation.

The beauty of an array b=[b1,…,bk] is defined as ∑ki=1⌈bix⌉, which means that we divide each element by x, round it up to the nearest integer, 
and sum up the resulting values. For example, if x=3, and the array is [4,11,6], the beauty of the array is equal to ⌈43⌉+⌈113⌉+⌈63⌉=2+4+2=8.

Please determine the minimum and the maximum beauty you can get by performing some operations on the original array.

Input
The first input line contains a single integer t — the number of test cases (1 ≤ t ≤ 1000).

The first line of each test case contains two integers n and x (1 ≤ n ≤ 10^5, 1 ≤ x ≤ 10^9).

The next line contains n integers a1,a2,…,an (1 ≤ ai ≤ 10^9), the elements of the array a.

It is guaranteed that the sum of values of n over all test cases does not exceed 10^5.

Output
For each test case output two integers — the minimal and the maximal possible beauty.

Input:
2
3 3
3 6 9
3 3
6 4 11

Output:
6 6
7 8
"""
import math
cases = int(input())
for _ in range(cases):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    maxi = math.ceil(sum(arr) / x)
    mini = sum(math.ceil(a / x) for a in arr)
    print(mini, maxi)