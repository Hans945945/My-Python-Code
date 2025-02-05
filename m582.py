import sys
n, m = map(int, sys.stdin.readline().split())
bookshelfs = list(map(int, sys.stdin.readline().split()))
book_positions = {book: idx + 1 for idx, book in enumerate(bookshelfs)}
r = [book_positions[i] for i in range(1, m + 1)]
sys.stdout.write(" ".join(map(str, r)) + "\n")
