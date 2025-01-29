nums = input().strip()
code = int(nums[6:])

first, second = -1, -1
for digit in nums:
    num = int(digit)
    if num > first:
        second = first
        first = num
    elif num > second:
        second = num
check = first**2 + second**2
print("Good Morning!" if code == check else "SPY!")

