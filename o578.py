l,w,h,k = map(int, input().split())
if l%k == 0 and w%k ==0 and h%k == 0:
    print((l*w*h) // (k**3))
else:
    print(0)
