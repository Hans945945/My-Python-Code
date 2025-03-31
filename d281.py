import sys
r = []
for s in sys.stdin.readlines()[:-1]:
    n = int(s)
    r.append(f"{n*25:.0f}%" if n != 1 else "0%")
sys.stdout.write("\n".join(r)+"\n")
