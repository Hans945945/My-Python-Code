import sys
data = sys.stdin.read().splitlines()
r = []
for s in data[:-1]:
    r.append(oct(int(s))[2:])
r.append("-1")
sys.stdout.write("\n".join(r)+"\n")
