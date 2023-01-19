from time import perf_counter
import random

def test_solution(state):
    for var in range(len(state)):
        left = state[var]
        middle = state[var]
        right = state[var]
        for compare in range(var + 1, len(state)):
            left -= 1
            right += 1
            if state[compare] == middle:
                print(var, "middle", compare)
                return False
            if left >= 0 and state[compare] == left:
                print(var, "left", compare)
                return False
            if right < len(state) and state[compare] == right:
                print(var, "right", compare)
                return False
    return True

def goal_test(state):
    col=set()
    for i in state:
        if i==None:
            return False
        col.add(i)
    return True

def possible(state, row, col):
    for x in state:
        if x==col:
            return False
    x=1
    while row-x>=0 and col-x>=0:
        if state[row-x]==col-x:
            return False
        x+=1
    x=1
    while row-x>=0 and col+x<n:
        if state[row-x]==col+x:
            return False
        x+=1
    x=1
    while row+x<n and col-x>=0:
        if state[row+x]==col-x:
            return False
        x+=1
    x=1
    while row+x<n and col+x<n:
        if state[row+x]==col+x:
            return False
        x+=1
    return True

def get_next(state):
    pos=[]
    for i in range(n):
        if state[i]==None:
            pos.append(i)
    return random.choice(pos)

def get_values(state, i):
    states=[]
    for j in range(n):
        if possible(state, i, j):
            states.append(j)
    random.shuffle(states)
    return states

def backtracking(state):
    if goal_test(state):
        return state
    var=get_next(state)
    for val in get_values(state, var):
        result=backtracking(state[:var]+[val]+state[var+1:])
        if result!=None:
            return result

def conflict(state, row, col):
    ans=0
    for i, x in enumerate(state):
        if x==col and i!=row:
            ans+=1
    x=1
    while row-x>=0 and col-x>=0:
        if state[row-x]==col-x:
            ans+=1
        x+=1
    x=1
    while row-x>=0 and col+x<n:
        if state[row-x]==col+x:
            ans+=1
        x+=1
    x=1
    while row+x<n and col-x>=0:
        if state[row+x]==col-x:
            ans+=1
        x+=1
    x=1
    while row+x<n and col+x<n:
        if state[row+x]==col+x:
            ans+=1
        x+=1
    return ans

def best(arr):
    minv=min(arr)
    new=[]
    for i, x in enumerate(arr):
        if x==minv:
            new.append(i)
    return random.choice(new)

def repair():
    state=[None for i in range(n)]
    for i in range(n):
        con=[conflict(state, i, j) for j in range(n)]
        state[i]=best(con)
    conflicts=[conflict(state, i, state[i]) for i in range(n)]
    while sum(conflicts)>0:
        prev=sum(conflicts)
        prev2=state
        maxv=max(conflicts)
        pos=[]
        for i, x in enumerate(conflicts):
            if x==maxv:
                pos.append(i)
        i=random.choice(pos)
        pos=[]
        for j in range(n):
            pos.append(conflict(state, i, j))
        state[i]=best(pos)
        conflicts=[conflict(state, i, state[i]) for i in range(n)]
    return state

while(True):
    n=int(input().strip())
    if n==0:
        break
    start=perf_counter()
    ans=repair()
    print(ans)
    if not test_solution(ans):
        print("Invalid Solution!")
    end=perf_counter()
    print(end-start, "seconds")