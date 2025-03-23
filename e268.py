import sys
data = sys.stdin.readlines()
L,N = map(int, data.pop(0).split())
idx = 0
table = {}
for _ in range(L):
    k,v = data[idx].split()
    table[k] = v
    idx += 1
r = []
for _ in range(N):
    w = data[idx].rstrip()
    weird = table.get(w,0)
    if weird != 0:
        r.append(weird)
    elif w[-1] == "y" and w[-2] not in "aeiou":
        r.append(f"{w[:-1]}ies")
    elif w[-1] in "osx" or w[-2:] in ["ch","sh"]:
        r.append(f"{w}es")
    else:
        r.append(f"{w}s")
    idx += 1
sys.stdout.write("\n".join(r)+"\n")
