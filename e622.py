n,S = map(int, input().split())
pets = []
Id = 0
time = S//1000
for i in range(0, n):
    Id += 1
    CP, IV = map(int, input().split())
    if IV <= 29:
        pets.append(CP+10*time)
    elif IV <= 39:
        pets.append(CP+50*time)
    else:
        pets.append(CP+100*time)
r = max(pets)
print(pets.index(r)+1, r)
