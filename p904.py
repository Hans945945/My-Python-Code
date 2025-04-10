n = int(input())
spend = sum(map(int, input().split()))
if n<=10:
    pass
elif n <= 20:
    spend*=0.95
elif n <= 40:
    spend*=0.9
else:
    spend*=0.85
spend = int(spend+0.5)
print(min(1200,spend))
