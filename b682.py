H1,M1 = map(int, input().split())
H2,M2 = map(int, input().split())
if H1>H2:
    H2 = H2+24
elif H1 == H2 and M1> M2:
    H2 += 24
r = (H2*60+M2) - (H1*60+M1)
H = r//60
M = r%60
print(H,M)
