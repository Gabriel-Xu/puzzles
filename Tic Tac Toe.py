def display(board):
    print()
    print("Current board:")
    for i in range(3):
        print(board[3*i:3*i+3])
    print()

def game_over(board):
    for i in range(3):
        if board[3*i]==board[3*i+1] and board[3*i]==board[3*i+2] and board[3*i]!=".":
            return True
        if board[i]==board[i+3] and board[i]==board[i+6] and board[i]!=".":
            return True
    if board[0]==board[4] and board[0]==board[8] and board[0]!=".":
        return True
    if board[2]==board[4] and board[2]==board[6] and board[2]!=".":
        return True
    for x in board:
        if x==".":
            return False
    return True

def score(board):
    for i in range(3):
        if board[3*i]==board[3*i+1] and board[3*i]==board[3*i+2] and board[3*i]!=".":
            if board[3*i]=="X":
                return 1
            else:
                return -1
        if board[i]==board[i+3] and board[i]==board[i+6] and board[i]!=".":
            if board[i]=="X":
                return 1
            else:
                return -1
    if (board[0]==board[4] and board[0]==board[8] or board[2]==board[4] and board[2]==board[6]) and board[4]!=".":
        if board[4]=="X":
            return 1
        else:
            return -1
    return 0

def next_boards(board):
    if board.count("X")==board.count("O"):
        player="X"
    else:
        player="O"
    boards=[]
    for i, x in enumerate(board):
        if x==".":
            boards.append((i, board[:i]+player+board[i+1:]))
    return boards

def max_step(board):
    if game_over(board):
        return score(board)
    return max([min_step(new_board[1]) for new_board in next_boards(board)])

def min_step(board):
    if game_over(board):
        return score(board)
    return min([max_step(new_board[1]) for new_board in next_boards(board)])

def max_move(board):
    new_boards=next_boards(board)
    bestv=-2
    for i, x in enumerate(new_boards):
        print("Moving at "+str(x[0])+" results in a ", end="")
        res=min_step(x[1])
        if res==1:
            print("win.")
        elif res==-1:
            print("loss.")
        else:
            print("tie.")
        if res>bestv:
            ans=i
            bestv=res
    print()
    print("I choose space "+str(new_boards[ans][0])+".")
    return new_boards[ans][1]

def min_move(board):
    new_boards=next_boards(board)
    bestv=2
    for i, x in enumerate(new_boards):
        print("Moving at "+str(x[0])+" results in a ", end="")
        res=max_step(x[1])
        if res==-1:
            print("win.")
        elif res==1:
            print("loss.")
        else:
            print("tie.")
        if res<bestv:
            ans=i
            bestv=res
    print()
    print("I choose space "+str(new_boards[ans][0])+".")
    return new_boards[ans][1]

board=input().strip()
if board.count(".")==9:
    inpt=input("Should I be X or O? ").strip()
    if inpt=="X":
        ai_is_x=True
    elif inpt=="O":
        ai_is_x=False
    else:
        print("Invalid Input!")
    cur_player="X"
else:
    ai_is_x=board.count("X")==board.count("O")
    if ai_is_x:
        cur_player="X"
    else:
        cur_player="O"
display(board)
while not game_over(board):
    if ai_is_x and cur_player=="X":
        board=max_move(board)
    elif not ai_is_x and cur_player=="O":
        board=min_move(board)
    else:
        possible=[]
        for i, x in enumerate(board):
            if x==".":
                possible.append(str(i))
        print("You can move to any of these spaces: "+", ".join(possible)+".")
        choice=int(input("Your choice? ").strip())
        board=board[:choice]+cur_player+board[choice+1:]
    display(board)
    if cur_player=="X":
        cur_player="O"
    else:
        cur_player="X"
if score(board)==1:
    if ai_is_x:
        print("I win!")
    else:
        print("You win!")
elif score(board)==-1:
    if ai_is_x:
        print("You win!")
    else:
        print("I win!")
else:
    print("We tied!")