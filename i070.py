import sys
n = int(input())
teacher = sys.stdin.readline().split()
kid = sys.stdin.readline().split()
index = {}
for i in range(n):
    if index.get(kid[i],0):
        index[kid[i]].append(i)
    else:
        index[kid[i]] = [i]
r = []
for i in range(n):
    temp = index.get(teacher[i],0)
    if temp:
        r.append(min(abs(i-idx) for idx in temp))
    else:
        r.append("-1")
sys.stdout.write(" ".join(map(str, r)))
    
