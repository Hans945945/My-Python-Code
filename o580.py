def factors(n):
    count = 0
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            count+=2
    if n**0.5 != int(n**0.5):
        count += 1
    return count+1
a,b = map(int, input().split())
m = 0
max_n = -1
for i in range(a, b+1):
    n = factors(i)
    if n > max_n:
        max_n = n
        m = i
print(m,max_n)
