squares = [0]*101
for i in range(1,101):
    squares[i] = i*i + squares[i-1]
while True:
    n = int(input())
    if n == 0:
        break
    print(squares[n])
