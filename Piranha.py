"""

----------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1433/C ------------------------------------------------

There are n piranhas with sizes a1,a2,…,an in the aquarium. Piranhas are numbered from left to right in order they live in the aquarium.

Scientists of the Berland State University want to find if there is dominant piranha in the aquarium. 
The piranha is called dominant if it can eat all the other piranhas in the aquarium (except itself, of course). Other piranhas will do nothing while the dominant piranha will eat them.

Because the aquarium is pretty narrow and long, the piranha can eat only one of the adjacent piranhas during one move. Piranha can do as many moves as it needs (or as it can). More precisely:

The piranha i can eat the piranha i−1 if the piranha i−1 exists and ai−1<ai.
The piranha i can eat the piranha i+1 if the piranha i+1 exists and ai+1<ai.
When the piranha i eats some piranha, its size increases by one (ai becomes ai+1).

Your task is to find any dominant piranha in the aquarium or determine if there are no such piranhas.

Note that you have to find any (exactly one) dominant piranha, you don't have to find all of them.

For example, if a=[5,3,4,4,5], then the third piranha can be dominant. Consider the sequence of its moves:

The piranha eats the second piranha and a becomes [5,5–,4,5] (the underlined piranha is our candidate).
The piranha eats the third piranha and a becomes [5,6–,5].
The piranha eats the first piranha and a becomes [7–,5].
The piranha eats the second piranha and a becomes [8–].
You have to answer t independent test cases.

Input
The first line of the input contains one integer t (1 ≤ t ≤ 2⋅10^4) — the number of test cases. Then t test cases follow.

The first line of the test case contains one integer n (2 ≤ n ≤ 3⋅10^5) — the number of piranhas in the aquarium. 
The second line of the test case contains n integers a1,a2,…,an (1 ≤ ai ≤ 10^9), where ai is the size of the i-th piranha.

It is guaranteed that the sum of n does not exceed 3⋅10^5 (∑n ≤ 3⋅10^5).

Output
For each test case, print the answer: -1 if there are no dominant piranhas in the aquarium or index of any dominant piranha otherwise. If there are several answers, you can print any.

Input:
6
5
5 3 4 4 5
3
1 1 1
5
4 4 3 4 4
5
5 5 4 3 2
3
1 1 2
5
5 4 3 5 5

Output:
3
-1
4
3
3
1
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    # storing the numbers with their indexes in a list of tuples
    indexed_arr = [(arr[i], i) for i in range(n)]
    # if there are multiple maximum number (largest number), finding the one that has at least one smaller number on either side
    max_num = max(arr)
    max_num_indices = [i for i, num in enumerate(arr) if num == max_num]
    found = False
    for index in max_num_indices:
        if (index > 0 and arr[index - 1] < max_num) or (index < n - 1 and arr[index + 1] < max_num):
            print(index + 1)  # printing the index of the largest number that has at least one smaller number on either side
            found = True
            break
    if not found:
        print(-1)  