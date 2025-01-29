import sys
data = sys.stdin.read
N = int(input().strip())
hs = list(map(int,input().split()))
ws = list(map(int,input().split()))
min_v = float("inf")
smallest = -1
for i in range(N):
    lion = ws[i]*hs[i]
    if lion < min_v:
        min_v = lion
        smallest = i
print(hs[smallest], ws[smallest])
    
