import sys
n = int(sys.stdin.readline())
elevator = list(map(int, sys.stdin.readline().split()))
elevator.insert(0, 1)
total = 0
for i in range(1, len(elevator)):
    last = elevator[i-1]
    now = elevator[i]
    if last < now:
        total += (now - last)*3
    else:
        total += (last - now)*2
print(total)
