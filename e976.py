while True:
    #try:
        h,m,s = map(int, input().split())
        a = m/s
        if h >= a:
            print(f'{h} {m} {s}. I will make it!')
        else:
            print(f'{h} {m} {s}. I will be late!')
    except:
        break
