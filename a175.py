import sys
data = sys.stdin.read().splitlines()
index = 0
r = []
while index < len(data):
    k,m = map(int, data[index].split())
    hash_table = {i: {"NULL"} for i in range(m)}
    index += 1
    for s in data[index:index+k]:
        if s.strip() == '3':
            r.append("===== s =====")
            for i in range(m):
                r.append(f"[{i:03d}]:{' -> '.join(map(str, sorted(hash_table[i], key=lambda x: (isinstance(x, str), x))))}")
            r.append("===== e =====")
        else:
            t,n = map(int, s.split())
            if t == 1:
                hash_table[n%m].add(n)
            else:
                hash_table[n%m].discard(n)
                index += k

sys.stdout.write("\n".join(r)+"\n")
