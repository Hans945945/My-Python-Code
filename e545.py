T = int(input())
for _ in range(T):
    n = int(input())
    b = list(str(bin(n))).count("1")
    h = list(str(bin(int(str(n),16)))).count("1")
    print(b,h)
