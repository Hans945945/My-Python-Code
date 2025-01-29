import sys
N, m = input().split()
n = len(N)
for s in sys.stdin:
    A = 0
    B = 0
    for i in range(n):
        if N[i] == s[i]:
            A+=1
        elif N[i] in s:
            B+=1
    print(f"{A}A{B}B")
