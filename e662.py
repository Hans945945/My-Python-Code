while True:
    D, N = input().split()
    if D == "0" and N == "0":
        break
    r = "".join([i for i in N if i != D])
    if r == "":
        r = 0       
    print(int(r))
    
