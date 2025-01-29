n = int(input())
rocks = list(map(int, input().split()))
avg = sum(rocks)//n
biggest = max(rocks)
rocks[rocks.index(biggest)] = avg
rocks[rocks.index(min(rocks))] += biggest - avg
print(" ".join(map(str, rocks)))
