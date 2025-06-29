while 1:
    try:
        def GCD(a,b):
            while b:
                a,b = b,a%b
            return a
        n = int(input())
        nums = [int(input()) for _ in range(n)]
        if n == 1:
            print(nums[0])
        else:
            a = GCD(nums[0],nums[1])
            for b in nums[2:]:
                a = GCD(a,b)
            print(a)
    except EOFError:
        break
