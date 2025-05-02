x,n = map(int, input().split())
foods = list(map(int, input().split()))
left = right = 0
for f in foods:
    if f > x:
        right += 1
    else:
        left += 1
if right > left:
    print(right, max(foods))
else:
    print(left, min(foods))
