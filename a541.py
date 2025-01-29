n = int(input())
words = set()
for _ in range(n):
    words.add(input().strip())
n = int(input())
for _ in range(n):
    w = input().strip()
    if w in words:
        print("yes")
    else:
        print("no")
        words.add(w)
