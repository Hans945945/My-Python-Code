import sys
r = []
for s in sys.stdin.readlines():
    r.append(f"{pow(int(s), (1/3)):.0f}")
sys.stdout.write("\n".join(r)+"\n")
