n = int(input())
slogan = {}
for _ in range(n):
    c = input().rstrip()
    r = input().rstrip()
    slogan[c] = r
q = int(input())
for _ in range(q):
    c = input().rstrip()
    print(slogan[c])
