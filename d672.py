def check(n):
    n = sum(map(int, list(str(n))))
    if n == 9:
        return 1
    else:
        return check(n) +1
n = int(input())
while n != 0:
    if n % 9 ==0:
        degree = check(n)
        print(f'{n} is a multiple of 9 and has 9-degree {degree}.')
    else:
        print(f'{n} is not a multiple of 9.')
    n = int(input())
