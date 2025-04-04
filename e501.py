import sys

data = sys.stdin.read().splitlines()
T = int(data[0])
i = 1
r = []

for _ in range(T):
    while i < len(data) and data[i].strip() == "":
        i += 1

    keys = data[i].strip()
    i += 1
    values = data[i].strip()
    i += 1

    trans = {keys[j]: values[j] for j in range(len(keys))}

    r.append(values)
    r.append(keys)

    while i < len(data) and data[i].strip() != "":
        r.append("".join(trans.get(c, c) for c in data[i].strip()))
        i += 1

    r.append("")

sys.stdout.write("\n".join(r[:-1]) + "\n")
