T = int(input())
for x in range(T):
    print(f"Case {x+1}:", sorted(map(int, input().split()))[1])
