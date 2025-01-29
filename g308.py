n,t = map(int, input().split())
doors = list(map(int, input().split()))
food = list(map(int, input().split()))
eaten = 0
while doors[t] != -1:
    eaten += food[t]
    temp = t
    t = doors[t]
    doors[temp] = -1
print(eaten)
             
