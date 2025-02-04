import sys
n = int(sys.stdin.readline())
street = sorted(map(int, sys.stdin.readline().split()),key = abs)
last = (street[0] < 0) #1白0黑
count = 0
for i in range(1,n):
    now = (street[i] < 0)
    if now != last:
        count += 1
    last = now
print(count)

