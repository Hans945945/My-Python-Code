ans = input()
n = int(input())
r = ["*"] * len(ans)
print("".join(r))
for _ in range(n):
    guess = input()
    r = [char if char == guess or r[i] != "*" else "*" for i, char in enumerate(ans)]
    print("".join(r))
