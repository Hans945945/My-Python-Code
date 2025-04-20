n = int(input())
nums = list(map(int, input().split()))
min_n = nums[0]
i = max_income = buy = sell = 0
min_idx = 1
for n in nums:
    i+= 1
    if n - min_n > max_income:
        max_income = n - min_n
        sell = i
        buy = min_idx
    if n < min_n:
        min_n = n
        min_idx = i
print(f"{buy} {sell}" if buy or sell else -1)
