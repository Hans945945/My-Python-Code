import sys
data = sys.stdin.readlines()
n = int(data.pop(0))
r = []
for i in range(0,n,2):
    data[i] = list(map(int, data[i].split()))
    data[i+1] = list(map(int, data[i+1].split()))
    temp = []
    for j in range(0,n,2):
        temp.append(str(max(data[i][j], data[i+1][j], data[i][j+1], data[i+1][j+1])))
    r.append(" ".join(temp))
sys.stdout.write("\n".join(r)+"\n")
