import sys
n = int(sys.stdin.readline())
factories = []
data = sys.stdin.read().splitlines()
for s in data[:-1]:
    a, p = map(int, s.split())
    factories.append((a, p))

num = int(data[-1])
factories.sort(reverse=True)
accumulated = 0
r = n
if num != 0: 
    for i in range(n):
        accumulated += factories[i][1]
        if accumulated >= num: 
            r= i + 1
            break
else:
    r = 0
print(r)

