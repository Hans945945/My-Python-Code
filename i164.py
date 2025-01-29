import sys
from bisect import bisect_left

n = int(input())
teacher = sys.stdin.readline().split()
kid = sys.stdin.readline().split()

index = {}
for i, value in enumerate(kid):
    if value not in index:
        index[value] = []
    index[value].append(i)

r = []
for i, value in enumerate(teacher):
    if value in index:
        positions = index[value]
        pos = bisect_left(positions, i)
        if pos == 0:
            closest = positions[0]
        elif pos == len(positions):
            closest = positions[-1]
        else:
            closest = positions[pos] if abs(positions[pos] - i) < abs(positions[pos - 1] - i) else positions[pos - 1]
        r.append(abs(closest - i))
    else:
        r.append(-1)

sys.stdout.write(" ".join(map(str, r)) + "\n")

