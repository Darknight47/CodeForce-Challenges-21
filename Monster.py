"""

------------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/2227/B ------------------------------------------------

Yousef has given you a sequence s of length n consisting only of characters '(' and ')'. You are allowed to perform the following operation at most once:

Choose a substring∗ of s and remove it. Then, you may reinsert the removed characters back into the remaining string one by one. 
Each character can be placed at any arbitrary position, independently of the others.
Yousef wants you to determine whether it is possible to obtain a regular bracket sequence† after performing the operation at most once.

∗ A substring is a contiguous subsegment of a string. For example, "acab" is a substring of "abacaba" (it starts in position 3 and ends in position 6), 
but "aa" or "d" aren't substrings of this string. So the substring of the string s from position l to position r is s[l,r]=slsl+1…sr.

† A regular bracket sequence is a bracket sequence that can be transformed into a correct arithmetic expression by inserting the characters 1 
and + between the original characters of the sequence. For example:

bracket sequences ()() and (()) are regular (the resulting expressions are: (1)+(1) and ((1+1)+1));
bracket sequences )(, ( and ) are not.
Input
The first line contains an integer t (1 ≤ t ≤ 10^4) — the number of test cases. The descriptions of the test cases follow.

The first line of each test case contains a single integer n (1 ≤ n ≤ 2⋅10^5) — the length of the string s.

The second line of each test case contains a sequence s of length n consisting only of characters '(' and ')'.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, output "YES" if the sequence can be made regular, and "NO" otherwise.

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.

Input:
6
2
()
2
)(
3
(((
6
())(()
4
(()(
5
)()()

Output:
YES
YES
NO
YES
NO
NO
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    s = input()
    left = s.count('(')
    right = n - left
    if left == right:
        print("YES")
    else:
        print("NO")