n = int(input())

is_prime = [1] * (n + 1)
is_prime[0] = is_prime[1] = 0

for i in range(2, int(n ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, n + 1, i):
            is_prime[j] = 0

count = 0
for i in range(2, n - 1):
    if is_prime[i] and i + 2 <= n and is_prime[i + 2]:
        count += 1

print(count)
