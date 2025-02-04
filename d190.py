import sys
data = sys.stdin.read().splitlines()[:-1]
for i in range(1, len(data), 2):
    sys.stdout.write(" ".join(map(str, sorted(map(int, data[i].split()))))+"\n")
