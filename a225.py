while True:
    try:
        n = int(input())
        nums = list(map(int, input().split()))
        for i in range(n):
            nums[i] = [nums[i]%10, -1*nums[i]]
        nums.sort()
        for i in range(n):
            print(nums[i][1]*-1, end = " ")
        print()
    except:
        break
