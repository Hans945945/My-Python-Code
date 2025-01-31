import sys
from collections import Counter
r = []
for s in sys.stdin:
    words = [w.lower() for w in s.strip() if w.isalpha()]
    temp = "yes !"
    count = 0
    for value in Counter(words).values():
        if value % 2 == 1:
            count += 1
        if count > 1:
            temp = "no..."
            break
    r.append(temp)
sys.stdout.write("\n".join(r)+"\n")
