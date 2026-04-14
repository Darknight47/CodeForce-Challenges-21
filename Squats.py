"""

----------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/424/A  -----------------------------------------------

Pasha has many hamsters and he makes them work out. Today, n hamsters (n is even) came to work out. The hamsters lined up and each hamster either sat down or stood up.

For another exercise, Pasha needs exactly  hamsters to stand up and the other hamsters to sit down. 
In one minute, Pasha can make some hamster ether sit down or stand up. How many minutes will he need to get what he wants if he acts optimally well?

Input
The first line contains integer n (2 ≤ n ≤ 200; n is even). The next line contains n characters without spaces. 
These characters describe the hamsters' position: the i-th character equals 'X', if the i-th hamster in the row is standing, and 'x', if he is sitting.

Output
In the first line, print a single integer — the minimum required number of minutes. 
In the second line, print a string that describes the hamsters' position after Pasha makes the required changes. If there are multiple optimal positions, print any of them.

Input:
4
xxXx

Output:
1
XxXx
"""
n = int(input())
s = input()
sit = s.count('x')
stand = n - sit
half = n // 2
if(sit == half):
    print(0)
    print(s)
else:
    if(sit > half):
        excess = sit - half
        result = list(s)
        for i in range(n):
            if excess == 0:
                break
            if result[i] == 'x':
                result[i] = 'X'
                excess -= 1
        print(sit - half)
        print(''.join(result))
    else:
        excess = stand - half
        result = list(s)
        for i in range(n):
            if excess == 0:
                break
            if result[i] == 'X':
                result[i] = 'x'
                excess -= 1
        print(half - sit)
        print(''.join(result))