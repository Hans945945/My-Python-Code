import sys
n,m = map(int, sys.stdin.readline().split())
buildings = list(map(int, sys.stdin.readline().split()))
m-=1
tallest = buildings[m]
count = 0
if m != 0:
    for i in range(m-1,-1,-1):
         if buildings[i]>tallest:
             tallest = buildings[i]
             count += 1
tallest = buildings[m]
if m != n-1:
    for i in range(m+1,n):
        if buildings[i]>tallest:
             tallest = buildings[i]
             count += 1
print(count)
