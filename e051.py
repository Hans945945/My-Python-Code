q = input()
r = q[0]
for i in range(len(q)-2):
    r+="_"
r+=q[-1]
print(r)
