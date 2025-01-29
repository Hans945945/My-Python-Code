n = int(input())
r = 0
for _ in range(n):
    call = list(input())
    if call[1] == "+":
        r += 1
    else:
        r -= 1
print(r)
