for i in range(int(input())):
        y = int(input())
        if y % 4 == 0 and y % 100 != 0 or y%400 == 0:
            print("Case",str(i+1)+":","a leap year")
        else:
            print("Case",str(i+1)+":","a normal year")
