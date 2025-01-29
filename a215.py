while True:
    try:
        data = list(map(int, input().split()))
        n = data[0]
        m = data[1]
        total = n
        count = 1
        while total <= m:
            total = total+n+count
            count += 1
        print(count)
            
    except:
        break
