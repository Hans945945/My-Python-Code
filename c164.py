total = 0
k = int(input())
i = 0
o = 1
for _ in range(k):
    total += o
    i += 1
    if i == o:
        o += 1
        i = 0
print(total)
    
