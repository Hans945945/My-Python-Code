while True:
    try:
        n = int(input())
        S = 0
        for i in range(2, int(n**0.5)+1):
            if n % i ==0:
                S += i
                S += n//i
                if i == n**0.5:
                    S-=i
        S += 1
        if S < n:
            print("虧數")
        elif S == n:
            print("完全數")
        else:
            print("盈數")
    except:
        break
