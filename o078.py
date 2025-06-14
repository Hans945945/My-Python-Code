'''
from itertools import product
k = input()
l = int(input())
s = input()

for t in product(k, repeat = l):
    now = ''.join(t)
    if now not in s:
        print(now)
        break
'''
import sys
sys.setrecursionlimit(1000000)
k = input().strip()
L = int(input().strip())
S = input().strip()

no = set(S[i:i+L] for i in range(len(S) - L + 1))

found =0
ans = []

def dfs(d):
    global found
    if found:
        return
    if d == L:
        word = ''.join(ans)
        if word not in no:
            print(word)
            found = 1
        return
    for c in k:
        ans.append(c)
        dfs(d + 1)
        ans.pop()

dfs(0)

