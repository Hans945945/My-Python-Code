n = int(input())
print("Lumberjacks:")
for _ in range(n):
    i = list(map(int, input().split()))
    print("Ordered" if sorted(i) == i or sorted(i, reverse = True) == i else "Unordered")
