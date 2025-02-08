import sys
show = set()
r= []
for s in sys.stdin:
    line = s.strip()
    r.append("YES" if line in show else "NO")
    show.add(line)
sys.stdout.write("\n".join(r)+"\n")
