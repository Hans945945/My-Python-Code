n,m = 15,30
Defult = [list(input()) for i in range(n)]
Map = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        if Defult[i][j] == "*":
            if i != 0 and j < m-1:
                if Defult[i-1][j+1] != "*":
                    Map[i-1][j+1] += 1
                else:
                    Map[i-1][j+1] = "*"
            if i != 0 and j != 0:
                if Defult[i-1][j-1] != "*":
                    Map[i-1][j-1] += 1
                else:
                    Map[i-1][j-1] = "*"
            if i < n-1 and j != 0:
                if Defult[i+1][j-1] != "*":
                    Map[i+1][j-1] += 1
                else:
                    Map[i+1][j-1] = "*"
            if i < n-1 and j < m-1:
                if Defult[i+1][j+1] != "*":
                    Map[i+1][j+1] += 1
                else:
                    Map[i+1][j+1] = "*"
            if i != 0:
                if Defult[i-1][j] != "*":
                    Map[i-1][j] += 1
                else:
                    Map[i-1][j] = "*"
            if i < n-1:
                if Defult[i+1][j] != "*":
                    Map[i+1][j] += 1
                else:
                    Map[i+1][j] = "*"
            if j != 0:
                if Defult[i][j-1] != "*":
                    Map[i][j-1] += 1
                else:
                    Map[i][j-1] = "*"
            if j < m-1:
                if Defult[i][j+1] != "*":
                    Map[i][j+1] += 1
                else:
                    Map[i][j+1] = "*"
            Map[i][j] = "*"
for i in range(n):
    for j in range(m):
        if Map[i][j] == 0:
            print(".", end = "")
        else:
            print(Map[i][j],end = "")
    print()
