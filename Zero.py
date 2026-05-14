"""

------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/75/A -------------------------------------

Can you imagine our life if we removed all zeros from it? For sure we will have many problems.

In this problem we will have a simple example if we removed all zeros from our life, it's the addition operation. 
Let's assume you are given this equation a + b = c, where a and b are positive integers, and c is the sum of a and b. Now let's remove all zeros from this equation. 
Will the equation remain correct after removing all zeros?

For example if the equation is 101 + 102 = 203, if we removed all zeros it will be 11 + 12 = 23 which is still a correct equation.

But if the equation is 105 + 106 = 211, if we removed all zeros it will be 15 + 16 = 211 which is not a correct equation.

Input
The input will consist of two lines, the first line will contain the integer a, and the second line will contain the integer b which are in the equation as described above (1 ≤ a, b ≤ 10^9). 
There won't be any leading zeros in both. The value of c should be calculated as c = a + b.

Output
The output will be just one line, you should print "YES" if the equation will remain correct after removing all zeros, and print "NO" otherwise.

Input:
101
102

Ouput:
YES
"""
a = input()
b = input()
a_with_zero = int(a)
b_with_zero = int(b)
temp_sum = a_with_zero + b_with_zero
temp_sum_str = str(temp_sum).replace('0', '')
a_without_zero = int(a.replace('0', ''))
b_without_zero = int(b.replace('0', ''))
temp_sum_without_zero = a_without_zero + b_without_zero
print("YES" if temp_sum_str == str(temp_sum_without_zero) else "NO")