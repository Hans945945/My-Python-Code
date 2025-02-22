people = list(map(int, input().split()))
people.sort()
c = sum(people)//4 - people[0] - people[9]
a = people[1]-c
b = people[0]-a
e = people[8]-c
d = people[9]-e
print(a,b,c,d,e)
