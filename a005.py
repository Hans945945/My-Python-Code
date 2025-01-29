import sys
t = int(input())
c = 0

while t != c:
    for s in sys.stdin:
        c = c+1
        lst = s.split()
        if int(lst[1]) - int(lst[0]) == int(lst[2]) - int(lst[1]):
            num = int(lst[3]) + (int(lst[1]) - int(lst[0]))
        else:
            num = int(lst[3])*(int(lst[1]) // int(lst[0]))
        print(lst[0], lst[1], lst[2], lst[3],num)
