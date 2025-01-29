L1 = [ 10, 11, 12, 13, 14, 15, 16,
          17, 34, 18, 19, 20, 21, 22,
          35, 23, 24, 25, 26, 27, 28,
          29, 32, 30, 31, 33 ]
L2 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
n = list(input())
n = list(map(int,n))
ln = n.pop()
r = ""
total = 0

for i in range(len(n)):
    n[i] = n[i]*(8-i)
for j in range(len(L1)):
    total = sum(n)+(L1[j] % 10)*9+(L1[j] // 10)
    if ((10 - (total % 10)) %10) == ln:
        r = r+L2[j]
print(r)
