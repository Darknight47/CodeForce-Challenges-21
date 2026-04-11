"""

---------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1525/B ------------------------------------------------

You are given a permutation a consisting of n numbers 1, 2, ..., n (a permutation is an array in which each element from 1 to n occurs exactly once).

You can perform the following operation: choose some subarray (contiguous subsegment) of a and rearrange the elements in it in any way you want. But this operation cannot be applied to the whole array.

For example, if a=[2,1,4,5,3] and we want to apply the operation to the subarray a[2,4] (the subarray containing all elements from the 2-nd to the 4-th), 
then after the operation, the array can become a=[2,5,1,4,3] or, for example, a=[2,1,5,4,3].

Your task is to calculate the minimum number of operations described above to sort the permutation a in ascending order.

Input
The first line contains a single integer t (1 ≤ t ≤ 2000) — the number of test cases.

The first line of the test case contains a single integer n (3 ≤ n ≤ 50) — the number of elements in the permutation.

The second line of the test case contains n distinct integers from 1 to n — the given permutation a.

Output
For each test case, output a single integer — the minimum number of operations described above to sort the array a in ascending order.

Input:
3
4
1 3 2 4
3
1 2 3
5
2 1 4 5 3

Output:
1
0
2
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    cpy_arr = arr.copy()
    cpy_arr.sort()
    if(cpy_arr == arr):
        print(0)
    else:
        if(cpy_arr[0] == arr[-1] and cpy_arr[-1] == arr[0]):
            print(3)
        elif(cpy_arr[0] == arr[0] or cpy_arr[-1] == arr[-1]):
            print(1)
        else:
            print(2)