import sys
data = sys.stdin.read().splitlines()
index = 0
results = []

while index < len(data):
    P = data[index].strip().split()
    index += 1
    n = int(data[index])
    index += 1

    for _ in range(n):
        A, B = 0, 0
        ans = data[index].strip().split()
        index += 1

        unmatched_P = []
        unmatched_ans = []
        
        for p, a in zip(P, ans):
            if p == a:
                A += 1
            else:
                unmatched_P.append(p)
                unmatched_ans.append(a)

        for p in unmatched_P:
            if p in unmatched_ans:
                B += 1
                unmatched_ans.remove(p)

        results.append(f"{A}A{B}B")

sys.stdout.write("\n".join(results) + "\n")

