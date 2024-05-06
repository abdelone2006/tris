# abdelone_2006 tris         tiki-take-toe
import os
import random
import time
#++++++++++++control block row+++++++++++++++++++++++++++++++++++++
def check_to_block_row():
    for i in range(3):
        k=0
        free=0
        for j in range(3):
            if matrix[i][j]=='o':
                k=k+1
            elif matrix[i][j]!='x':
                free=int(matrix[i][j])
            if k==2 and free!=0:
                if control_digit('x',free):
                    return True 
    return False
#++++++++++++control block cloum+++++++++++++++++++++++++++++++++++++++
def check_to_block_column():
    for j in range(3):
        k=0 
        free=0
        for i in range(3):
            if matrix[i][j]=='o' :
                k=k+1
            elif matrix[i][j]!='x':
                free=int(matrix[i][j])
            if k==2 and free!=0: 
                if control_digit('x',free):
                    return True
    return False
#+++++++control block diagonal+++++++++++++++++++++++++++++++++++++
def check_to_block_diagonal():
    #diagonale principale
    j = 0
    k = 0
    for i in range(3):
        if matrix[i][i] == 'o':
            k += 1 #conta avversario       
        elif matrix[i][i] != 'x':
            j+=1 #conto libere
            free=i
            #free = int(matrix[i][j])
    if k == 2 and j==1:
        free=int(matrix[free][free])
        if control_digit('x', free):
            return True
    #diagonale principale
    k = 0
    j = 2
    n = 0
    free=0
    for i in range(3):
        if matrix[i][j] == 'o':
            k += 1
        elif matrix[i][j] != 'x':
            n = n+1
            pi=i
            pj=j
        j -= 1
            #free=matrix([i][j])
    if k == 2 and n == 1:
           free=int(matrix[pi][pj])
           if control_digit('x', free):
                return True
    return False
# ++++++++++++++++++++++print matrix++++++++++++++++++++++++++++++++++
def print_matrix():
    for row in matrix:
        print("-------------")
        print("|", end=" ")
        for element in row:
            print(element, end=" | ")
        print()
    print("----------")
#++++++++++++++++row controll++++++++++++++++++++++++++++++++++++++++++++++
def check_win_of_row(charter):
    for i in range(3):
        k=0
        for j in range(3):
            if matrix[i][j]==charter:
                k=k+1
        if k==3:
            return True 
    return False

#+++++++++++control cloumn win++++++++++++++++++++++++++++++++++++++++++
def check_win_of_column(charter):
    k=0
    for j in range(3):
        k=0 
        for i in range(3):
            if matrix[i][j]==charter:
                k=k+1
        if k==3:
            return True
    return False
#++++++++++++++++++diagonal control++++++++++++++++++++++++++++++++++++++++++
def check_win_of_diagonal(charter):
    j=0
    k=0
    for i in range(3):
        if(matrix[i][j]==charter):
            k=k+1 
            j=j+1                
    if k==3:
        return True 
    k=0
    j=2
    for i in range(3):
        if(matrix[i][j]==charter):
            k=k+1 
            j=j-1                
    if k==3:
        return True
    else: return False
#+++++++++++++switch for cases of input digit+++++++++++++++++++++++++
def control_digit(c, position):
    if position == 1 and matrix[0][0] == 1:
        matrix[0][0] = c
        return True
    elif position == 2 and matrix[0][1] == 2:
        matrix[0][1] = c
        return True
    elif position == 3 and matrix[0][2] == 3:
        matrix[0][2] = c
        return True
    elif position == 4 and matrix[1][0] == 4:
        matrix[1][0] = c
        return True
    elif position == 5 and matrix[1][1] == 5:
        matrix[1][1] = c
        return True
    elif position == 6 and matrix[1][2] == 6:
        matrix[1][2] = c
        return True
    elif position == 7 and matrix[2][0] == 7:
        matrix[2][0] = c
        return True
    elif position == 8 and matrix[2][1] == 8:
        matrix[2][1] = c
        return True
    elif position == 9 and matrix[2][2] == 9:
        matrix[2][2] = c
        return True
    else:
        return False


#+++++++++++++++++++++++++++matrix creation++++++++++++++++++++++++++++++++++++++++++++
matrix=[
    [1,2,3]
    ,[4,5,6]
    ,[7,8,9]
]


#++++++++++++++++++++++++++++assign digit++++++++++++++++++++++++++++++++++++++++++++++
p = True
while p:
    os.system("clear")
    print("                                                             start                                           ")
    print("                                              welcome to tiki taka toe game! :)")
    print("SELECT MODE: ")
    print("1->player1 vs played 2")
    print("2->player vs pc")
    select=int(input("ENTER MODE:"))
#+++++++++++++++++1 vs 1 +++++++++++++++++++++++++++++++++++++++++++++
    if select==1:
        os.system("clear")
        l=input("enter player1 name:")
        l1=input("enter player2 name:")

        check=True
        i=0
        for i in range (9):
            os.system("clear")
            print_matrix()
            if i%2==0: #usa Oelse: #usa X
                carattere='o'
                name=l
            else: #usa 
                carattere='x'
                name=l1
            print("it's turn of:",name)
            position=int((input("insert 'o' in the position that you want:")))
            control_digit(carattere,position)
            while not control_digit(carattere,position):
                os.system("clear")
                print("not valid number or cell is ocupate")
                print_matrix()
                position=int((input("insert 'o' in the position that you want:")))
                if control_digit(carattere,position):
                    break  
            if check_win_of_row(carattere) or check_win_of_column(carattere) or check_to_block_diagonal(carattere):
                os.system("clear")
                print_matrix()
                print(name,"win,you are the bosssss ")
                break
            elif i==9:
                os.system("clear")
                print_matrix()
                print("draw, you are very stupid")
                break  





#+++++++++++++++++++++++++++++computer vs player++++++++++++++++++++++++++++++++
    elif select==2:
        os.system("clear")
        l=input("enter your name:")
        i=0
        for i in range (9):
            os.system("clear")
            print_matrix()
            if i%2==0: #usa O
                print("it's your",i,"turn")
                position=int((input("insert the number of the cell that you want to put 'O'")))
                check=control_digit('o',position)
                while not check:
                    os.system("clear")
                    print("not valid number or cell is ocupate")
                    print_matrix()
                    position=int((input("insert 'O' in the position that you want:")))
                    if control_digit('o',position):
                        break
            else:  # Computer's turn
                if not check_to_block_row():
                    if not check_to_block_column():
                        if not check_to_block_diagonal():
                            position = random.randint(1, 9)
                            control_digit('x', position)                    
            if check_win_of_row('x') or check_win_of_column('x') or check_win_of_diagonal('x'):
                os.system("clear")
                print_matrix()
                print("Computer wins")
                break
            elif check_win_of_row('o') or check_win_of_column('o') or check_win_of_diagonal('o'):
                os.system("clear")
                print_matrix()
                print(l, "wins, you are the boss!")
                break
            elif i == 8:
                os.system("clear")
                print_matrix()
                print("It's a draw")
                break
          
    else:
            print("no valid number:")
            p=True
    break
print("the end,thank you for try this game,byee")
print("see you next time")
