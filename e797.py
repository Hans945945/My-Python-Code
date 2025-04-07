n, t = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(n)]

And = [1] * t
Or = [0] * t
Xor = [0] * t

for n in nums:
    for i in range(t):
        And[i] &= n[i]
        Or[i] |= n[i]
        Xor[i] ^= n[i]

print("AND:", *And)
print(" OR:", *Or)
print("XOR:", *Xor)
