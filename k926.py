s1,s2 = input(), input()
for _ in range(int(input())):
    a,b = input().split()
    s1 = s1.replace(a,b)
print(sum(1 for a,b in zip(s1,s2) if a != b))
