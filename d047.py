while True:
    try:
        year = int(input())
        ordinary = 1
        leap = 0
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            print("This is leap year.")
            ordinary = 0
            leap = 1
        if year % 15 == 0:
            print("This is huluculu festival year.")
            ordinary = 0
        if leap and year % 55 == 0:
            print("This is bulukulu festival year.")
            ordinary = 0
        if ordinary:
            print("This is an ordinary year.")
        print()
    except EOFError:
        break
