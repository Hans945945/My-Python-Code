prices = list(map(int, input().split()))
max_profit = 0
min_price = prices[0]
buy = sell = -1
for price in prices:
    profit = price - min_price
    if profit > max_profit:
        max_profit = profit
        buy = min_price
        sell = price
    min_price = min(price, min_price)
print(max_profit, buy, sell)
