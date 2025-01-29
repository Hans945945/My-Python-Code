T = int(input())
for _ in range(T):
    num = ""
    for i in range(1, int(input())+1):
        num += str(i)
    print(" ".join(map(str, [num.count(str(i)) for i in range(10)])))
