def solve(row, current, cols, diag1, diag2, solutions):
    if row == 9:
        solutions.append(current.copy())
        return
    for col in range(1, 9):
        if col in cols or (row - col) in diag1 or (row + col) in diag2:
            continue
        current.append(col)
        cols.add(col)
        diag1.add(row - col)
        diag2.add(row + col)
        solve(row + 1, current, cols, diag1, diag2, solutions)
        current.pop()
        cols.remove(col)
        diag1.remove(row - col)
        diag2.remove(row + col)

solutions = []
solve(1, [], set(), set(), set(), solutions)

t = int(input())
for case in range(t):
    if case > 0:
        print()
    c,r = map(int, input().split())
    valid = [sol for sol in solutions if sol[r - 1] == c]
    valid.sort()
    print("SOLN       COLUMN")
    print(" #      1 2 3 4 5 6 7 8")
    for idx, sol in enumerate(valid, 1):
        print(f"{idx:2}      ", end="")
        print(" ".join(str(x) for x in sol))
