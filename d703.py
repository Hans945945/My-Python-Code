import sys

def backtrack(counter, path, n, r):
    if len(path) == n:
        r.append("".join(path))
        return
    for ch in counter:
        if counter[ch] > 0:
            counter[ch] -= 1
            path.append(ch)
            backtrack(counter, path, n, r)
            path.pop()
            counter[ch] += 1

r = []
for s in sys.stdin:
    n, m = map(int, s.split())
    counter = {"S":n, "L":m}
    temp = []
    backtrack(counter, [], n+m, temp)
    r.extend(temp)
    r.append("")
    
sys.stdout.write("\n".join(r))
