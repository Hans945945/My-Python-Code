import sys
r = []
for s in sys.stdin.readlines()[1:]:
    now = s.strip()
    r.append(min(now.count("M"), now.count("A")//3, now.count("R")//2, now.count("G"), now.count("I"), now.count("T")))
sys.stdout.write("\n".join(map(str, r))+"\n")
