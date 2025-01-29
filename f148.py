w, h = map(int, input().split())
n = int(input())
field = [input().replace(" ", "") for _ in range(w)]
count = 0
r = []
for t in range(97, 123):
    target = chr(t)
    x,y = -1, -1
    for i in range(w):
        for j in range(h):
            if field[i][j] == target:
                x,y = i,j
                break
    if x != -1:
        r.append(f"{x} {y}")
        count += 1
print("Mission fail." if count < n else "\n".join(r[:n]))
