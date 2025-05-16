s, e, a= map(int, input().split())  
day = 1
count = 0

while True:
    if s >= e:
        print(day)
        break
    day += 1    
    if day % 9 == 1 or day % 10 == 1:
        None
    elif day % 3 == 1:
        s += s//3
    else:
        s += s//10
    if day % 11 == 1:
        a-=1
    if a == 0:
        print("unsalable")
        break
