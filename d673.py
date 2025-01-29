s = int(input())
x = 0
while s >= 0:
    q = list(map(int, input().split()))
    n = list(map(int, input().split()))
    x+=1
    print(f"Case {x}:")
    for i in range(12):
        if s + sum(q[:i])>= n[i]:
            s -= n[i]
            print("No problem! :D")
        else:
            print("No problem. :(")
    s = int(input())
