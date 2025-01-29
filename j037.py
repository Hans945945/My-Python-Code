nums = list(map(int, input().split()))
while nums.count(0)!= 3:
    try:
        nums.sort()
        if nums[2] **2 == nums[1]**2 + nums[0]**2:
            print("right")
        else:
            print("wrong")
        nums = list(map(int, input().split()))
    except:
        break
