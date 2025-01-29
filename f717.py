Class = list(map(int, input().split()))
r = sum(Class)%len(Class)
print(r if r != 0 else len(Class))
