import sys
import re

seen = []
r = []

for s in sys.stdin:
    s = s.rstrip()
    if s == "0":
        break

    temp = []

    words = re.findall(r"[A-Za-z]+|[^A-Za-z\d\s]+|\s+", s)

    for w in words:
        if re.fullmatch(r"[A-Za-z]+", w):
            if w in seen:
                idx = seen.index(w)
                temp.append(str(idx + 1))
                seen.insert(0, seen.pop(idx))
            else:
                temp.append(w)
                seen.insert(0, w)
        else:
            temp.append(w)

    r.append(''.join(temp))

sys.stdout.write('\n'.join(r) + '\n')
