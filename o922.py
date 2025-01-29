N = int(input())
p = list(map(int, input().split()))
x,g = map(int, input().split())
c = 0
while not(x == 0 and g ==0):
    c+=p[x-1]*g
    x,g = map(int, input().split())
print(c)
