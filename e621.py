N = int(input())
for _ in range(N):
    a,b,c = map(int, input().split())
    p = [i for i in range(a+1,b)]
    No = True
    for i in range(len(p)):
        if p[i] % c != 0:
            print(p[i], end = " ")
            No = False
    if No:
        print("No free parking spaces.")
    else:
        print()
            
