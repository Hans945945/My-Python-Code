def find_cycle_length(n):
    count = 1
    while n != 1:
        if n%2 ==1:
            n = 3*n+1
        else:
            n = n/2
        count += 1
    return count
while True:
    try:
        iandj = list(map(int,input().split()))
        i = min(iandj)
        j = max(iandj)
        most = 0
        for k in range(i,j+1):
            r = find_cycle_length(k)
            if r > most:
                most = r
        print(iandj[0],iandj[1],most)
    except:
        break
