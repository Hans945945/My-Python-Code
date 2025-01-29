while True:
    try:
        data = list(map(int, input().split()))
        n = data[0]
        nums = []
        for i in range(1,int(n)+1):
            nums.append(data[i])
        r = sum(nums)/n
        if r > 59:
            print("no")
        else:
            print("yes")
    except:
        break
    
