import sys
N = int(sys.stdin.readline())
count = 0
for n1 in range(1, 27):
    a1 = n1 * 20
    if a1 >= N:
        break
    for n2 in range(n1 + 1, 28):
        a2 = a1 + n2 ** 2
        if a2 >= N:
            break
        for n3 in range(n2 + 1, 29):
            a3 = a2 + n3 * 3
            if a3 >= N:
                break
            for n4 in range(n3 + 1, 30):
                a4 = a3 + (n3 + n4) * 4
                if a4 >= N:
                    break
                for n5 in range(n4 + 1, 31):
                    a5 = a4 + (n5 - n4) * 5
                    if a5 == N:
                        count += 1
                    elif a5 > N:
                        break

if count > 0:
    password = count ** 3
else:
    password = N * 5 - 3

sys.stdout.write(f"{password}\n")


