x = int(input())
n = [0 for _ in range(x+1)]
n[1] = 1
for i in range(2, x+1):
    n[i] = n[i-1]+i*i-i+1
print(n[-1])
