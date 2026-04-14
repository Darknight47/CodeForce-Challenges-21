"""

----------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/369/A ------------------------------------------------

Valera is a lazy student. He has m clean bowls and k clean plates.

Valera has made an eating plan for the next n days. As Valera is lazy, he will eat exactly one dish per day. 
At that, in order to eat a dish, he needs exactly one clean plate or bowl. We know that Valera can cook only two types of dishes. 
He can eat dishes of the first type from bowls and dishes of the second type from either bowls or plates.

When Valera finishes eating, he leaves a dirty plate/bowl behind. His life philosophy doesn't let him eat from dirty kitchenware. 
So sometimes he needs to wash his plate/bowl before eating. Find the minimum number of times Valera will need to wash a plate/bowl, if he acts optimally.

Input
The first line of the input contains three integers n, m, k (1 ≤ n, m, k ≤ 1000) — the number of the planned days, the number of clean bowls and the number of clean plates.

The second line contains n integers a1, a2, ..., an (1 ≤ ai ≤ 2). If ai equals one, then on day i Valera will eat a first type dish. If ai equals two, then on day i Valera will eat a second type dish.

Output
Print a single integer — the minimum number of times Valera will need to wash a plate/bowl.

Input:
3 1 1
1 2 1

Output:
1
"""
days, bowls, plates = map(int, input().split())
arr = list(map(int, input().split()))
# type_one only can be eaten from a bowl
# type_two can be eaten from a plate or a bowl
min_wash = 0
for i in range(days):
    food_type = arr[i]
    if food_type == 1:
        if bowls > 0:
            bowls -= 1
        else:
            min_wash += 1
    else:
        if plates > 0:
            plates -= 1
        elif bowls > 0:
            bowls -= 1
        else:
            min_wash += 1
print(min_wash)