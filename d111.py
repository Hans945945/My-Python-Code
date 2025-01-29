import math
n = -1
while n != 0:
    try:
        n = int(input())
        r = "no"
        if n != 0:
            i = math.floor(math.sqrt(n))
            if i**2 == n:
                    r = "yes"
            print(r)
    except:
        break
