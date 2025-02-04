import sys
data = sys.stdin.read().splitlines()
table = {}
index = 0
for s in data[1:]:
    words = s.strip()
    if words == "[1337]":
        index = data.index(s)
        break
    key, value = words.split(":")
    table[key] = value
r = []
for line in data[index+1:-1]:
    line = line.strip()
    r.append(" ".join([table.get(w, w) for w in line.split()]))
sys.stdout.write("\n".join(r)+"\n")
