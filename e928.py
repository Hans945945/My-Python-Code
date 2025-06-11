N1 = int(input())
a = list(map(int, input().split()))
N2 = int(input())
b = list(map(int, input().split()))

r = [0] * (N1 + N2 + 1)

for i in range(len(a)-1,-1,-1):
    for j in range(len(b)-1,-1,-1):
        r[i + j] += a[i] * b[j]

print(N1 + N2)
print(' '.join(map(str, r)))
