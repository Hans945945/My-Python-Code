import sys
x,y,l,r = map(int, sys.stdin.readline().split())
r*=r
n = int(sys.stdin.readline())
count = 0
for s in sys.stdin:
    Sx, Sy, Sl = map(int, s.split())
    if Sl <= l and (abs(x-Sx)**2 + abs(y-Sy)**2) <= r:
        count+=1
print(count)
