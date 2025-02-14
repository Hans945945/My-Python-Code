import sys
min_l = float("inf")
max_l = float("-inf")
data = sys.stdin.readlines()[1:]
lastX,lastY = map(int, data.pop(0).split())
for s in data:
    x,y = map(int, s.split())
    now = abs(x-lastX) + abs(y-lastY)
    max_l = max(max_l,now)
    min_l = min(min_l,now)
    lastX,lastY = x,y
print(max_l,min_l)
