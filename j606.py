k,q,r = map(int, input().split())
words = list(input())
output = []
for _ in range(q):
    nums = list(map(int, input().split()))
    temp = [0 for i in range(k)]
    for j in range(k):
        temp[nums[j]-1] = words[j]
    output.append(temp)
    words = temp
for i in range(r):
    for j in range(q):
        print(output[j][i], end = "")
    print()
    
