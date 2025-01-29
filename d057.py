x1, y1, x2, y2 = map(int, input().split())
while not(x1 ==0 and y1 ==0 and x2 == 0 and y2 ==0):
    x_d = abs(x1-x2)
    y_d = abs(y1-y2)
    if x_d == 0 and y_d == 0:
        print(0)
    elif x_d == 0 or y_d == 0 or x_d == y_d:
        print(1)
    else:
        print(2)
    x1, y1, x2, y2 = map(int, input().split())
        
