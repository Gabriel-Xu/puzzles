import math
from time import perf_counter

def display(board):
    for i in range(n):
        for j in range(n):
            print(board[i*n+j], end=" ")
        print()
    print()

def get_next(board):
    minv=n+1
    for i, x in enumerate(board):
        if len(x)<minv and len(x)>1:
            minv=len(x)
            mini=i
    return mini

def goal_test(board):
    for x in board:
        if len(x)>1:
            return False
    return True

def forward(board):
    q=[]
    for i, x in enumerate(board):
        if len(x)==1:
            q.append(i)
    while len(q)>0:
        cur=q.pop()
        for i in neighbors[cur]:
            if len(board[i])==1:
                if board[i]==board[cur]:
                    return None
            else:
                new=""
                for char in board[i]:
                    if char!=board[cur]:
                        new+=char
                board[i]=new
                if len(board[i])==1:
                    q.append(i)
    return board

def propagate_helper(board, con):
    for row in con:
        for char in symbols:
            count=0
            for x in row:
                if char in board[x]:
                    count+=1
                    i=x
            if count==0:
                return False
            elif count==1:
                board[i]=char
    return True

def propagate(board):
    if not propagate_helper(board, row_con):
        return None
    if not propagate_helper(board, col_con):
        return None
    if not propagate_helper(board, block_con):
        return None
    return forward(board)

def backtracking(board):
    if goal_test(board):
        return board
    var=get_next(board)
    for val in board[var]:
        new_board=[x for x in board]
        new_board[var]=val
        checked_board=propagate(new_board)
        if checked_board!=None:
            result=backtracking(checked_board)
            if result!=None:
                return result

with open("Sudoku Files/"+input().strip()) as f:
    puzzles=[line.strip() for line in f]

start=perf_counter()
for puzzle in puzzles:
    n=int(len(puzzle)**.5)
    sub_height=math.floor(n**.5)
    while n%sub_height!=0:
        sub_height-=1
    sub_width=math.ceil(n**.5)
    while n%sub_width!=0:
        sub_width+=1
    alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbols=[str(i) if i<10 else alpha[i-10] for i in range(1, n+1)]
    row_con=[[i*n+j for j in range(n)] for i in range(n)]
    col_con=[[i*n+j for i in range(n)] for j in range(n)]
    block_con=[]
    for i in range(n//sub_height):
        for j in range(n//sub_width):
            block_con.append([i1*n+j1 for i1 in range(i*sub_height, (i+1)*sub_height) for j1 in range(j*sub_width, (j+1)*sub_width)])
    neighbors=[set() for i in range(n*n)]
    for i in range(n):
        for j in range(n):
            a=i*n+j
            for v in row_con[i]:
                neighbors[a].add(v)
            for v in col_con[j]:
                neighbors[a].add(v)
            for v in block_con[i//sub_height*n//sub_width+j//sub_width]:
                neighbors[a].add(v)
            if a in neighbors[a]:
                neighbors[a].remove(a)
    board=[]
    for pos, val in enumerate(puzzle):
        if val!=".":
            board.append(val)
        else:
            board.append("".join(symbols))
    propagate(board)
    display(backtracking(board))

end=perf_counter()
print(end-start, "seconds")