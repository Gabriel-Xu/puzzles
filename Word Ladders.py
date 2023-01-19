from time import perf_counter
import heapq

start=perf_counter()

file1="Word Ladders Files/words_06_letters.txt" # Dictionary
file2="Word Ladders Files/puzzles_normal.txt" # Prompts

with open(file1) as f:
    words=[line.strip() for line in f]
    
adj={x:[] for x in words}
for i in range(len(words[0])):
    dct={x[:i]+x[i+1:]:[] for x in words}
    for j, x in enumerate(words):
        dct[x[:i]+x[i+1:]].append(j)
    for x in dct:
        lst=dct[x]
        for j in range(len(lst)):
            for k in range(j+1, len(lst)):
                adj[words[lst[j]]].append(words[lst[k]])
                adj[words[lst[k]]].append(words[lst[j]])

end=perf_counter()
print()
print("Time to create the data structure was:", end-start, "seconds")
print("There are",  len(words), "words in this dict.")

start=perf_counter()

with open(file2) as f:
    puzzles=[list(line.strip().split()) for line in f]

for i, cur in enumerate(puzzles):
    print()
    print("Line:", i)
    start_word=cur[0]
    end_word=cur[1]
    q=[[1, start_word, [start_word]]]
    heapq.heapify(q)
    visited={start_word}
    solved=False
    while len(q)!=0:
        word=heapq.heappop(q)
        if word[1]==end_word:
            print("Length is:", word[0])
            for row in word[2]:
                print(row)
            solved=True
            break
        for child in adj[word[1]]:
            if child not in visited:
                visited.add(child)
                heapq.heappush(q, [word[0]+1, child, word[2]+[child]])
    if not solved:
        print("No Solution!")

end=perf_counter()
print()
print("Time to solve all of these puzzles was:", end-start, "seconds")

start=perf_counter()

for i, cur in enumerate(puzzles):
    start_word=cur[0]
    end_word=cur[1]
    startq=[[1, start_word, [start_word]]]
    heapq.heapify(startq)
    start_vis={start_word:[1, [start_word]]}
    endq=[[1, end_word, [end_word]]]
    heapq.heapify(endq)
    end_vis={end_word:[1, [end_word]]}
    solved=False
    while len(startq)!=0 and len(endq)!=0:
        word=heapq.heappop(startq)
        if word[1] in end_vis:
            solved=True
            break
        for child in adj[word[1]]:
            if child not in start_vis:
                start_vis[child]=[word[0]+1, word[2]+[child]]
                heapq.heappush(startq, [word[0]+1, child, word[2]+[child]])
        word=heapq.heappop(endq)
        if word[1] in start_vis:
            solved=True
            break
        for child in adj[word[1]]:
            if child not in end_vis:
                end_vis[child]=[word[0]+1, word[2]+[child]]
                heapq.heappush(endq, [word[0]+1, child, word[2]+[child]])

end=perf_counter()
print("Time to solve all of these puzzles using bidirectional BFS was:", end-start, "seconds")