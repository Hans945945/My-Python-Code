import sys
r = []
for s in sys.stdin:
    r.append(".".join(str(k) for k in (int(s)).to_bytes(4, 'big')))
sys.stdout.write("\n".join(r)+"\n")
