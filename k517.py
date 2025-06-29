p = int(input())
MAP = {"W":1, "S":2, "E":3, "N":4}
r = []
for _ in range(p):
    c,d,v= input().split()
    r.append((int(d)/int(v), c))
r.sort(key = lambda x: (x[0], MAP[x[1]]))
print("".join(c for _,c in r))
