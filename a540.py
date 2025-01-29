from itertools import accumulate

def max_sum(nums):
    maximum_sum = -1000
    minimum = 0
    for current_sum in accumulate(nums):
        maximum_sum = max(maximum_sum, current_sum - minimum)
        minimum = min(minimum, current_sum)
    return maximum_sum
n = int(input())
while n != 0:
    money = list(map(int, input().split()))
    r = max_sum(money)
    if r <= 0:
        print("Losing streak.")
    else:
        print(f"The maximum winning streak is {r}.")
    n = int(input())
    
