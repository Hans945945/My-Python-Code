case = 1
while True:
    try:
        s = input()
        print(f"Case {case}:")
        n = int(input())
        for _ in range(n):
            i,j = sorted(map(int, input().split()))
            now = s[i]
            flag = 1
            for k in range(i+1,j+1):
                if s[k] != now:
                    print("No")
                    flag = 0
                    break
            if flag:
                print("Yes")
        case+=1
    except EOFError:
        break
        
        
