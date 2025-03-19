import sys
data = sys.stdin.readlines()
T = int(data.pop(0))
r = []
for i in range(0,T*2,2):
    n = int(data[i])
    farms = list(data[i+1])
    idx = 0
    count = 0
    while idx < n:
        if farms[idx] == ".":
            count += 1
            idx += 2
        idx += 1
    r.append(f"Case {i//2+1}: {count}")
sys.stdout.write("\n".join(r)+"\n")
