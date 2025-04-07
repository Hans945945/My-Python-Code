B = int(input())
P = int(input())
flow = [0] * (B+1)

for _ in range(P):
    X, Y = map(int, input().split())
    for i in range(min(X, Y), max(X, Y)+1):
        flow[i] += 1

min_flow = min(flow[1:])
max_flow = max(flow[1:])
min_r = next(i for i in range(1, B+1) if flow[i] == min_flow)
max_r = max(i for i in range(1, B+1) if flow[i] == max_flow)

print(f"{min_r} {max_r}") 
