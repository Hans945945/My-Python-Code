while True:
    try:
        nums = list(map(int, input().split()))
        n = nums.pop(0)

        delta = [ 0 for x in range(n)]

        for i in range(1,n):
            d = abs(nums[i]-nums[i-1])
            if d <= n-1:
                delta[d] += 1

        isJolly = True

        for j in range(1,n):
            if delta[j] != 1:
                isJolly = False
                break
        if isJolly:
            print("Jolly")
        else:
            print("Not jolly")
    except:
        break
            
