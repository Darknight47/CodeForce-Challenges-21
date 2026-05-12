"""

--------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/102/B ---------------------------------------------

Having watched the last Harry Potter film, little Gerald also decided to practice magic. He found in his father's magical book a spell that turns any number in the sum of its digits. 
At the moment Gerald learned that, he came across a number n. How many times can Gerald put a spell on it until the number becomes one-digit?

Input
The first line contains the only integer n (0 ≤ n ≤ 10^100000). It is guaranteed that n doesn't contain any leading zeroes.

Output
Print the number of times a number can be replaced by the sum of its digits until it only contains one digit.

Input:
0

Output:
0
"""
n = input()
count = 0

while len(n) > 1:
    digit_sum = sum(int(d) for d in n)
    n = str(digit_sum)
    count += 1

print(count)