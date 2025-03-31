import sys
r = []
for s in sys.stdin:
    nums = list(map(int, s.split()))
    max_n = now = 0
    for n in nums:
        now = max(n,now+n)
        max_n = max(max_n, now)
    r.append(f"{max_n}")
sys.stdout.write("\n".join(r)+"\n") 
