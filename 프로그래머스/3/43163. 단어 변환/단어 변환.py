visited = []
result = []

def dfs(begin, target, words, count):
    if begin == target:
        result.append(count)
        return
    
    for i in range(len(words)):
        if visited[i] == 1:
            continue
        if word_diff(begin, words[i]) == 1:
            visited[i] = 1
            dfs(words[i], target, words, count+1)
            visited[i] = 0

def word_diff(begin, target):
    diff = 0
    for i in range(len(begin)):
            if begin[i] != target[i]:
                diff += 1
    return diff

def solution(begin, target, words):
    for _ in range(len(words)):
        visited.append(0)
    
    if target not in words:
        return 0
        
    dfs(begin, target, words, 0)
    
    return min(result) 