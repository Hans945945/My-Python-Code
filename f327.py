a,b = input().split()
c = 0
for w in a:
    c = c*26 + ord(w)-65+1
d = 0
for w in b:
    d = d*26 + ord(w)-65+1
print(abs(c-d)+1)
