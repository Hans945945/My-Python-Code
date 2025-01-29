data = input().split()
a = int(data[0])
b = int(data[1])

n = int(input())

count = 0

for _ in range(n):
    items = list(map(int, input().split()))
    items.pop()
    take_out = []
    buy = []
    A = False
    B = False
    index = 0
    for i in range(len(items)):
        if items[i] > 0:
            buy.append(items[i])
        else:
            take_out.append(items[i])
    for i in range(len(buy)):
        for j in range(len(take_out)):
            if buy[i] == abs(take_out[j]) and items.count(take_out[j]):
                index = items.index(buy[i])
                items.pop(index)
                index = items.index(take_out[j])
                items.pop(index)
    for i in range(len(items)):
        if items[i] == a :
            A = True
        if items[i] == b :
            B = True
    
    
    if A and B:
        count += 1

print(count)
