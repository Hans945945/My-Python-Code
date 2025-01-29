n = int(input())
c = list(map(int,input().split()))
r = []
found = False
bs = -1
ws = -1
for i in range(n):
    r.append(c.pop(c.index(min(c))))
    print(r[-1], end = " ")
    if not found and r[-1]>=60:
        if len(r) == 1:
            ws = "best case"
        else:
            ws = r[-2]
        bs = r[-1]
        found = True
print()
if bs == -1:
    bs = "worst case"
if ws == -1:
    ws = r[-1]
print(ws)
print(bs)

