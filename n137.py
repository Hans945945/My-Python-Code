N = int(input())
for _ in range(N):
    names = input().split()
    nums = input().split()
    temp = []
    for i in range(len(nums)):
        temp.append((names[i], int(nums[i])))
    temp.sort()
    print("\n".join(f"{n} {v}" for n,v in temp))
