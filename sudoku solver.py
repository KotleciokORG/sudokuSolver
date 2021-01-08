def show_sudoku(sudoku,height,width):
    for line in sudoku:
        print('|',end='')
        for char in line:
            print(char,'|',end='')
        print('')
        pass
    
def solve_sudoku(sudoku,width,height,S_width,S_height):
    
    border = max(height,width)
    possibilities = [i+1 for i in range(border)]
    def check_tile(x,y):
        element = sudoku[y][x]
        rectangle = []
        W2 = x//S_width*S_width
        H2 = y//S_height*S_height
        for i in range(H2,H2+S_height):
            rectangle+= sudoku[i][W2:W2+S_width]
        

        L = [0,0,0]
        #testing elements in rectangle
        for i in rectangle:
            if element == i:
                if L[0] >=1:
                    #print("Rectangle")
                    return False
                L[0]+=1
        #testing elements in row
        for i in sudoku[y]:
            if element == i:
                if L[1] >=1:
                    #print("Row")
                    return False
                L[1]+=1
        #testing elements in column
        for i in sudoku:
            if element == i[x]:
                if L[2] >=1:
                    #print("Column")
                    return False
                L[2]+=1
                

        return True
    
    def check_filed(sudoku):
        for line in sudoku:
            for el in line:
                if el==0:
                    return False
        return True

    def fill_tile(x,y):
        
        #print("{",y,'}',"{",x,'}',)
        if sudoku[y][x] != 0:
            x+=1
            if x >= width:
                x=0
                y+=1
                if y>=height:
                    return 0
            
            fill_tile(x,y)
        else:
            for i in possibilities:
                sudoku[y][x] = i


       #         show_sudoku(sudoku,width,height)
        #        print('')

                if check_tile(x,y):
                    if check_filed(sudoku):
                        print("Solution found!")
                        show_sudoku(sudoku,height,width)
                        
                    xSaved = x
                    ySaved = y
                    x+=1
                    if x >= width:
                        x=0
                        y+=1
                        if y>=height:
                            sudoku[-1][-1] = 0
                            return 0
                    fill_tile(x,y)
                    x = xSaved
                    y = ySaved

            sudoku[y][x] = 0

    fill_tile(0,0)
            
SUDOKU = [
    [0,1,0,5,0,0,3,0,0],
    [0,0,2,8,0,0,0,0,0],
    [0,0,3,0,0,0,1,9,0],
    [0,2,0,0,0,9,0,1,0],
    [6,4,0,0,0,0,0,5,0],
    [5,0,0,0,0,1,0,2,0],
    [0,0,0,0,7,0,0,0,6],
    [0,0,0,0,6,2,0,0,7],
    [0,9,0,0,0,0,0,0,0],
]

solve_sudoku(SUDOKU,9,9,3,3)
#show_sudoku(SUDOKU1,4,4)