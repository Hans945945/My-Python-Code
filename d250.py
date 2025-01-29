sudoku = []
for _ in range(9):
    temp = list(map(int, list(input())))
    sudoku.append(temp)
for i in range(9):
    print(45-sum([sudoku[i][j] for j in range(9)]))
    
