r,c = map(int, input().split())
marker = [list(map(int, input().split())) for i in range(r)]
arr = [[0 for i in range(c)] for j in range(r)]
for i in range(r):
    for j in range(c):
        if marker[i][j] == 5:
            if i != 0 and j < c-1:
                if marker[i-1][j+1] == 5:
                    arr[i][j] = 3
                    arr[i-1][j+1] = 3
            if i != 0 and j != 0:
                if marker[i-1][j-1] == 5:
                    arr[i][j] = 3
                    arr[i-1][j-1] = 3
            if i < r-1 and j != 0:
                if marker[i+1][j-1] == 5:
                    arr[i][j] = 3
                    arr[i+1][j-1] = 3
            if i < r-1 and j < c-1:
                if marker[i+1][j+1] == 5:
                    arr[i][j] = 3
                    arr[i+1][j+1] = 3
            if i != 0:
                if marker[i-1][j] == 5:
                    arr[i][j] = 3
                    arr[i-1][j] = 3
            if i < r-1:
                if marker[i+1][j] == 5:
                    arr[i][j] = 3
                    arr[i+1][j] = 3
            if j != 0:
                if marker[i][j-1] == 5:
                    arr[i][j] = 3
                    arr[i][j-1] = 3
            if j < c-1:
                if marker[i][j+1] == 5:
                    arr[i][j] = 3
                    arr[i][j+1] = 3
            if arr[i][j] == 0:
                arr[i][j] = 5
found, count = 0,0
for i in range(r):
    for j in range(c):
        if marker[i][j] == 1:
            f = True
            count += 1
            if i != 0 and j < c-1 and f:
                if arr[i-1][j+1] == 5:
                    found +=1
                    f = False
            if i != 0 and j != 0 and f:
                if arr[i-1][j-1] == 5:
                    found +=1
                    f = False
            if i < r-1 and j != 0 and f:
                if arr[i+1][j-1] == 5:
                    found +=1
                    f = False
            if i < r-1 and j < c-1 and f:
                if arr[i+1][j+1] == 5:
                    found +=1
                    f = False
            if i != 0 and f:
                if arr[i-1][j] == 5:
                    found +=1
                    f = False
            if i < r-1 and f:
                if arr[i+1][j] == 5:
                    found +=1
                    f = False
            if j != 0 and f:
                if arr[i][j-1] == 5:
                    found +=1
                    f = False
            if j < c-1 and f:
                if arr[i][j+1] == 5:
                    found +=1
                    f = False
not_found = count - found
print(found, not_found)
