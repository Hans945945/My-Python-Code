k = int(input())
x1,y1 = map(int, input().split())
x2,y2 = map(int, input().split())
ans = 0
while k > 0:
    ans += k
    if ans % x1 == 0:
        k -= y1
    if ans % x2 == 0:
        k -= y2
print(ans)
