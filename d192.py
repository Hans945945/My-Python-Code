T = int(input())
for case in range(1, T + 1):
    n, k = map(int, input().split())
    pos = 0
    for i in range(2, n + 1):
        pos = (pos + k) % i
    print(f"Case {case}: {pos + 1}")
