# SUDOKU SOLVER
from itertools import count

# gets the puzzle from .txt
# TO CHANGE THE .TXT CHANGE THE NAME: 'sudoku,txt' in function sudoku_from_txt()
def sudoku_from_txt():
    f = open('sudoku.txt', 'r')
    sudoku = f.read()
    # making a list of numbers from imported file
    test_sudoku = []
    for el in sudoku:
        if el == "0" or el == "1" or el == "2" or el == "3" or el == "4" or el == "5" or el == "6" or el == "7" or el == "8" or el == "9":
            test_sudoku.append(int(el))
        else:
            pass

    ready_to_solve = []
    list1=[]
    # 9 lists in array
    i,m=0,0
    while m <9: 
        while i < 9:
            list1.append(test_sudoku.pop(0))
            i+=1
        ready_to_solve.append(list1)
        list1=[]
        m+=1
        i=0
    if dont_sabogate(ready_to_solve):
        return ready_to_solve
    else:
        print("It would have worked if you didn't try to sabotage my beautiful program :)")
        return False

# if you try to sabotage the solver, it will call you out <3
def dont_sabogate(puzzle):
    result_row = 0
    # for row
    for list in puzzle:
        for el in list:
            if el != 0:
                result_row = list.count(el)
                if result_row >= 2:
                    return False
                else:
                    result_row = 0
    
    
    # for column --> add numbers of columns where a given digit is to a list and check if there are any duplicates in this list, repeat for every number
    all_num = []
    for el in range(1,10):
        for row in range(9):
            for col in range(9):
                if el == puzzle[row][col]:
                    all_num.append(col)
                    if len(all_num) != len(set(all_num)):
                        return False
        all_num=[]

    # # in a 3x3 square, 9 squares
    square1 = []
    for c in range(0,3):
        for r in range(0,3):
            if puzzle[r][c] != 0:
                square1.append(puzzle[r][c])
                if len(square1) != len(set(square1)):
                    return False

    square2=[]
    for c in range(3,6):
        for r in range(0,3):
            if puzzle[r][c] != 0:
                square2.append(puzzle[r][c])
                if len(square2) != len(set(square2)):
                    return False   

    square3=[]     
    for c in range(6,9):
        for r in range(0,3):
            if puzzle[r][c] != 0:
                square3.append(puzzle[r][c])
                if len(square3) != len(set(square3)):
                    return False

    square4 = []
    for c in range(0,3):
        for r in range(3,6):
            if puzzle[r][c] != 0:
                square4.append(puzzle[r][c])
                if len(square4) != len(set(square4)):
                    return False
    
    square5 = []
    for c in range(3,6):
        for r in range(3,6):
            if puzzle[r][c] != 0:
                square5.append(puzzle[r][c])
                if len(square5) != len(set(square5)):
                    return False
    
    square6 = []
    for c in range(6,9):
        for r in range(3,6):
            if puzzle[r][c] != 0:
                square6.append(puzzle[r][c])
                if len(square6) != len(set(square6)):
                    return False

    square7 = []
    for c in range(0,3):
        for r in range(6,9):
            if puzzle[r][c] != 0:
                square7.append(puzzle[r][c])
                if len(square7) != len(set(square7)):
                    return False

    square8 = []
    for c in range(3,6):
        for r in range(6,9):
            if puzzle[r][c] != 0:
                square8.append(puzzle[r][c])
                if len(square8) != len(set(square8)):
                    return False

    square9 = []
    for c in range(6,9):
        for r in range(6,9):
            if puzzle[r][c] != 0:
                square9.append(puzzle[r][c])
                if len(square9) != len(set(square9)):
                    return False

    return True
          
# finds an empty space in sudoku
def find_next_empty(puzzle):
    # finds the next row, col on puzzle that's not filled yet --> we represent these with 0
    for row in range(9):
        for column in range(9):
            if puzzle[row][column] == 0:
                return row, column
    return None, None # if no spaces in the puzzle are empty (0)

# guesses a number in one empty spot, according to sudoku rules
def is_guess_valid(puzzle, guess, row, column):
    # did that number appear in a row?
    if guess in puzzle[row]: 
        return False

    # did that number appear in a column?
    some_column = [puzzle[i][column] for i in range(9)]
    if guess in some_column:
        return False
    
    # did that number appear in a 3x3 square?
    
    row_start = (row//3)*3          # for 0,1,2 = 0 || 3,4,5 = 1 || 6,7,8, = 2
    column_start = (column//3)*3    # for 0,1,2 = 0 || 3,4,5 = 1 || 6,7,8, = 2

    for r in range(row_start, row_start + 3):
        for c in range(column_start, column_start + 3):
            if guess == puzzle[r][c]:
                return False

    return True

# fills spaces with valid guesses, one by one, bactracking method
def solve_sudoku(puzzle):
    if puzzle == False:
        return
    row, column = find_next_empty(puzzle)

    if row is None:
        return True
    
    for guess in range(1,10):
        if is_guess_valid(puzzle, guess, row, column):
            puzzle[row][column] = guess
            if solve_sudoku(puzzle):
                file = open('final_puzzle.txt', 'w')
                file.write(str(puzzle))
                file.close()
                return puzzle
        puzzle[row][column] = 0
    return False

# makes the solution more readable
def make_nicer_puzzle(file):
    if sudoku_from_txt() == False:
        return False
    file = open('final_puzzle.txt', 'r')
    final_suddoku_str = file.read()
    final_suddoku_list = []
    final_suddoku_str1 = ""

    for el in final_suddoku_str:
        if el == "0" or el == "1" or el == "2" or el == "3" or el == "4" or el == "5" or el == "6" or el == "7" or el == "8" or el == "9":
            final_suddoku_list.append(int(el))
        else:
            pass
    
    
    # every 9 elements in the list do enter
    i,m,n,o=0,0,0,0
    final_suddoku_str1 = "==============================\n ||"
    for el in final_suddoku_list:
        final_suddoku_str1 += " " + str(el)
        i+=1
        m+=1
        n+=1
        o+=1
        if i==9:
            final_suddoku_str1 += " ||\n"
            i=0
        if n==27:
            final_suddoku_str1 += "==============================\n"
            n=0
        if o==81:
            break              
        if m==3:
            final_suddoku_str1 += " ||"
            m=0
    file = open('final_puzzle.txt', 'w')
    file.write(final_suddoku_str1)
    file.close()
    
    return final_suddoku_str1

print(make_nicer_puzzle(solve_sudoku(sudoku_from_txt())))
