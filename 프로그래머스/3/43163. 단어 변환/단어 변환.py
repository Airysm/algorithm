from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    return bfs(begin, target, words)

def bfs(begin, target, words):
    queue = deque()
    queue.append([begin, 0])
    
    while queue:
        print(queue)
        word, count = queue.popleft()
        if word == target:
            return count
        
        for w in words:
            diff = 0
            for i in range(len(word)):
                if word[i] != w[i]:
                    diff += 1
            
            if diff == 1:
                queue.append([w, count+1])