n = int(input())
grades = list(map(int, input().split()))
a = sum(grades)/n
if int(a) == a:
    print(int(a))
else:
    print(round(a,2))
