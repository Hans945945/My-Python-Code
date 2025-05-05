n = int(input())
if  n <= 3:
    print(1)
else:
    n = (n - 4) % 2781668
    a = b = c = 1

    for _ in range(n+1):
        a, b, c = b, c, (a + b + c) % 10007
        
    print(c)
