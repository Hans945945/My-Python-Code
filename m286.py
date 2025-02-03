n,m = map(int, input().split())
if n % m == 0:
    print(f"整數 {n//m}")
elif n < m:
    print(f"真分數 {n}/{m}")
else:
    print(f"帶分數 {n//m} {n%m}/{m}")
