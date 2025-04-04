import sys
data = sys.stdin.readlines()
r = []
for i in range(1,len(data),2):
    nums = list(map(int, data[i].split()))
    if not nums:
        continue

    max_prod = 0
    curr_max = 1
    curr_min = 1

    for num in nums:
        if num == 0:
            curr_max, curr_min = 1, 1
            max_prod = max(max_prod, 0)
            continue

        temp = curr_max * num
        curr_max = max(num, temp, curr_min * num)
        curr_min = min(num, temp, curr_min * num)

        if curr_max > 0:
            max_prod = max(max_prod, curr_max)

    r.append(f"Case #{(i+1)//2}: The maximum product is {max_prod}.\n")

sys.stdout.write("\n".join(r) + "\n")
