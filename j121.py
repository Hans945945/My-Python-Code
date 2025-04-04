import sys
data = sys.stdin.readlines()
r = []

for idx in range(0, len(data), 2):
    a = data[idx].strip()
    b = data[idx+1].strip()

    count1 = {}
    for i in a:
        count1[i] = count1.get(i,0) + 1

    count2 = {}
    for i in b:
        count2[i] = count2.get(i,0) + 1

    r.append("YES" if sorted(count1.values()) == sorted(count2.values()) else "NO")

sys.stdout.write("\n".join(r) + "\n")
