import sys
r = []
for s in sys.stdin.readlines()[:-1]:
    n = int(s)
    if n == 0:
        r.append("0")
        continue
    temp = []
    while n > 0:
        temp.append(n%3)
        n//=3
    r.append("".join(map(str, temp[::-1])))
sys.stdout.write("\n".join(r)+"\n")
