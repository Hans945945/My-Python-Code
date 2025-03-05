import sys
data = sys.stdin.readlines()
r = []
for i in range(0,len(data),2):
    a = list(data[i])
    b = list(data[i+1])
    x = []
    for w in a:
        if w in b:
            b.pop(b.index(w))
            x.append(w)
    r.append("".join(sorted(x)))
sys.stdout.write("\n".join(r)+"\n")
    
