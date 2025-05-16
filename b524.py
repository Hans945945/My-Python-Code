import sys
for s in sys.stdin:
    s = s.rstrip()
    pos = [i for i, ch in enumerate(s) if ch == 'y']
    print(sum(abs(pos[i] - 3 * i) for i in range(len(pos))))
