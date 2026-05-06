"""

--------------------------------------------- Link for the challenge: https://codeforces.com/contest/1795/problem/A ---------------------------------------------

There are two towers consisting of blocks of two colors: red and blue. Both towers are represented by strings of characters B and/or R denoting the order of blocks in 
them from the bottom to the top, where B corresponds to a blue block, and R corresponds to a red block.
You can perform the following operation any number of times: choose a tower with at least two blocks, and move its top block to the top of the other tower.
The pair of towers is beautiful if no pair of touching blocks has the same color; i. e. no red block stands on top of another red block, and no blue block stands on top of another blue block.

You have to check if it is possible to perform any number of operations (possibly zero) to make the pair of towers beautiful.

Input
The first line contains one integer t (1 ≤ t ≤ 1000) — the number of test cases.

Each test case consists of three lines:

the first line contains two integers n and m (1 ≤ n, m ≤ 20) — the number of blocks in the first tower and the number of blocks in the second tower, respectively;
the second line contains s — a string of exactly n characters B and/or R, denoting the first tower;
the third line contains t — a string of exactly m characters B and/or R, denoting the second tower.
Output
For each test case, print YES if it is possible to perform several (possibly zero) operations in such a way that the pair of towers becomes beautiful; otherwise print NO.

You may print each letter in any case (YES, yes, Yes will all be recognized as positive answer, NO, no and nO will all be recognized as negative answer).

Input:
4
4 3
BRBB
RBR
4 7
BRBR
RRBRBRB
3 4
RBR
BRBR
5 4
BRBRR
BRBR

Output:
YES
YES
YES
NO
"""
def alternating(s):
    if len(s) <= 1:
        return True
    return all(s[i] != s[i+1] for i in range(len(s)-1))

cases = int(input())
for _ in range(cases):
    a, b = map(int, input().split())
    A = input().strip()
    B = input().strip()
    ok = False
    # Case 1: move from A → B
    for k in range(len(A) + 1):
        removed = A[len(A) - k:][::-1]   
        A2 = A[:len(A) - k]
        B2 = B + removed
        if alternating(A2) and alternating(B2):
            ok = True
            break

    # Case 2: move from B → A
    if not ok:
        for k in range(len(B) + 1):
            removed = B[len(B) - k:][::-1]
            B2 = B[:len(B) - k]
            A2 = A + removed
            if alternating(A2) and alternating(B2):
                ok = True
                break

    print("YES" if ok else "NO")