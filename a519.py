ancestors = [1,1]
for i in range(2,81):
    ancestors.append(ancestors[i-1]+ancestors[i-2])
while True:
    n = int(input())
    if n == 0:
        break
    print(ancestors[n])
