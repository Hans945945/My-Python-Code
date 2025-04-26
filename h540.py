import sys
r = []
for s in sys.stdin.readlines()[1:]:
    C,R = map(int, s.split())
    ans = R*2-1 if R <= C else R+C
    r.append(f"{ans if ans > 0 else '٩(ˊᗜˋ*)و'}")
sys.stdout.write("\n".join(r)+"\n")
