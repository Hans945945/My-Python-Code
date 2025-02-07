import sys
price_one = list(map(int, sys.stdin.readline().split()))
price_two = list(map(int, sys.stdin.readline().split()))
min_price = float("inf")
fd = ld = 0
n = 10
for i in range(n):
    for j in range(i,n):
        price= price_one[i] + price_two[j] + 1000*(j-i)
        if price < min_price:
            min_price = price
            fd,ld = i+1,j+1
print(fd,ld,min_price)
