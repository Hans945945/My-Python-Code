def factors(n):
    total = [1]
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            total.append(i)
            if i != n // i:
                 total.append(n//i)
    return sorted(total)
n = int(input())
f1 = factors(n)
s1 = sum(f1)
print(f'{"+".join(map(str, f1))}={s1}')
if s1 == n:
    print(n, "is perfect.")
elif s1 == 1:
    print("=0")
    print(f"{n} has no friends.")
else:
    f2 = factors(s1)
    s2 = sum(f2)
    print(f'{"+".join(map(str, f2))}={s2}')
    print(f"{n} has no friends." if s2 != n else f"{n} and {s1} are friends.")
    
    

        
