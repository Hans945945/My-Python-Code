from itertools import combinations
H = int(input())
N = int(input())

trips = [
    {1, 2, 3, 5, 6, 8, 11, 13, 17, 21, 22},
    {2, 3, 5, 7, 8, 13, 16, 17, 21, 22, 24},
    {1, 3, 5, 6, 7, 15, 16, 17, 22, 23, 24, 25},
    {2, 4, 5, 7, 8, 15, 17, 21, 23, 25}
]

Count = {1: 2, 2: 3, 3: 3, 4: 1, 5: 4, 6: 2, 7: 3, 8: 3, 11: 1, 
    13: 2, 15: 2, 16: 2, 17: 4, 21: 3, 22: 3, 23: 2, 24: 2, 25: 2 }

sort_count = sorted([place for place, count in Count.items() if count >= H])

count = 0
for combo in list(combinations(sort_count, N)):
    if sum(1 for trip in trips if set(combo).issubset(trip)) >= H:
        count += 1

print(count)
