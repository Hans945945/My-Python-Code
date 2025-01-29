N = int(input())
for _ in range(N):
    sides = list(map(int, input().split()))
    sides.sort()
    print("OK" if sides[0] + sides[1] > sides[2] else "Wrong!!")
