import copy
R,C,k,m = map(int, input().split())
cities = [[-1]*(C+2)]+ [[-1] + list(map(int, input().split()))+ [-1] for _ in range(R)]+ [[-1]*(C+2)]
for _ in range(m):
    r = copy.deepcopy(cities)
    for i in range(1,R+1):
        for j in range(1,C+1):
            if cities[i][j] != -1:
                if cities[i][j+1] != -1:
                    r[i][j] -= cities[i][j] // k
                    r[i][j+1] += cities[i][j] // k
                if cities[i][j-1] != -1:
                    r[i][j] -= cities[i][j] // k
                    r[i][j-1] += cities[i][j] // k
                if cities[i+1][j] != -1:
                    r[i][j] -= cities[i][j] // k
                    r[i+1][j] += cities[i][j] // k
                if cities[i-1][j] != -1:
                    r[i][j] -= cities[i][j] // k
                    r[i-1][j] += cities[i][j] // k
    cities = r
    
minv = float('inf')
maxv= float('-inf')
for i in range(1, R+1):
    for j in range(1, C+1):
        if cities[i][j]!= -1:
            minv = min(minv, cities[i][j])
            maxv = max(maxv, cities[i][j])
print(minv)
print(maxv)
