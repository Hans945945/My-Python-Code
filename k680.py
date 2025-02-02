T = int(input())
for _ in range(T):
    o = input()
    a,b = map(int, input().split(o))
    print(a+b if o=="+" else a-b)
