n = int(input())
sqrt_n = n**0.5
if sqrt_n == int(sqrt_n):
    print(int(sqrt_n))
else:
    a = b = 1
    for i in range(2,int(sqrt_n)+1):
        count = 0
        while n % i == 0:
            count += 1
            n //= i
        if count != 0:
            a*=i**(count//2)
            if count % 2 == 1:
                b*=i
    if n != 1:
        b*=n
    if a == 1:
        print(f"sqrt({b})")
    else:
        print(f"{a} sqrt({b})")
