from time import perf_counter
import heapq

def to_string(board):
    ans=""
    for row in board:
        for hole in row:
            if hole:
                ans+="O"
            else:
                ans+="X"
    return ans

def to_list(board, n):
    ans=[]
    for i in range(n):
        ans.append([board[i*(i+1)//2+j]=="O" for j in range(i+1)])
    return ans

def display(board, n):
    for i in range(n):
        print(" "*(n-i-1), end="")
        for j in range(i+1):
            print(board[(i*(i+1))//2+j], end=" ")
        print()

def make(board, i1, j1, i2, j2, i3, j3):
    ans=[[hole for hole in row] for row in board]
    ans[i1][j1]=True
    ans[i2][j2]=True
    ans[i3][j3]=False
    return ans

def get_children(board, n):
    children=[]
    board=to_list(board, n)
    for i, row in enumerate(board):
        for j, hole in enumerate(row):
            if i<=n-3:
                if not hole and not board[i+1][j] and board[i+2][j]:
                    children.append(to_string(make(board, i, j, i+1, j, i+2, j)))
                if not hole and not board[i+1][j+1] and board[i+2][j+2]:
                    children.append(to_string(make(board, i, j, i+1, j+1, i+2, j+2)))
            if j>=2:
                if not hole and not board[i][j-1] and board[i][j-2]:
                    children.append(to_string(make(board, i, j, i, j-1, i, j-2)))
                if not hole and not board[i-1][j-1] and board[i-2][j-2]:
                    children.append(to_string(make(board, i, j, i-1, j-1, i-2, j-2)))
            if j<=i-2:
                if not hole and not board[i][j+1] and board[i][j+2]:
                    children.append(to_string(make(board, i, j, i, j+1, i, j+2)))
                if not hole and not board[i-1][j] and board[i-2][j]:
                    children.append(to_string(make(board, i, j, i-1, j, i-2, j)))
    return children

start=perf_counter()

n=int(input("What size board? ").strip())
board="O"+(n*(n+1)//2-1)*"X"
goal="X"+(n*(n+1)//2-1)*"O"
q=[[0, board, [board]]]
heapq.heapify(q)
visited={board}
while len(q)!=0:
    state=heapq.heappop(q)
    if state[1]==goal:
        for step in state[2]:
            display(step, n)
        print(state[0], end=" ")
        break
    for child in get_children(state[1], n):
        if child not in visited:
            visited.add(child)
            heapq.heappush(q, [state[0]+1, child, state[2]+[child]])

end=perf_counter()
print("moves found in", end-start, "seconds with BFS")

start=perf_counter()

board="O"+(n*(n+1)//2-1)*"X"
goal="X"+(n*(n+1)//2-1)*"O"
q=[[0, board, [board]]]
heapq.heapify(q)
visited={board}
while len(q)!=0:
    state=q.pop()
    if state[1]==goal:
        for step in state[2]:
            display(step, n)
        print(state[0], end=" ")
        break
    for child in get_children(state[1], n):
        if child not in visited:
            visited.add(child)
            heapq.heappush(q, [state[0]+1, child, state[2]+[child]])

end=perf_counter()
print("moves found in", end-start, "seconds with DFS")