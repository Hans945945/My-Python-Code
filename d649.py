n = int(input())
while n != 0:
    for i in range(n):
        for _ in range(n-i-1):
            print("_",end = '')
        for _ in range(i+1):
            print("+",end = '')
        print()
    n = int(input())
