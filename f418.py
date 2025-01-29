import sys
h, w, r1, c1, r2, c2 = map(int, input().split())
words = []
for s in sys.stdin:
    words.append(list(s))

if r1 == r2:
    print("".join(words[r1-1][c1-1:c2]))
elif c1 == c2:
    words = list(zip(*words))
    print("".join(words[c1-1][r1-1:r2]))
else:
    r = ""
    for i in range(r2-r1+1):
        r += words[r1-1+i][c1-1+i]
    print(r)
