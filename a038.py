num = int(input())
nums = []
new_num = 0

while num>= 10:
    nums.insert(0,num%10)
    num = num //10
nums.insert(0,num)
size = len(nums)
while size >1:
    new_num = new_num + nums.pop()*(10**(size-1))
    size = len(nums)
new_num = new_num + nums[0]
print(new_num)
