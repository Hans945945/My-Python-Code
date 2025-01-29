import sys
data = sys.stdin.read().splitlines()
n = int(data[0])
t = set()
for i in range(1, n+1):
    temp = list(sorted(map(int, data[i].split())))
    t.add((temp[0] / temp[1], temp[1] / temp[2], temp[2] / temp[0]) )
print(len(t))
