import sys

data = sys.stdin.readlines()
T = int(data.pop(0).strip())
r = []
idx = 0

for _ in range(T):
    count = {}
    total_trees = 0

    while idx < len(data) and not data[idx].strip():
        idx += 1

    while idx < len(data) and data[idx].strip():
        tree = data[idx].strip()
        count[tree] = count.get(tree, 0) + 1
        total_trees += 1
        idx += 1

    idx += 1

    for tree in sorted(count):
        percentage = (count[tree] / total_trees) * 100
        r.append(f"{tree} {percentage:.4f}")

    r.append("")

sys.stdout.write("\n".join(r[:-1]) + "\n")
