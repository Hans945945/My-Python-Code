while True:
    start, n1, n2, n3 = map(int, input().split())
    if start == 0 and n1 == 0 and n2 == 0 and n3 == 0:
        break
    n = 0
    if start > n1:
        n += start-n1
    else:
        n += start+40-n1
    if n2 < n1:
        n += n2+40-n1
    else:
        n += n2-n1
    if n3 < n2:
        n += n2-n3
    else:
        n += n2+40-n3
    n*= 9
    print(1080+n)
