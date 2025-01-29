words = list(input())
n = []

for i in range(1,len(words)):
    d = str(abs(ord(words[i])-ord(words[i-1])))
    n.append(d)
r = "".join(n)
print(r)
