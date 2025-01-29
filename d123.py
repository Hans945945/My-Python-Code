count = 1
while True:
    try:
        n = int(input())
        nums = list(map(int, input().split()))
        seen = []
        if len(nums) != len(set(nums)):
            print(f"Case #{count}: It is not a B2-Sequence.")
            count += 1
            print()
            continue  
        if any(num < 1 for num in nums) or sorted(nums) != nums:
            print(f"Case #{count}: It is not a B2-Sequence.")
        else:
            for i in range(n):
                for j in range(i, n):
                    total = nums[i] + nums[j]
                    seen.append(total)
        if len(seen) != len(set(seen)):
            print(f"Case #{count}: It is not a B2-Sequence.")
        else:
            print(f"Case #{count}: It is a B2-Sequence.")

        count +=1

        print()

    except EOFError:
        break
