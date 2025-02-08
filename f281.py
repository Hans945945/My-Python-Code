c = int(input())
whole_class = list(map(int, input().split()))
l = int(input())
whole_class.sort()
lowest = whole_class[0]
s_lowest = whole_class[1]
n = l - lowest
if s_lowest - n < l:
    print("You are too black!")
else:
    print(n)
