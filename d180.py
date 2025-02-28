import sys
data = sys.stdin.read().split()
n = int(data.pop(0))
l = 0
r = 0
for i in range(n):
    if i %2 == 0:
        l += int(data[i])
    else:
        r += int(data[i])
print("left" if l > r else "right")
