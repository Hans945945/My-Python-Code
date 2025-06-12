n = int(input())
for _ in range(n):
    a, b = map(int, input().split()) 
    r = str(a // b)
    m = a % b

    if m == 0:
        print(r+ ".(0)")
        continue

    decimals = [] 
    seen = {}     
    pos = 0

    flag = 1
    while m != 0:
        if m in seen:
            start = seen[m]
            flag = 0
            print(r + "." + ''.join(decimals[:start]) + "(" + ''.join(decimals[start:]) + ")")
            break

        seen[m] = pos
        m *= 10
        decimals.append(str(m // b))
        m %= b
        pos += 1
        if pos == 50:
            start = 50
            print(r + "." + "(" + ''.join(decimals[:start]) + ''.join(decimals[start:]) + "...)")
            flag = 0
            break

    if flag:
        print(r + "." + ''.join(decimals) + "(0)")
