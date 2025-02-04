a, b = map(int, input().split())
c = a + b
n = int(input())
children = list(map(int, input().split()))
total = 0
for sec in children:
    d = sec % c
    if d >= a:
        total += c - d
print(total)
