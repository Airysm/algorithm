def solution(n, computers):
    visited = [False] * n
    count = 0
    
    def dfs(v):
        visited[v] = True
        
        for nei in range(n):
            if not visited[nei] and computers[v][nei]:
                dfs(nei)
                
    for idx in range(n):
        if not visited[idx]:
            dfs(idx)
            count += 1
            
    return count