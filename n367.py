a,b,c = map(int, input().split())
x = a+c-b
y = a+b-c
z = b+c-a
t = x*y + y*z + z*x
print(f"{x/2:.4f}\n{y/2:.4f}\n{z/2:.4f}\n{t**0.5/4:.4f}" if t>0 else "error")
