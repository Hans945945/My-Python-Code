T = int(input())
for _ in range(T):
    data = list(map(int, input().split()))
    data.sort()
    if data[0] == data[3]:
        print("square")
    elif data[0] == data[1] and data[2] == data[3]:
        print("rectangle")
    elif sum(data[0:3]) > data[3]:
        print("quadrangle")
    else:
        print("banana")
