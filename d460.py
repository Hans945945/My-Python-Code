n = int(input())
r = (n<=11 and n>=6)*590 + (n >= 12 and n <= 17)*790 + (n >= 18 and n <= 59)*890 + (n >= 60)*399
print(r)
