import sys

r = []
for s in sys.stdin.readlines()[1:]:
    n = int(s)
    if n == 1:
        r.append("1")
        continue

    c = 0
    flag = 1

    for i in range(2, int(n**0.5) + 1):
        count = 0
        while n % i == 0:
            n //= i
            count += 1
        if count > 0:
            c += 1
        if count >= 2:
            r.append("0")
            flag = 0
            break

    if flag:
        if n > 1:
            c += 1
        r.append(f"{(-1)**c}")

sys.stdout.write("\n".join(r) + "\n")

        
