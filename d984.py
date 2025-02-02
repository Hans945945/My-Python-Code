import sys
for s in sys.stdin:
    candidates = sorted(list(zip(map(int, s.split()),["A","B","C"])))
    sys.stdout.write(candidates[1][1]+"\n" if candidates[0][0] + candidates[1][0] > candidates[2][0] else candidates[2][1]+"\n")
