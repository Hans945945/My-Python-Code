n = int(input())
found = 0

for d in range(1, 100):
    m = int(str(d)[::-1])
    if m < 10:
        m*=10
    if 18 <= m and m+n <= 99 and m + n == 2 * (d + n):
        print(d)
        found = 1
        break

if not found:
    print("no answer")
