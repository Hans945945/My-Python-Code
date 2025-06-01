def correct(x):
    return int(str(abs(x)).zfill(m)[-m:]) * (-1 if x < 0 else 1)

n, c, m = map(int, input().split())
total = 0

for _ in range(n):
    a, b = map(int, input().split())
    power = 1
    for _ in range(b):
        power = correct(power * c)
    total = correct(total + correct(a * power))

print(str(abs(total)).zfill(m))




