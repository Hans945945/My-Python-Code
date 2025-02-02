T = int(input())
for _ in range(T):
    a,b = map(int, input().split("+"))
    ans = int(input())
    print("yes" if a+b == ans else "no")
