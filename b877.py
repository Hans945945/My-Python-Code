a,b = map(int, input().split())
r = (a>b)*(100-a+b) + (a<=b)*(b-a)
print(r)
