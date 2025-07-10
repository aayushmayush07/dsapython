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
squares=[[[0,3],[2,5]],
         
         
         ]

class Sudoku:
    def __init__(self):
        self.choices=[1,2,3,4,5,6,7,8,9]
        previous_index=[-1,-1]

        for i in range (0,9):
            for j in range(0,9):
                if (sudoku[i][j]==0):
                    
                    for k in range(1,10):
                        inSquare=True
                        inRow=True
                        inColumn=True
                        if(k!=sudoku[previous_index[0]][previous_index[1]]):
                            

                            if(k not in sudoku[i] ):  #not in that particular row
                                inRow=False
                              
                                for c in range(0,9):
                                    if(k == sudoku[c][j]):  #in that column
                                        inColumn=True
                                        if(k==9):
                                            
                                            if(j==0):
                                                i-=1
                                                j=8
                                                sudoku[i][j]=0
                                            else:
                                                j-=1  
                                                sudoku[i][j]=0                                        
                                        break

                                    else:
                                        inColumn=False
                                if(inColumn==False):  #not in that column
                                    sq_r_start=i-(i%3) 
                                    sq_c_start=j-(j%3)
                                   
                                    for sq_r in range (sq_r_start,sq_r_start+3):
                                        
                                        for sq_c in range(sq_c_start,sq_c_start+3):
                                            if(k  ==sudoku[sq_r][sq_c]):    #in the square
                                                inSquare=True


                                                if(k==9):
                                                    
                                                    if(j==0):
                                                        i-=1
                                                        j=8
                                                        sudoku[i][j]=0
                                                    else:
                                                        j-=1  
                                                        sudoku[i][j]=0  

                                                break
                                            else:
                                                inSquare=False
                            if(inSquare==False and inRow==False and inColumn==False):
                                sudoku[i][j]=k
                                print(f"in {i+1} row {j+1} column  {k} is filled")
                                previous_index=[i,j]   #not even in the square
                                break
                            elif(k==9):
                                
                                if(j==0):
                                    i-=1
                                    j=8
                                    sudoku[i][j]=0
                                else:
                                    j-=1   
                                    sudoku[i][j]=0                                       

    
    def show_sudoku(self):
        for values in sudoku:
            print(values)

                                



sudoku_game=Sudoku()

sudoku_game.show_sudoku()
