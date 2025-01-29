T = int(input())
for _ in range(T):
    N = int(input())
    a_i = list(map(int, input().split()))
    a = list(set(sorted(a_i)))
    times = []
    count = 0
    for i in a:
        times.append(a_i.count(i))
    if N < 3:
        print(0)
    elif len(times) == 3:
        if (a[0]^2) + (a[1]^2) == a[2]^2:
            count = times[0] * times[1] * times[2]
    else:
        N = len(a)
        for i in range(N-2):
            for j in range(i+1,N-1):
                for k in range(j+1,N):
                    if a[i]**2 + a[j]**2 == a[k]**2:
                        count += times[i] * times[j] * times[k]
    print(count)
                        
                        
