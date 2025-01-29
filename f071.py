a,b,c = map(int, input().split())
lottery = list(zip(map(int, input().split()), map(int, input().split())))
total = 0
double = 1
for n, price in lottery:
    if n == a:
        total += price
    if n == b:
        total += price
    if n == c:
        total -= price
        double = 0
if double:
    total *= 2
print(max(0, total))
