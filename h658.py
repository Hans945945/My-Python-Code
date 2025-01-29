import sys
x,y = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
min_d = min_x = min_y = float("inf")
for s in sys.stdin:
    a,b = map(int, s.split())
    d = abs(x-a)**2 + abs(y-b)**2
    if d < min_d:
        min_x = a
        min_y = b
        min_d = d
print(min_x, min_y)
