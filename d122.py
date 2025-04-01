import sys
r = []
for s in sys.stdin.readlines():
    n = int(s)
    ans = 0
    for i in range(1,15):
        ans += n//(5**i)
    r.append(f"{ans}")
sys.stdout.write("\n".join(r)+"\n")
