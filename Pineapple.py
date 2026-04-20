"""

------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/697/A  ------------------------------------------

Ted has a pineapple. This pineapple is able to bark like a bulldog! At time t (in seconds) it barks for the first time. Then every s seconds after it, it barks twice with 1 second interval. 
Thus it barks at times t, t + s, t + s + 1, t + 2s, t + 2s + 1, etc.

Barney woke up in the morning and wants to eat the pineapple, but he can't eat it when it's barking. 
Barney plans to eat it at time x (in seconds), so he asked you to tell him if it's gonna bark at that time.

Input
The first and only line of input contains three integers t, s and x (0 ≤ t, x ≤ 109, 2 ≤ s ≤ 109) — the time the pineapple barks for the first time, 
the pineapple barking interval, and the time Barney wants to eat the pineapple respectively.

Output
Print a single "YES" (without quotes) if the pineapple will bark at time x or a single "NO" (without quotes) otherwise in the only line of output.

Input:
3 10 4

Output:
NO
"""
t, s, x = map(int, input().split())
if(x < t):
    print("NO")
elif(x < s and x != t):
    print("NO")
elif(x < (t + s) and x != t):
    print("NO")
else:
    if( ((x - t) % s == 0) or ((x - t - 1) % s == 0)):
        print("YES")
    elif(x == t):
        print("YES")
    else:
        print("NO")