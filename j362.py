n = int(input())
status = (input()=="print")
r = []
for i in range(2, int(n**0.5)+1):
    if n % i == 0:
        r.append(i)
        if i*i != n:
            r.append(n//i)
if status:
    r.append(1)
    r.append(n)
r.sort()
print("\n".join(map(str, r)))
print(f"{n}的因數的個數是{len(r)}，{n}的因數的總和是{sum(r)}")
