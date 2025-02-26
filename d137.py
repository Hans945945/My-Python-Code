import sys
r = []
for s in sys.stdin.readlines():
    s = s.strip().replace("i", "j")
    r.append(f"{abs(complex(s)):.3f}")
sys.stdout.write("\n".join(r) + "\n")
