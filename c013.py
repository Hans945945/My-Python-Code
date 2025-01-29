n = int(input())
input()
for _ in range(n):
    a = int(input())
    f = int(input())
    for k in range(f):
        for i in range(1,a+1):
            for j in range(i):
                print(i, end = "")
            print()
        for i in range(1,a):
            for j in range(a-i):
                print(a-i, end = "")
            print()
        print()
