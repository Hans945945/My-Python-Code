n = int(input())

lst = list(map(int, input().split()))

total = 0

for i in range(len(lst)):
    if lst[i] == 0:
        if i == 0:
            total += lst[1]
        
        elif (i == len(lst)-1):
            total += lst[-2]
        else:
            total += min(lst[i-1],lst[i+1])
print(total)
