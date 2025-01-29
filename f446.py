T = input()
if T == "":
    T = input()
for _ in range(int(T)):
    cars = []
    d = int(input())
    for _ in range(d):
        name, low, high = input().split()
        cars.append((name, int(low), int(high)))
    q = int(input())
    for _ in range(q):
        qualify = None
        price = int(input())
        for name, low, high in cars:
            if low <= price <= high:
                if qualify is None:
                    qualify = name
                else:
                    qualify = "UNDETERMINED"
                    break
        print(qualify if qualify else "UNDETERMINED")
