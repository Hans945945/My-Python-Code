import sys
data = sys.stdin.read().splitlines()
index = 0
r = []
while index < len(data):
    n = int(data[index])
    old = {}
    for _ in range(n):
        index += 1
        now = data[index].strip()
        if now in old:
            r.append(f"Old! {old[now]}")
        else:
            old[now] = len(old) + 1
            r.append(f"New! {old[now]}")
    index += 1
sys.stdout.write("\n".join(r) + "\n")
