n = int(input())
a = 0
while True:
    if n - a > 0 and all(d in '02468' for d in str(n-a)):
        print(a)
        break
    if all(d in '02468' for d in str(n+a)):
        print(a)
        break
    a += 1
