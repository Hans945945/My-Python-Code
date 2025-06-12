idx = 0
while True:
    idx += 1
    n,q = map(int, input().split())
    if n == 0 and q == 0:
        break
    temp = [int(input()) for i in range(n)]
    marbles = {}
    seen = set()
    for i, v in enumerate(sorted(temp)):
        if v not in seen:
            seen.add(v)
            marbles[v] = i
    print(f"CASE# {idx}:")
    for _ in range(q):
        now = int(input())
        find = marbles.get(now,-1)
        print(f"{now} found at {find+1}" if find != -1 else f"{now} not found")
        
