k,n = map(int, input().split())
lucky = [input(),input(),input()]
total = 0
for _ in range(n):
    now = input()
    max_p = 0
    for l in lucky:
        if l == now:
            max_p = 500000
            break
        if l[2:] == now[2:]:
            max_p = 10000
        elif l[4:] == now[4:]:
            max_p = max(max_p,1000)
        elif l[-3:] == now[-3:]:
            max_p = max(max_p,300)
    total += max_p
print(total)
        
