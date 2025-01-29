n = int(input())
overall = []
for _ in range(n):
    a,d = map(int, input().split())
    temp = [a**2+d**2,a,d]
    overall.append(temp)
overall.sort(reverse = True)
print(overall[1][1],overall[1][2])
