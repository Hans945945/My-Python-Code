while True:
    try:
        n = int(input())
        nums = []
        for _ in range(n):
            nums.append(int(input()))
        for _ in range(n):
            print(min(nums))
            nums.pop(nums.index(min(nums)))
    except:
        break
