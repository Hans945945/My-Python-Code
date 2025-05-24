from math import hypot

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

d12 = hypot(x2 - x1, y2 - y1)
d23 = hypot(x3 - x2, y3 - y2)
d31 = hypot(x1 - x3, y1 - y3)

if d12 > d23 and d12 > d31:
    x4, y4 = x1 + x2 - x3, y1 + y2 - y3
elif d23 > d31:
    x4, y4 = x2 + x3 - x1, y2 + y3 - y1
else:
    x4, y4 = x1 + x3 - x2, y1 + y3 - y2

print(x4, y4)
