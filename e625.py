while True:
    try:
        data = input().split()
        for i in range(len(data)):
            data[i] = list(data[i])
            for j in range(len(data[i])-1,-1,-1):
                print(data[i][j],end = "")
            print(" ", end= "")
        print()
    except:
        break
