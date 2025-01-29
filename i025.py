n = int(input())
total = 0
sqrt_n = n**0.5
for i in range(2, int(sqrt_n)+1):
    if n % i == 0:
        total += i
        total += n//i
if int(sqrt_n) == sqrt_n:
    total -= int(sqrt_n)
total += 1
print(total)
