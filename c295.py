nums = list(map(int, input().split()))
n = nums[0]
m = nums[1]
total = 0
numbers = []
count = 0
for i in range(n):
    xi = list(map(int, input().split()))
    total += max(xi)
    numbers.append(max(xi))
print(total)
for i in numbers:
    if total % i == 0:
        if count == 0:
            count += 1
            print(i,end="")
        else:
            count += 1
            print(" "+str(i),end="")
if count == 0:
    print(-1)
    
