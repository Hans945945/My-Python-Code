for _ in range(int(input())):
    H1, M1, H2, M2, M3 = map(int, input().split())
    T = (H2*60+M2)-(H1*60+M1)
    if  T>=M3:
        print("Yes")
    else:
        print("No")
    
