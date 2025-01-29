while True:
    n = input()
    if n == "0":
        break
    while len(n) != 1:
        total = 0
        for i in n:
            total += int(i)
        n = str(total)
    print(n)
