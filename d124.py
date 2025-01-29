while True:
    try:
        data = list(input())
        if data[0] == "-":
            data.pop(0)
        nums = list(map(int, data))
        total = sum(nums)
        if total%3 == 0:
            print("yes")
        else:
            print("no")
    except:
        break
