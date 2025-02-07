T = int(input())
for _ in range(T):
    a,o,b = input().split()
    print(int(a)**int(b) if o == "**" else int(a)*int(b))
