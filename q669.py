N = int(input())
score = int(input())
others = [int(input()) for _ in range(N - 1)]

scores = others + [score]
scores.sort(reverse=True)

higher = sum(1 for s in scores if s > score)
equal = sum(1 for s in scores if s == score)

if higher < 5 and higher + equal <= 5:
    print("Top 5")
elif higher < 5:
    print("Maybe Top 5")
elif higher < 10:
    print("Top 10")
else:
    print("Thank You")
