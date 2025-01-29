nums = list(map(int, input().split()))
n = nums[0]
m = nums[1]
r = []
for i in range(n,m+1):
    data = list(str(i))
    N = len(data)
    count = 0
    for j in range(N):
        count += int(data[j])**N
    if count == i:
        r.append(i)
if len(r) == 0:
    print("none")
else:
    for i in range(len(r)):
        print(r[i],end = " ")
