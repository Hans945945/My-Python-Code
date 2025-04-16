prices = list(map(int, input().split()))
min_price = prices[0]
max_profit = 0

for price in prices:
    max_profit = max(max_profit, price - min_price)
    min_price = min(min_price, price)

print(max_profit)
