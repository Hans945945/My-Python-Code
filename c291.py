n = int(input())
nums = list(map(int, input().split()))
visited = [0]*n

count = 0
for i in range(n):
    if not visited[i]:
        now = i
        while not visited[now]:
            visited[now] = 1
            now = nums[now]
        count += 1
        
print(count)
