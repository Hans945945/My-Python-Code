days = []
rain = []
for _ in range(7):
    nums = list(map(float, input().split()))
    days.append(sum(nums))
    rain.append(nums)
print(days.index(max(days))+1)
rain = zip(*rain)
rain = [sum(i) for i in rain]
time = rain.index(max(rain))
print("morning" if time == 0 else "afternoon" if time == 1 else "night" if time == 2 else "early morning")
    
