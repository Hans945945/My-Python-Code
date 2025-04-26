a,b,c, = map(int, input().split())
d,e,f = map(int, input().split())
n = int(input())
max_profit = float('-inf')
for i in range(n+1):
    temp = a*i*i+b*i+c + d*(n-i)**2 + e*(n-i) + f
    max_profit = max(temp, max_profit)
print(max_profit)
