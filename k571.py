n, k = map(int, input().split())
nums = list(map(int, input().split()))

left = 0
max_len = 0
count = 0

for right in range(n):
    if nums[right] < 2:
        count += 1
    while count > k:
        if nums[left] < 2:
            count -= 1
        left += 1
    max_len = max(max_len, right-left + 1)

print(max_len)
