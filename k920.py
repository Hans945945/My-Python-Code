t = input()
a,b,c = map(int, input().split())
print((a-b-1)//(b-c)+2 if t == "A" else a+b-1)
