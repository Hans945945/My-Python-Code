stairs = [1,1]+[0 for _ in range(9999)]
for i in range(2,10001):
    stairs[i] = stairs[i-1] + stairs[i-2]
while True:
    try:
        print(stairs[int(input())]%1000000007)
    except EOFError:
        break
