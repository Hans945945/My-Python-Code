n = int(input())
chains = []
for _ in range(n):
    temp = list(map(int, input().split()))
    temp.pop(0)
    chains.append(min(temp))
print(max(chains))
