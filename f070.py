a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
a3, b3 = map(int, input().split())
m = 1
while m % a1 != b1 or m % a2 != b2 or m % a3 != b3:
    m += 1
print(m)
