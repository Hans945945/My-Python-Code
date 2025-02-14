import sys
r = []
data = sys.stdin.readlines()
T = int(data.pop(0))
case = 0
for i in range(0,T*2,2):
    case += 1
    n = int(data[i])
    walls = list(map(int, data[i+1].split()))
    high = 0
    low = 0
    for j in range(1,n):
        if walls[j-1] < walls[j]:
            high += 1
        elif walls[j-1] > walls[j]:
            low += 1
    r.append(f"Case {case}: {high} {low}")
sys.stdout.write("\n".join(r)+"\n")
    
