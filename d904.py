c,n = map(int, input().split())
money = []
for _ in range(n):
    money.append(int(input()))
money.sort(reverse = True)
method = [i for i in range(0,1001*money[0], money[0])]
#method = [100000 for _ in range(1001)]
#method[0] = 0
for i in range(n):
    for j in range(money[i], c+1):
        method[j] = min(method[j], method[j-money[i]]+1)

print(method[c])
