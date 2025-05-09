T = int(input())
for _ in range(T):
    n,w = map(int, input().split())
    grades = list(map(int, input().split()))
    for _ in range(w):
        nums = list(map(int, input().split()))
        if len(nums) == 2:
            print(grades[nums[1]])
        else:
            if nums[0] == 1:
                print(max(grades[nums[1]:nums[2]+1]))
            else:
                print(int(sum(grades[nums[1]:nums[2]+1])/(nums[2]-nums[1]+1)))
