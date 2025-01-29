while True:
    try:
        n,k = map(int, input().split())
        if n >= k:
            count = n
            while n >=k:
                count += int(n/k)
                n = int(n/k)+n%k
            print(count)
        else:
            print(n)
    except:
        break
