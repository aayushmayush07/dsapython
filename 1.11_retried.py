sudoku = [
    [5, 0, 0, 0, 1, 0, 0, 0, 9],
    [0, 4, 0, 0, 0, 5, 8, 0, 0],
    [0, 7, 0, 0, 3, 4, 5, 2, 0],
    [2, 1, 0, 7, 6, 0, 0, 3, 0],
    [0, 4, 0, 9, 8, 2, 6, 1, 0],
    [0, 0, 0, 3, 2, 0, 0, 0, 4],
    [9, 0, 6, 7, 1, 0, 0, 0, 3],
    [8, 1, 0, 4, 0, 0, 2, 7, 0],
    [0, 0, 3, 0, 0, 0, 9, 8, 0],
]

class Sudoku:
    def __init__(self):
        i = 0
        while i < 9:
            j = 0
            while j < 9:
                if sudoku[i][j] == 0:
                 
                 
                    k = 1
                    while k < 10:
                        inRow = False
                        inColumn = False
                        inSquare = False                        
                        if k in sudoku[i]:
                            inRow = True
                            
                        if(inRow==False):
                            c = 0
                            while c < 9:
                                if k == sudoku[c][j]:
                                    inColumn = True
                                    break
                                c += 1

                            if inColumn == False:
                                sq_r_start = i - (i % 3)
                                sq_c_start = j - (j % 3)
                                sq_r = sq_r_start
                                while sq_r < sq_r_start + 3:
                                    sq_c = sq_c_start
                                    while sq_c < sq_c_start + 3:
                                        if k == sudoku[sq_r][sq_c]:
                                            inSquare = True
                                            break
                                        sq_c += 1
                                    sq_r += 1
                        k += 1

                    if inSquare == False and inRow == False and inColumn == False:
                        sudoku[i][j] = k
                        print(f"in {i+1} row {j+1} column  {k} is filled")
                        previous_index = [i, j]

                    elif k == 9:
                        if j == 0:
                            i -= 2
                            j = 8
                            sudoku[i][j] = 0
                        else:
                            j -= 2
                            sudoku[i][j] = 0
                
                        c += 1
                        
                j += 1
            i += 1









    def show_sudoku(self):
        for values in sudoku:
            print(values)

                                



sudoku_game=Sudoku()

sudoku_game.show_sudoku()