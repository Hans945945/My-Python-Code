square = []
for i in range(1,int(100*(10**0.5))+1):
    square.append(i**2)
a,b = map(int, input().split())
while not(a == 0  and b == 0):
    if a ** 0.5  != int(a ** 0.5):
        square.append(a)
        square.sort()
        index_a = square.index(a)
        square.pop(square.index(a))
    else:
        index_a = square.index(a)
    if b ** 0.5  != int(b ** 0.5):
        square.append(b)
        square.sort()
        index_b = square.index(b)
        square.pop(square.index(b))
    else:
        index_b = square.index(b)+1
    print(len(square[index_a:index_b]))
    a,b = map(int, input().split())
    
        
