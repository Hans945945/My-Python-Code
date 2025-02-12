import sys
data = sys.stdin.readlines()
N = int(data[0])
legal = {n.strip() for n in data[1:1+N]}
r = []
count = 0
for i in range(N+1,N+11):
    Id = data[i].strip()
    if Id[0] == "B" and Id[1:3].isdigit() and Id[3:7] in legal and Id[-2:].isdigit():
        r.append("Y")
    else:
        r.append("N")
        count += 1
r.append("0" if not count else "1" if count == 10 else f"0.{count}")
sys.stdout.write("\n".join(r)+"\n")


