int_to_g = {i: chr(i + 65) for i in range(26)}
g_to_int = {chr(i + 65): i for i in range(26)}

while True:
    try:
        n = input().rstrip()
        if not n:
            continue
        a, b = input().rstrip(), input().rstrip()
    except EOFError:
        break

    n = len(a)
    powers = [26**i for i in reversed(range(n))]
    c = sum((g_to_int[a[i]] + g_to_int[b[i]]) * powers[i] for i in range(n))

    r = []
    if c == 0:
        r.append("A")
    while c > 0:
        r.append(int_to_g[c % 26])
        c //= 26
    print("".join(r[::-1]))
