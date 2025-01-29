import sys
data = sys.stdin.read().splitlines()
index = 1
r = []
T = int(data[0])
for _ in range(T):
    N, S = map(int, data[index].split())
    S *= S
    index += 1
    ducks = [data[i + index] for i in range(N)]
    index += N
    x0, y0 = map(int, data[index].split())
    index += 1
    count = 0
    for i in range(N):
        x, y = map(int, ducks[i].split())
        if (x-x0)**2 + (y-y0)**2 <= S:
            count += 1
    r.append(str(count))
sys.stdout.write("\n".join(r)+"\n")
        
    
        
