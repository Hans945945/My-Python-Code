import sys
r = []
for s in sys.stdin.readlines():
    n = int(s)
    extra = (n < 0)*"i"
    n = abs(n)
    a = 1
    b = 1
    i = 2
    while i * i <= n:
        count = 0
        while n % i == 0:
            count += 1
            n //= i
        if count > 0:
            a *= i ** (count // 2)
            if count % 2 == 1:
                b *= i
        i += 1
    if n > 1:
        b *= n
    temp = f"{a if a > 1 else ''}{f'_/{b}' if b > 1 else ''}{extra}"
    r.append(temp if temp else "0")
sys.stdout.write("\n".join(r)+"\n")
