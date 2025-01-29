n = int(input())
nums = [1]
for i in range(1,10001):
    nums.append(nums[i-1]*2)
while n != 0:
    try:
        print(nums[n])
        n = int(input())
    except:
        break
