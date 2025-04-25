import sys
import re
seen = []
r = []
for s in sys.stdin.readlines():
    s = s.rstrip()
    if s == "0":
        break
    
    temp = []
    words = re.findall(r"[A-Za-z]+|\d+|[^A-Za-z\d\s]+|\s+", s)

    for w in words:
        if w.isdigit():
            idx = int(w) - 1
            temp.append(seen[idx])
            seen.insert(0, seen.pop(idx))
        elif re.fullmatch(r"[A-Za-z]+", w):
            temp.append(w)
            seen.insert(0, w)
        else:
            temp.append(w)
            
    r.append(''.join(temp))

sys.stdout.write('\n'.join(r)+"\n")
