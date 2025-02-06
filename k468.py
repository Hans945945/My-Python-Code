import sys
n, s, f = map(int, sys.stdin.readline().split())
targets = sys.stdin.readline().split()

count = {}
s -= (s % 2 == 0)

for t in targets:
    count[t] = count.get(t, 0) + 1
    if t == str(f) and count[t] == s:
        break

sys.stdout.write(str(sum((v + 1) // 2 for v in count.values())) + "\n")
