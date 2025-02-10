import sys
data = sys.stdin.readlines()[1:]
idx = 0
r = []
i = 0
while idx < len(data):
    i += 1
    n = int(data[idx])
    total = 0
    best = float("inf")
    for _ in range(n):
        idx += 1
        m,s = map(int, data[idx].split())
        s+=m*60
        total += s
        best = min(best, s)
    avg = total // n
    r.append(f"Track {i}:")
    r.append(f"Best Lap: {best//60} minute(s) {best%60} second(s).")
    r.append(f"Average: {avg//60} minute(s) {avg%60} second(s).")
    r.append("")
    idx += 1
sys.stdout.write("\n".join(r)+"\n")
