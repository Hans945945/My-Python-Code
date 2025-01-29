def factors(n):
    total = 0
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            total += i
            if i != n**0.5:
                total += n//i
    return total-n
T = int(input())
for _ in range(T):
    n = int(input())
    total = factors(n)
    if n == total:
        print("perfect")
    elif n < total:
        print("abundant")
    else:
        print("deficient")

            
