import sys
ans = input()
q = int(input())
for s in sys.stdin:
    A = 0
    B = 0
    for i in range(4):
        if ans[i] == s[i]:
            A+=1
        elif ans[i] in s:
            B+=1
    print(f"{A}A{B}B")
