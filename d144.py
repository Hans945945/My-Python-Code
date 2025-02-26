now = 1
ans = 1
for i in range(1,101):
    now *= i
    ans *= now
print("\n".join(list(str(ans))))
