N = 1
total = 0
l = []
for i in range(1,101):
    total+=i**i
    l.append(total % 10)
    N +=1
n = int(input())
while n != 0:
    try:
        print(l[(n-1)%100])
        n = int(input())
    except:
        break
