while True:
    try:
        n = int(input())
        nums = list(map(int, input().split()))
        for _ in range(n):
            print(min(nums), end = " ")
            nums.pop(nums.index(min(nums)))
        print()
    except:
        break
