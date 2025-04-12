import math

def is_prime(x):
    if x <= 1:
        return 1
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return 0
    return 1

n = int(input())
x = n + 1
while not is_prime(x):
    x += 1
y = int(pow(n,1/3))
while (y ** 3) <= n:
    y += 1

print(
    x,
    (int(n**0.5) + 1) ** 2,
    y**3
)




