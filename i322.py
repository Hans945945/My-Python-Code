def hanoi(n,a,b,c):
    if n == 1:
        print(f"Move disc 1 from {a} to {c}")
    else:
        hanoi(n-1,a,c,b)
        print(f"Move disc {n} from {a} to {c}")
        hanoi(n-1,b,a,c)
hanoi(int(input()),"A","B","C")
        
