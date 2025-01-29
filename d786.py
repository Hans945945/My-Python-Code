n = int(input())
for _ in range(n):
    nums = list(map(int, input().split()))
    nums.pop(0)
    r = round(sum(nums)/len(nums),2)
    print(f'{r:.2f}')
