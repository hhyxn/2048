import random
def printBoard(board):
    # ANSI escape sequences for colors
    WHITE_BG_AND_TEXT = "\033[97;107m"
    BGOFFWHITE = "\033[48;5;253m"
    BGRED = "\u001b[41;1m"
    BGBEIGE = "\033[48;5;230m"
    BGLIGHTORANGE = "\033[48;5;215m"
    BGMEDIUMORANGE = "\033[48;5;208m"
    BGCORAL="\033[48;5;203m"
    LIGHTYELLOWBG = "\033[48;5;229m"
    SOFT_YELLOW_BG = "\033[48;5;227m"
    YELLOW_BG = "\033[48;5;226m"
    DARK_YELLOW_BG = "\033[48;5;214m"
    DEEP_YELLOW_BG = "\033[48;5;208m"
    GREY = "\033[38;5;240m"
    WHITE= "\033[38;5;15m"
    RESET = "\033[0m"
    for i in range(len(board)):
        for j in range(len(board [i])):
            if(board[i][j]==2):
                print(BGOFFWHITE+GREY +str(board[i][j])+ RESET ,sep=' ',end="     ")
            elif(board[i][j]==4):
                print(BGBEIGE+GREY +str(board[i][j])+ RESET ,sep=' ',end="     ")
            elif(board[i][j]==8):
                print(BGLIGHTORANGE+WHITE +str(board[i][j])+ RESET ,sep=' ',end="     ")
            elif(board[i][j]==16):
                print(BGMEDIUMORANGE +WHITE+str(board[i][j])+ RESET ,sep=' ',end="     ")
            elif(board[i][j]==32):
                print(BGCORAL +WHITE+str(board[i][j])+ RESET ,sep=' ',end="     ")
            elif(board[i][j]==64):
                print(BGRED+WHITE+str(board[i][j])+ RESET ,sep=' ',end="     ")
            elif(board[i][j]==128):
                print(LIGHTYELLOWBG +WHITE+str(board[i][j])+ RESET ,sep=' ',end="     ")
            elif(board[i][j]==256):
                print(SOFT_YELLOW_BG+WHITE +str(board[i][j])+ RESET ,sep=' ',end="     ")
            elif(board[i][j]==512):
                print(YELLOW_BG +WHITE+str(board[i][j])+ RESET ,sep=' ',end="     ")
            elif(board[i][j]==1024):
                print(DARK_YELLOW_BG +WHITE+str(board[i][j])+ RESET ,sep=' ',end="     ")
            elif(board[i][j]==2048):
                print(DEEP_YELLOW_BG+WHITE +str(board[i][j])+ RESET ,sep=' ',end="     ")
            elif(board[i][j]==0):
                print(WHITE_BG_AND_TEXT+str(board[i][j])+ RESET ,sep=' ',end="     ")
        print("")
        print("")
    print(f"Score: {score}")

def startGame(board):
    i = 0
    while i<2:
        row=random.randint(0,3)
        col =random.randint(0,3)
        num = random.choice([2,2,2,2,2,2,2,2,2,4])
        if board[row][col] == 0:
            board [row][col]=num
            i+=1
    global score
    score = 0
    # printing controls for user
    print("Commands are as follows : ")
    print("w : Move Up")
    print("s : Move Down")
    print("a : Move Left")
    print("d : Move Right")

def gameOver(board):
    #check if 2048 is reached
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==2048:
                return True
    return False
def shiftVertical(board,j,way):
    col = [0,0,0,0]
    colInd = 0
    if(way=='u'):
        for i in range(4):
            if board[i][j]!=0:
                col[colInd] = board[i][j]
                colInd+=1
        #shift all elements to the most up spot
        for i in range(4):
            board[i][j]=col[i]
    elif(way=='d'):
        i = 3
        while i>=0:
            if board[i][j]!=0:
                col[colInd]=board[i][j]
                colInd+=1
            i-=1
        #shift all elements down
        col.reverse()
        for i in range(4):
            board[i][j]=col[i]

def shiftHorizontal(board,i,way):
    row = [0,0,0,0]
    rowInd=0
    if way == 'r':
        for j in range(4):
            if board[i][j]!=0:
                row[rowInd]=board[i][j]
                rowInd+=1
        #shift all elements to the right
        for j in range(4):
            board[i][j]=row[j]
    elif way =='l':
        j = 3
        while j>=0:
            if board[i][j]!=0:
                row[rowInd]=board[i][j]
                rowInd+=1
            j-=1
        #shift all elements to the left
        row.reverse()
        for col in range(4):
            board[i][col]=row[col]
            
def moves(board,move):
    global score
    #move up w
    if move == 'w':
        for j in range(4):
            shiftVertical(board,j,'u')
            #merge
            for i in range(3):
                if board[i][j]==board[i+1][j]:
                    board[i][j]*=2
                    score += board[i][j]
                    board[i+1][j]=0
            shiftVertical(board,j,'u')        
    #move down
    elif move == 's':
        for j in range(4):
            shiftVertical(board,j,'d')
            #merge
            i = 3
            while i>0:
                if board[i][j]==board[i-1][j]:
                    board[i][j]*=2
                    score += board[i][j]
                    board[i-1][j]=0 
                i-=1
            shiftVertical(board,j,'d')
    #move left
    elif move == 'd':
        for i in range(4):
            shiftHorizontal(board,i,'l')
            #merge
            j = 3
            while j > 0:
                if board[i][j]==board[i][j-1]:
                    board[i][j]*=2
                    score += board[i][j]
                    board[i][j-1]=0
                j-=1
            shiftHorizontal(board,i,'l')
    #move right
    elif move == 'a':
        for i in range(len(board)):
            shiftHorizontal(board,i,'r')
            #merge
            j = 0
            while j < 3 :
                if board[i][j]==board[i][j+1]:
                    board[i][j]*=2
                    score+=board[i][j]
                    board[i][j+1]=0
                j+=1
            shiftHorizontal(board,i,'r')

def generateTile(board):
    row=random.randint(0,3)
    col =random.randint(0,3)
    num = random.choice([2,2,2,2,2,2,2,2,2,4])
    #check if full
    fulled = True
    for i in range(4):
        for j in range(4):
            if board[i][j]!=0:
                fulled = False
    #regenerate if spot is filled
    if fulled == False:
        while(board[row][col]!= 0):
            row=random.randint(0,3)
            col =random.randint(0,3)
        board[row][col]=num
        return True
    else:
        return False
board = [[0] * 4 for _ in range(4)]
startGame(board)
printBoard(board)
move=input("Move: ")
while move!='a' and move !='s' and move !='d' and move != 'w':
    print("Invalid Move. Please enter w s a d for the corresponding moves.")
    move=input("Move: ")
moves(board, move)
while (generateTile(board) == True and gameOver(board) == False):
    printBoard(board)
    move=input("Move: ")
    while move!='a' and move !='s' and move !='d' and move != 'w':
        print("Invalid Move. Please enter w s a d for the corresponding moves.")
        move=input("Move: ")
    moves(board, move)
printBoard(board)
print("Game Over!")
if (gameOver(board)==True):
    print("You win!")
else:
    print("Try Again :(")