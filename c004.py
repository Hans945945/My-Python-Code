T = int(input())
for _ in range(T):
    s,d = map(int, input().split())
    a = (s+d)/2
    b = (s-d)/2
    if a < 0 or b < 0 or int(a) != a or int(b) != b:
        print("impossible")
    else:
        print(int(a),int(b))
