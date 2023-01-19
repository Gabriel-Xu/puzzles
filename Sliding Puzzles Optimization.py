from time import perf_counter
import heapq

def distance(n, board, dct):
    ans=0
    for i in range(n):
        for j in range(n):
            k=i*n+j
            if board[k]==".":
                continue
            if board[k] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                a=dct[board[k]]
            else:
                a=int(board[k])-1
            ans+=abs(i-a//n)+abs(j-a%n)
    return ans

def inc(n, board, old, dct):
    for i in range(n):
        for j in range(n):
            a=i*n+j
            if old[a]==".":
                if i>0 and board[a-n]==".":
                    if dct[board[a]]//n>=i:
                        return -1
                elif i<n-1 and board[a+n]==".":
                    if dct[board[a]]//n<=i:
                        return -1
                elif j>0 and board[a-1]==".":
                    if dct[board[a]]%n>=i:
                        return -1
                elif j<n-1 and board[a+1]==".":
                    if dct[board[a]]%n<=i:
                        return -1
                return 1

def possible(n, board):
    count=0
    for i in range(n*n):
        for j in range(i+1, n*n):
            if board[i]>board[j] and board[i]!="." and board[j]!=".":
                count+=1
    if n%2==1:
        if count%2==1:
            return False
        return True
    for i in range(n):
        for j in range(n):
            if board[i*n+j]==".":
                if i%2==1 and count%2==0:
                    return True
                if i%2==0 and count%2==1:
                    return True
                return False

def print_puzzle(n, board):
    for i in range(n):
        for j in range(n):
            print(board[i*n+j], end=" ")
        print()

def find_goal(board):
    board=sorted(board)
    return "".join(board[1:])+board[0]

def get_children(n, board):
    for i in range(n):
        for j in range(n):
            a=i*n+j
            if board[a]==".":
                states=[]
                if i>0:
                    b=a-n
                    states.append(board[:b]+"."+board[b+1:a]+board[b]+board[a+1:])
                if i<n-1:
                    b=a+n
                    states.append(board[:a]+board[b]+board[a+1:b]+"."+board[b+1:])
                if j>0:
                    b=a-1
                    states.append(board[:b]+board[a]+board[b]+board[a+1:])
                if j<n-1:
                    b=a+1
                    states.append(board[:a]+board[b]+board[a]+board[b+1:])
                return states

lst=[]
with open(input("Filename: ").strip()) as f:
    for line in f:
        s=line.strip()
        lst.append(s)
for i, line in enumerate(lst):
    n=int(len(line)**.5)
    board=line
    print("Line "+str(i)+": "+board+", ", end="")
    start=perf_counter()
    dct={"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[j]:j for j in range(n*n)}
    goal=find_goal(board)
    if possible(n, board):
        visited=set()
        q=[(distance(n, board, dct), 0, board)]
        heapq.heapify(q)
        while len(q)!=0:
            state=heapq.heappop(q)
            if state[2]==goal:
                print("A* -", state[1], "moves", end="")
                break
            if state[2] not in visited:
                visited.add(state[2])
                for child in get_children(n, state[2]):
                    if child not in visited:
                        heapq.heappush(q, (state[0]+inc(n, child, state[2], dct)+1, state[1]+1, child))
    else:
        print("no solution determined", end="")
    end=perf_counter()
    print(" in", end-start, "seconds")