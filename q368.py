m,n = map(int, input().split())
print(n+1 if m==0 else n+2 if m==1 else 2*n+3 if m==2 else 2 ** (n + 3) - 3)
