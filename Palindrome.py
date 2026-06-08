"""

------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/2234/B   ---------------------------------------------

You are given a positive integer n. A pair of non-negative integers a,b is called beautiful if the following conditions hold:

a+b=n.
The number a is a palindrome.∗
The number b is divisible by 12.
You need to find a beautiful pair or report that it does not exist.

∗ A number is called a palindrome if and only if it remains the same when its digits (in decimal notation) are written in reverse order. 
For example, the numbers 12321, 6776, 5, 0 are palindromes, while the numbers 123 and 69 — are not.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^4). The description of the test cases follows.

The only line of each test case contains a single integer n (1 ≤ n ≤ 10^18).

Output
For each test case, if such a and b exist, output a and b on a separate line, separated by a space. Otherwise, output −1 on a separate line.

If there are several beautiful pairs a,b, you may output any of them.

Input:
6
1
10
310
12
1000000000
6111111111111111

Output:
1 0
-1
262 48
0 12
889989988 110010012
111111111111111 6000000000000000
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    if(n < 10):
        print(n, 0)
    elif(n == 10):
        print(-1)
    else:
        r = n % 12
        if(r == 10):
            print(22, n - 22)
        else:
            b = n - r
            print(r, b)