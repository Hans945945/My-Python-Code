h,m,s,t = map(int, input().split())
h+=36
m+=90*t+60*h
h = m//60%36
m %= 60
print(f"{h}:{str(m).zfill(2)}:{str(s).zfill(2)}")
