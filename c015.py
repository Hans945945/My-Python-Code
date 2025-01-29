N = int(input())
for _ in range(N):
    a = input()
    count = 0
    while True:
        b = a[::-1]
        a = str(int(a) + int(b))
        count += 1
        if a == a[::-1]:
            break
    print(count, a)
