n = int(input())
a = 0
b = 0
c = 0
for _ in range(n):
    num = int(input())
    if num % 3 == 0:
        a +=1
    elif num % 3 == 1:
        b +=1
    elif num % 3 == 2:
        c +=1
print(a,b,c)
