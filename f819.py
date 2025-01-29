import sys
data = sys.stdin.read().splitlines()
books = []
total = 0
for s in data[1:]:
    n, d = map(int, s.split())
    if d >100:
        books.append(n)
        total += (d-100)*5
if books:
    print(" ".join(map(str, sorted(books))))
print(total)
    
