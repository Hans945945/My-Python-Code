from collections import defaultdict
n = int(input())
food = defaultdict(set)
for _ in range(n):
    f,s = input().split()
    food[s].add(f)
temp = food.get(input(), "No")
print("\n".join(sorted(temp)) if temp != "No" else temp)
