n = int(input())
x = 0
while n >= 0:
    x += 1
    b_n = bin(n)[2:]
    print(f'Case {x}: {len(b_n) - (list(str(b_n)).count("1") == 1)}')
    n = int(input())
